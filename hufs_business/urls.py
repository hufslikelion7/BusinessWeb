from django.contrib import admin
from django.urls import path

import account.views
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', main.views.home, name="home"),
    # include 로 account url 관리하기전에 확인용으로 넣어놈.
    path('', account.views.signup, name="signup"),
    path('signupAction/', account.views.signupAction, name="signupAction"),
]
