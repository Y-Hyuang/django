from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from homework.formviews import LoginForm,RegisterForm
from django.template.context import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from homework.models import UserProfile
# Create your views here.

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html', RequestContext(request, {'form':form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            human = True
            username = request.POST['username']
            password1 = request.POST['password']
#            password = make_password(password1, 'a', 'pbkdf2_sha256')
            user = auth.authenticate(username=username, password=password1)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/index/")
            else:
                return render_to_response('login.html', context_instance = RequestContext(request, {'form':form, 'password_is_wrong':True}))
        else:
            return render_to_response('login.html', RequestContext(request, {'form':form,}))
        
        

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/index/")

def index(request):
    return render_to_response('index.html', context_instance = RequestContext(request))

def register(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect("/index/")
    try:
        if request.method == 'POST':
         
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            type1 = request.POST['type']
            stu_num = request.POST['stu_num']
            error = []
            
            
            form = RegisterForm(request.POST)              
            if not form.is_valid():
                error.append('注册信息填写不完整')
                return render_to_response("register.html", context_instance = RequestContext(request, {'form':form, 'errors':error}))
            if form.is_valid():
                human = True
            if password1 != password2:
                error.append("两次输入密码不一致！")
                return render_to_response("register.html", context_instance = RequestContext(request, {'form':form, 'errors':error}))
            filterresult = User.objects.filter(username = username)
            if len(filterresult) > 0:
                error.append("用户名已存在")
                return render_to_response("register.html", context_instance = RequestContext(request, {'form':form, 'errors':error}))
            
            user = User()
            user.username = username
            user.set_password(password1)
            user.email = email
            user.save()
            
            profile = UserProfile()
            profile.user_id = user.id
            profile.phone = phone
            profile.address = address
            profile.type1 = type1 
            profile.stu_num = stu_num
            profile.save()
            
            newuser = auth.authenticate(username=username, password=password1)
            if newuser is not None and newuser.is_active:
                auth.login(request, newuser)
                return HttpResponseRedirect("/index/")
        else:
            form = RegisterForm()
            return render_to_response('register.html', RequestContext(request, {'form':form,}))
    except Exception as e :
  
        error.append(str(e))
        return render_to_response("register.html", context_instance = RequestContext(request, {'form':form, 'errors':error}))
    
    return render_to_response("register.html", context_instance = RequestContext(request, {'form':form}))
            
    