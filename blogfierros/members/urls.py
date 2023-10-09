from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('registration/', UserRegisterView.as_view(), name='register'),
	path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
	#path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
	#path('<int:uid>/password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
	path('password_success', views.password_success, name="password_success"),
	path('login_success', views.login_success, name="login_success"),
	path('logout_success', views.logout_success, name="logout_success"),
	path('sign_in_success', views.sign_in_success, name="sign_in_success"),
	path('profile_edit_success', views.profile_edit_success, name="profile_edit_success"),
	path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
	path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
	path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
	path('profile_page_edit_success', views.profile_page_edit_success, name="profile_page_edit_success"),
	path('profile_list', views.profile_list, name="profile_list"),
	path('profile_page_edit_success', views.profile_page_edit_success, name="profile_page_edit_success"),
	path('profile_page_crete_success', views.profile_page_create_success, name="profile_page_create_success"),
]