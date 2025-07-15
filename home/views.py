from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from rooms.models import Room

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            room_count = Room.objects.count()
            context = {
                'rooms_count':room_count
            }
            return render(request,'rooms/rooms.html',context)
        else:
            messages.error(request, "账号或密码错误！")
            return redirect('home')
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
            messages.error(request, "创建用户失败，当前用户已存在！")
            return redirect('signup')
    return render(request,'home/signup.html')    