from django.shortcuts import render, redirect, render_to_response
from .forms import SignupForm
from .models import Origin_users
from django.contrib.auth.models import User
from django.contrib.auth import login

from django.db.models import Q

from django.contrib import messages

def signup(request):
    form = SignupForm()
    return render(request, 'signup.html', {'form':form})

def signupAction(request):
    num = request.POST.get('user_number')
    pd1 = request.POST.get('user_password')
    pd2 = request.POST.get('user_password2')

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            if Origin_users.objects.filter(origin_number=num) and (pd1 == pd2):
                form.save()
                return redirect('http://naver.com')
            elif(not Origin_users.objects.filter(origin_number=num)):
                context = {
                    'result' : -1, #false 경영대 학생이 아님
                    'form' : form
                }
                return render(request, 'signup.html', context)
            elif((pd1 != pd2)):
                context = {
                    'result' : 0, #비밀번호 확인이 동일하지 않은 경우
                    'form' : form
                }
                return render(request, 'signup.html', context)
            else:
                context = {
                    'result' : -2, #데이터 에러
                    'form' : form
                }
                return render(request, 'signup.html', context) #데이터가 없는 경우
        else:
            form = SignupForm()
            return render(request, 'signup.html', {'form': form,})