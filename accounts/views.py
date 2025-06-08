from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ProfileCompletionForm
from .models import UserProfile
from django.urls import reverse
# Create your views here.

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('accounts:login'))
    return render(request, 'accounts/register.html', {'form': form})


def profile_view(request):
    if request.user.is_authenticated:
        context = {
            'profile': request.user.profile
        }
        return render(request, 'accounts/profile.html', context)
    else:
        return redirect('/accounts/login/?next=/accounts/profile/')
    
def profile_completion_view(request):
    try:
        profile_obj = get_object_or_404(UserProfile, user=request.user)
    except:
        profile_obj = None

    print(profile_obj)
    form = ProfileCompletionForm(request.POST or None, request.FILES or None, instance=profile_obj)
    context = {
        'form': form
    }
    if form.is_valid():
        profile = form.save(commit=False)
        if not profile.user:
            profile.user = request.user
        profile.save()
        return redirect(reverse('accounts:profile'))
    return render(request, 'accounts/profile-complete.html', context)



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
    return render(request, 'accounts/login.html', context = context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        next = request.GET.get('next', '/accounts/login/')
        return redirect(next)
    if request.htmx:
        return render(request, 'accounts/partials/par-logout.html', {})
    # if not request.htmx:
    return render(request, 'accounts/logout.html', {})





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

    