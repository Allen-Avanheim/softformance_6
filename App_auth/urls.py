from django.urls import path

from App_auth.views import *

app_name = 'App_auth'

urlpatterns = [
    path('', home, name='home'),
    path('login-or-signup/', login_or_signup, name='login-or-signup'),
    path('login-signup', login_signup, name='login-signup'),
    path('logout/', logout_view, name='logout'),
]
