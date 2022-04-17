from django.urls import path, re_path
from blog import views
from django.views.static import serve
from syang import settings

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('content/', views.Content.as_view(), name='content'),
    path('practice/', views.Practice_sharing.as_view(), name='practice'),
    path('study/', views.AboutStudy.as_view(), name='study'),
    path('studyContent/', views.StudyContent.as_view(), name='study_content'),
    path('userImages/', views.UserImages.as_view(), name='user_images'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
