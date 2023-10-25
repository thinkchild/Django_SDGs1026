from django.shortcuts import render,redirect

# 匯入相關套件
from django.http import HttpResponse
import datetime
# login authentication
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from .models import UserProfile
from boardapp import models as bmodel
from newsadm.models import NewsUnit
import math


# 首頁
def index(request, pageindex=None):
    users = UserProfile.objects.order_by('-cv', 'cp')
    global page1
    #每頁顯示資料筆數
    pagesize = 3
    newsall = NewsUnit.objects.all().order_by('-id')
    #計算新聞總筆數
    datasize = len(newsall)
    #計算新聞頁數
    totpage = math.ceil(datasize / pagesize)
    if pageindex == None:
        page1 = 1
        newsunits = NewsUnit.objects.filter(
        enabled=True).order_by('-id')[:pagesize]
    elif pageindex == '1':
        start = (page1 - 2) * pagesize
        if start >= 0:
            newsunits = NewsUnit.objects.filter(
            enabled=True).order_by('-id')[start:(start + pagesize)]
            page1 -= 1
    elif pageindex == '2':
        start = page1 * pagesize
        if start < datasize:
            newsunits = NewsUnit.objects.filter(
            enabled=True).order_by('-id')[start:(start + pagesize)]
            page1 += 1
    elif pageindex == '3':
        start = (page1 - 1) * pagesize
        newsunits = NewsUnit.objects.filter(
        enabled=True).order_by('-id')[start:(start + pagesize)]
        currentpage = page1

    boardall = bmodel.BoardUnit.objects.all().order_by('-id')  #讀取資料表,依時間遞減排
    datasize = len(boardall)  #資料筆數
    totpage = math.ceil(datasize / pagesize)  #總頁數
    if pageindex==None:  #無參數
        page = 0
        boardunits = bmodel.BoardUnit.objects.order_by('-id')[:pagesize]
    elif pageindex=='prev':  #上一頁
        start = (page-1)*pagesize  #該頁第1筆資料
        if start >= 0:  #有前頁資料就顯示
            boardunits = bmodel.BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
            page -= 1
        elif pageindex=='next':  #下一頁
            start = (page+1)*pagesize  #該頁第1筆資料
            if start < datasize:  #有下頁資料就顯示
                boardunits = bmodel.BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
                page += 1
                currentpage = page + 1  #將目頁前頁面以區域變數傳回html
    return render(request, "accounts/hello.html", locals())

def login(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=name, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				return redirect('/hello')
				mess = '登入成功！'
			else:
				mess = '帳號尚未啟用！'
		else:
			mess = '登入失敗！'
	return render(request, "accounts/login.html", locals())
	
def logout(request):
	auth.logout(request)
	return redirect('/hello')


def adduser(request):	
	try:
		# 抓取單一使用者帳號
		user=User.objects.get(username="test")
	except:
		user=None
	if user!=None:
		mess = user.username + " 帳號已建立!"
		return HttpResponse(mess)
	else:	# 建立 test 帳號			
		user=User.objects.create_user("test","test@test.com.tw","a123456!")
		user.first_name="wen" # 姓名
		user.last_name="lin"  # 姓氏
		user.is_staff=True	# 工作人員狀態
		user.save()
		return redirect('/admin/')

def register(request):
    # if request.method == "register":      
    #     user=User.objects.create_user(first_name, last_name, is_staff)
    #     user.first_name = request.POST['first_name'] 
    #     user.last_name = request.POST['last_name']
    #     user.email_address =  request.POST['email_address']
	#  	#新增一筆記錄
    #     unit = User.objects.create(first_name=user.first_name,  last_name=user.last_name, email_address=user.email_address)
    #     unit.save()  #寫入資料庫
    #     return redirect('/admin/')
    # else:
        return render(request, "accounts/register.html", locals())
	

def mypage(request):
    if request.user.is_authenticated:
        name=request.user.username
    return render(request, "accounts/hello.html", locals())

def rank_list(request):
  users = UserProfile.objects.order_by('-cv', 'cp')
  return render(request, 'myapp/RankList.html', {'users': users})

def interface(request):
  # 获取当前登录用户的UserProfile对象
  current_user_profile = UserProfile.objects.get(user=request.user)
  # 从UserProfile对象中提取CP值
  cp_value = current_user_profile.cp
  cv_value = current_user_profile.cv
  # 从UserProfile对象中提取NAME值
  username = current_user_profile.user
  # 从UserProfile对象中提取STDSEX值
  stdsex_value = current_user_profile.stdsex
  return render(request, 'user_interface/user.html', {'cp_value': cp_value,'cv_value': cv_value,'username': username,'stdsex_value': stdsex_value}  )
# Create your views here.
