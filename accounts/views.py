from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from articles.forms import LoginForm
# Create your views here.

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
# now with AuthenticationForm
    context = {}
    if 'next' in request.GET:
        context ['message'] = 'you need to be logged in to access this page. please login below'
    if request.method == 'POST':
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next = request.GET.get('next', '/')
            return redirect(next)
        else:
            context['form'] = form
    else:
        form = AuthenticationForm(request)
        context['form'] = form
    return render(request, 'accounts/formlogin.html', context = context)


    # (this was by using forms.form).
    #form = LoginForm(request.POST or None)
    #context = {
    #    'form' : form
    #}
    #if 'next' in request.GET:
    #    context ['message'] = 'you need to be logged in to access this page. please login below'
    #if form.is_valid():
    #    username = form.cleaned_data.get('username')
    #    password = form.cleaned_data.get('password')
    #    user = authenticate(request, username=username, password=password)
    #    if user is None:
    #        context['WUP'] = 'invalid username or password'
    #        return render(request, 'accounts/formlogin.html', context=context)
    #    login(request, user)
    #    next = request.GET.get('next', '/')
    #    return redirect(next)
    #return render(request, 'accounts/formlogin.html', context=context)


    # (this is the old manual way)  
    # context = {}
    # if 'next' in request.GET:
    #     context ['message'] = 'you need to be logged in to access this page. please login below'
    # if request.method == 'POST':       
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username= username, password= password)
    #     if user is None:
    #         context = {'WUP': 'invalid Username or Password'}
    #         return render (request, 'accounts/login.html', context=context)
    #     login(request, user)
    #     next = request.GET.get('next', '/')
    #     return redirect(next)
    # return render(request, 'accounts/login.html', context=context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        next = request.GET.get('next', '/login/')
        return redirect(next)
    return render(request, 'accounts/logout.html', {})

def log_view(request):
    return render(request, 'accounts/logout.html', {})