from django.urls import path
from apiaccount.views import userloginView, userlogoutView, usersignupView

urlpatterns = [
    path('signup/', usersignupView, name='user-signup'),
    path('login/', userloginView, name='user-login'),
    path('logout/', userlogoutView, name='user-logout')
]