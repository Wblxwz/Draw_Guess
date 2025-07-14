from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
    return render(request,'home/home.html')

def sign_up(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        if not User.objects.filter(username=nickname).exists():
            User.objects.create_user(username=nickname,password=password)
            messages.success(request, "创建用户成功！")
            return redirect('home')
        else:
            messages.success(request, "创建用户失败！")
            return redirect('signup')
    return render(request,'home/signup.html')
