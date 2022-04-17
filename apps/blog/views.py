import os
from syang.settings import BASE_DIR
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from blog.models import Hd_study, Practice, Study, StudyComment
from user.models import User
from django.utils.decorators import method_decorator
from markdown import markdown

# Create your views here.


def check_login(fn):
    def wrap(request, *args, **kwargs):
        if 'username' not in request.session or 'uid' not in request.session:
            return HttpResponseRedirect('/login/')
        else:
            if User.objects.filter(id=request.session['uid']):
                return fn(request, *args, **kwargs)
            else:
                if 'username' in request.session:
                    del request.session['username']
                if 'uid' in request.session:
                    del request.session['uid']
                return HttpResponseRedirect('/')
    return wrap


# 主页
class Index(View):
    def get(self, request: HttpRequest):
        articles_all = Hd_study.objects.all()
        articles = []
        # 首页展示的博客篇数
        count = 0
        for each in articles_all:
            articles.append(each)
            count += 1
            if count >= 6:
                break
        try:
            print(request.session['username'] + '访问了您的网站')
        except:
            print('游客登陆')
        return render(request, 'blog/index.html', {'articles': articles})


# 主页内容
@method_decorator(check_login, name='get')
class Content(View):
    def get(self, request: HttpRequest):
        article_id = request.GET['id']
        article = Hd_study.objects.get(id=article_id)
        try:
            Hd_study.objects.filter(id=article_id).update(read_count=article.read_count + 1)
        except Exception as e:
            print('--read_count error: %s' % e)
        return render(request, 'blog/content.html', {'article': article})


# 练字分享
@method_decorator(check_login, name='get')
class Practice_sharing(View):

    def get(self, request: HttpRequest):
        articles_all = Practice.objects.all()
        articles = []
        for each in articles_all:
            articles.append(each)
        articles.reverse()
        return render(request, 'blog/practice.html', {'articles': articles})


# 关于学习
@method_decorator(check_login, name='get')
class AboutStudy(View):
    def get(self, request: HttpRequest):
        articles_all = Study.objects.all()
        articles = []
        for each in articles_all:
            articles.append(each)

        articles.reverse()
        return render(request, 'blog/study.html', {'articles': articles})


# 关于学习内容
@method_decorator(check_login, name='get')
class StudyContent(View):
    def get(self, request: HttpRequest):
        article = Study.objects.get(id=request.GET['id'])
        article.content = markdown(
            article.content, extensions=[
                # extra 本身包含很多扩展
                'markdown.extensions.extra',
                # codehilite 是语法高亮
                'markdown.extensions.codehilite',
                # toc 是自动生成目录
                'markdown.extensions.toc',
            ]
        )
        try:
            Study.objects.filter(id=article.id).update(read_count=article.read_count + 1)
        except Exception as e:
            print('--read_count error: %s' % e)
        comments = list(StudyComment.objects.filter(article_id=article.id))
        comments.reverse()
        return render(request, 'blog/study_content.html', {'article': article, 'comments': comments})

    def post(self, request: HttpRequest):
        if request.POST['action'] == 'comment':
            comment = request.POST['comment']
            article_id = request.POST['article_id']
            username = request.session['username']
            uid = request.session['uid']
            user = User.objects.get(username=username)
            try:
                StudyComment.objects.create(username=username, comment=comment, article_id=article_id,
                                            user_image=str(user.image), user_id=uid)
            except Exception as e:
                print('--发表评论错误: %s' % e)
            print(username + '发表了评论' + comment)
            return HttpResponse('comment')

        if request.POST['action'] == 'approve':
            num = request.POST['num']
            num = int(str(num))
            comment_id = request.POST['comment_id']
            try:
                StudyComment.objects.filter(id=comment_id).update(agree=num)
            except Exception as e:
                print('--点赞更新失败: %s' % e)
            return HttpResponse('success')


# 用户上传头像
class UserImages(View):
    def post(self, request: HttpRequest):
        username = request.session['username']
        users = User.objects.filter(username=username)
        user = users[0]

        try:
            path = str(BASE_DIR) + '/media/' + str(user.image)
            os.remove(path)
        except:
            pass
        user.image = request.FILES['userImage']
        user.save()
        StudyComment.objects.filter(username=username).update(user_image=str(user.image))
        request.session['user_image'] = str(user.image)
        return HttpResponseRedirect('/')
