"""SDGs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import accounts.views as accounts 
import boardapp.views as boardapp
import newsadm.views as newsadm
import introduction.views as introduction
import issue.views as issue
import quiz.views as quiz

urlpatterns = [
  path('admin/', admin.site.urls),
  
  # accounts
  path('', accounts.index),
  path('hello/', accounts.index),
  path('rank-list/', accounts.rank_list, name='rank-list'),
  path('login/', accounts.login),
  path('logout/', accounts.logout),
  path('mypage/', accounts.mypage),
  path('adduser/', accounts.adduser),
  path('register/', accounts.register,name='Register'),
  path('user/', accounts.interface),

  #newsadm
  path('newsindex/', newsadm.index),
  path('newsindex/<str:pageindex>/', newsadm.index),
  path('newsdetail/<int:detailid>/', newsadm.detail),
  path('newslogin/', newsadm.login),
  path('newslogout/', newsadm.logout),
  path('newsadminmain/', newsadm.adminmain),
  path('newsadminmain/<str:pageindex>/', newsadm.adminmain),
  path('newsadd/', newsadm.newsadd),
  path('newsedit/<int:newsid>/', newsadm.newsedit),
  path('newsedit/<int:newsid>/<str:edittype>/', newsadm.newsedit),
  path('newsdelete/<int:newsid>/', newsadm.newsdelete),
  path('newsdelete/<int:newsid>/<str:deletetype>/', newsadm.newsdelete),

  # boardapp
  path('showpost/', boardapp.showpost),
  path('showpost/prev/', boardapp.showpost),
  path('showpost/next/', boardapp.showpost),
  path('addpost/', boardapp.addpost),
  path('ducsssion/', boardapp.showpost),

  #introduction
  path('SDGs/', introduction.sdgs),
  path('SDGs/create/', introduction.create, name='create'),
  path('SDGs/edit/<int:pk>/', introduction.edit, name='edit'),
  path('SDGs/delete/<int:pk>/', introduction.delete, name='delete'),
  path('SDGs/<slug:slug>/', introduction.detail, name='detail'),

  #issue
  path('vote01/',issue.vote01),
  #path('result01/',iviews.result01),
  path('result01/', issue.result01, name='result01'),
  path('vote02/',issue.vote02),
  path('result02/',issue.result02),
  path('bigissue/',issue.bigissue),
  path('chart_data_form/',issue.chart_data),
  

  #quit_app
  # path('quiz/', include('quiz_app.urls', namespace='quiz_app')),
  path('quiz_already_answered/',quiz.quiz_already_answered,name='quiz_already_answered'),
  path('quiz_already_answered/<int:question_id>/',quiz.quiz_already_answered, name='quiz_already_answered'),
  path('quiz/take_quiz/<int:question_id>/',quiz.take_quiz, name='take_quiz'),

  #event
  #path('event/', bigevent),

  #allauth
  #path('accounts/', include('allauth.urls')),
  #path('captcha/', include('captcha.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
