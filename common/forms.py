from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


class UserForm(UserCreationForm):
	email = forms.EmailField(label="이메일")

	realname = forms.Field(label="실명")
	hobby = forms.Field(label="취미")
	forte = forms.Field(label="특기")
	addr1 = forms.Field(label="주소1")
	intro = forms.Field(label="한줄소개")
	profileImage = forms.Field(label="프로필이미지")

	class Meta:
		model = User
		fields = ["username", "email", "realname", "hobby", "forte", "addr1", "intro", "profileImage"]


class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = get_user_model()
		fields = ['hobby', 'forte', 'addr1', 'email', 'intro', 'profileImage']
