from django.urls import path

from .views import (
    register_view,
    login_view,
    logout_view,
    profile_view,
    profile_completion_view
)

app_name = 'accounts'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'), #the profile page
    path('profile/complete', profile_completion_view, name='profile-complete'), #where users fill their details
]