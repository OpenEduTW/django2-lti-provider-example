# django 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.http import StreamingHttpResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from webapp import forms

#  _                 _         _____                 
# | |               (_)       |  __ \                
# | |     ___   __ _ _ _ __   | |__) |_ _  __ _  ___ 
# | |    / _ \ / _` | | '_ \  |  ___/ _` |/ _` |/ _ \
# | |___| (_) | (_| | | | | | | |  | (_| | (_| |  __/
# |______\___/ \__, |_|_| |_| |_|   \__,_|\__, |\___|
#               __/ |                      __/ |     
#              |___/                      |___/      
######################################################
def index(request):
	if request.method == "POST":
		postform = forms.LoginPostForm(request.POST)
		if postform.is_valid():
			username = postform.cleaned_data['username']
			pd = postform.cleaned_data['pd']
			user1 = authenticate(username=username, password= pd)
			if user1 is not None:
				auth.login(request, user1)
				postform= forms.LoginPostForm()
				return redirect('/')
			else:
				message = '登入失敗!'
		else:
			message='驗證碼錯誤'
	else:
		message = '帳號,密碼及驗證碼都必須輸入!'
		postform = forms.LoginPostForm()
	return render(request, "index.html", locals())
