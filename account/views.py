from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


# Create your views here.

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():  # 检测表单是否有数据
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])  # 根据数据库对用户予以验证
            if user is not None:
                if user.is_active:  # 查看数据库中该用户是否处于活跃状态
                    login(request, user)
                    return HttpResponse('Authenticated', 'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
