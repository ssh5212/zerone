from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
	path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('signup/', views.signup, name='signup'),
	path('modify/<int:user_id>', views.account_modify, name='account_modify'),
	path('password_modify/<int:user_id>', views.password_modify, name='password_modify'),
]
