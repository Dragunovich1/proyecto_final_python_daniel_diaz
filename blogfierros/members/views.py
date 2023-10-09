from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, CreateView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, ProfilePageForm
from appfierros.models import Profile, Categoria
from django.contrib import messages

class CreateProfilePageView(CreateView):
	model = Profile
	form_class = ProfilePageForm
	template_name = "registration/create_user_profile_page.html"
	success_url = reverse_lazy('profile_page_create_success')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def get_context_data(self, *args, **kwargs):
		cat_menu = Categoria.objects.all()
		context = super(CreateProfilePageView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class EditProfilePageView(generic.UpdateView):
	model = Profile
	form_class = ProfilePageForm
	template_name = 'registration/edit_profile_page.html'
	success_url = reverse_lazy('profile_page_edit_success')
	#fields = ['bio', 'profile_pic', 'github_url', 'linkedin_url', 'facebook_url', 'instagram_url', 'twitter_url']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Categoria.objects.all()
		context = super(EditProfilePageView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class ShowProfilePageView(DetailView):
	model = Profile
	template_name = 'registration/user_profile.html'

	def get_context_data(self, *args, **kwargs):
		#users = Profile.objects.all()
		context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
		page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
		context["page_user"] = page_user
		return context

def logout_success(request):
    logout(request)
    return render(request, 'registration/logout_success.html', {})

def login_success(request):
    user = request.user  # Obtén el usuario que ha iniciado sesión
    login(request, user)  # Llama a la función login con el usuario
    return render(request, 'registration/login_success.html', {})


class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangeForm
	#success_url = reverse_lazy('home')
	success_url = reverse_lazy('password_success')

	def get_context_data(self, *args, **kwargs):
		cat_menu = Categoria.objects.all()
		context = super(PasswordsChangeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context


def password_success(request):
	return render(request, 'registration/password_success.html', {})

class UserRegisterView(generic.CreateView):
	form_class = SignUpForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('sign_in_success')

	def get_context_data(self, *args, **kwargs):
		cat_menu = Categoria.objects.all()
		context = super(UserRegisterView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

def sign_in_success(request):
	return render(request, 'registration/sign_in_success.html', {})

class UserEditView(generic.UpdateView):
	form_class = EditProfileForm
	#fields = ('username', 'first_name', 'last_name', 'email', 'password')
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('profile_edit_success')

	def get_object(self):
		return self.request.user

	def get_context_data(self, *args, **kwargs):
		cat_menu = Categoria.objects.all()
		context = super(UserEditView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

def profile_list(request):
	if request.user.is_authenticated:
		profiles = Profile.objects.exclude(user=request.user)
		return render(request, 'registration/profile_list.html', {"profiles":profiles})
	else:
		messages.success(request, ("Debes iniciar sesión para ingresar a esta sección"))
		return redirect('home')

def profile_edit_success(request):
	return render(request, 'registration/profile_edit_success.html', {})

def profile_page_create_success(request):
	return render(request, 'registration/profile_page_create_success.html', {})

def profile_page_edit_success(request):
	return render(request, 'registration/profile_page_edit_success.html', {})

	
