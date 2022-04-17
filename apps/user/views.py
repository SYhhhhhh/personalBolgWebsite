from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from user.models import User

# Create your views here.


# 登录
class Login(View):
    def get(self, request: HttpRequest):
        return render(request, 'user/login.html')

    def post(self, request: HttpRequest):
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('--login user error %s' % e)
            return render(request, 'user/login.html', {'response': '该用户不存在'})

        if password != user.password:
            return render(request, 'user/login.html', {'response': '密码错误'})

        request.session['username'] = username
        request.session['uid'] = user.id
        request.session['user_image'] = str(user.image)
        request.session.set_expiry(36259200)

        res = HttpResponseRedirect('/')
        return res


def check_img(request, n):
    from PIL import Image, ImageDraw, ImageFont
    import random
    bgColor = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    img = Image.new('RGB', (100, 25), bgColor)
    draw = ImageDraw.Draw(img)
    for i in range(0, 100):
        xy = (random.randrange(0, 100), random.randrange(0, 25))
        fill = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        draw.point(xy, fill)

    str1 = '1AZQWXS5DEC3FRV4TGB8YH465N9UJM2IK7487987OLP6'
    rand_str = ''
    for i in range(4):
        rand_str += str1[random.randrange(0, len(str1))]

    font = ImageFont.truetype('DejaVuSans-Bold.ttf', 23)
    draw.text((5, random.randrange(-4, 3)), rand_str[0], font=font,
              fill=(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    draw.text((25, random.randrange(-4, 3)), rand_str[1], font=font,
              fill=(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    draw.text((50, random.randrange(-4, 3)), rand_str[2], font=font,
              fill=(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    draw.text((75, random.randrange(-4, 3)), rand_str[3], font=font,
              fill=(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    img.save('static/images/check_img/' + str(n) + '.png')
    return rand_str


# 注册
class Register(View):
    def get(self, request: HttpRequest):
        rand_words = []
        for n in range(1, 21):
            word = check_img(request, str(n))
            rand_words.append(word)
        request.session['rand_words'] = rand_words
        return render(request, 'user/register.html')

    def post(self, request: HttpRequest):

        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        qq = request.POST['qq']

        old_user = User.objects.filter(username=username)
        if old_user:
            return render(request, 'user/register.html', {'response': '用户名已存在'})

        if not username or not password or not password2:
            return render(request, 'user/register.html', {'response': '用户名或密码不能为空'})

        if password != password2:
            return render(request, 'user/register.html', {'response': '两次密码输入不一致'})

        rand_words = request.session['rand_words']
        n = int(str(request.POST['num']))
        rand_word = rand_words[n]
        rand_str = request.POST['rand_str']
        if str(rand_word) != str(rand_str).upper():
            return render(request, 'user/register.html', {'response': '验证码错误'})

        try:
            user = User.objects.create(username=username, password=password, qq=qq, ip=request.META['REMOTE_ADDR'])
        except Exception as e:
            print('--create user error %s' % e)
            return render(request, 'user/register.html', {'response': '用户名已存在'})

        request.session['username'] = username
        request.session['uid'] = user.id
        request.session['user_image'] = str(user.image)
        request.session.set_expiry(36259200)
        del request.session['rand_words']

        return HttpResponseRedirect('/')


# 退出登录
class Logout(View):
    def get(self, request: HttpRequest):
        if 'username' in request.session:
            del request.session['username']
        if 'uid' in request.session:
            del request.session['uid']
        try:
            if 'user_image' in request.session['user_image']:
                del request.session['user_image']
        except:
            pass
        return HttpResponseRedirect('/')
