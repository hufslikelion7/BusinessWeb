from .models import Users

from django import forms


class SignupForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['user_name', 'user_number', 'user_nickName','user_email','user_password','user_password2','user_tel']
        labels = {
            'user_name':'이름',
            'user_number':'학번',
            'user_nickName':'아이디',
            'user_password':'비밀번호',
            'user_password2':'비밀번호 확인',
            'user_email':'이메일',
            'user_tel':'전화번호'
        }