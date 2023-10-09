from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Categoria, Comment, Profile
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

#def home(request):
#	return render(request, 'home.html', {})

def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True

	return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-post_date', '-post_time']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Categoria.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

def CategoriaListView(request):
	cat_menu_list = Categoria.objects.all()
	return render(request, 'categoria_list.html', {'cat_menu_list':cat_menu_list})

def CategoriaView(request, cats):
	categoria_posts = Post.objects.filter(categoria=cats.replace('-', ' '))
	return render(request, 'categorias.html', {'cats':cats.title().replace('-', ' '), 'categoria_posts':categoria_posts})

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Categoria.objects.all()
		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()

		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True

		context["cat_menu"] = cat_menu
		context["total_likes"] = total_likes
		context["liked"] = liked
		return context


class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	success_url = reverse_lazy('add_comment_success')
	#success_url = reverse_lazy('home')

	def form_valid(self, form):
		form.instance.post_id =  self.kwargs['pk']
		return super().form_valid(form)

class EditCommentView(UpdateView):
	model = Comment
	form_class = CommentForm
	template_name = 'edit_comment.html'
	success_url = reverse_lazy('edit_comment_success')
	#success_url = reverse_lazy('home')

	def get_context_data(self, *args, **kwargs):
		cat_menu = Categoria.objects.all()
		context = super(EditCommentView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context


class DeleteCommentView(DeleteView):
	model = Comment
	template_name = 'delete_comment.html'
	success_url = reverse_lazy('delete_comment_success')
	#success_url = reverse_lazy('home')

	def get_context_data(self, *args, **kwargs):
		cat_menu = Categoria.objects.all()
		context = super(DeleteCommentView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class CrearPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'crear_post.html'
	#fields = '__all__'
	#fields = ('titulo', 'autor', 'body')
	success_url = reverse_lazy('crear_post_success')

	def get_context_data(self, *args, **kwargs):
		cat_menu = Categoria.objects.all()
		context = super(CrearPostView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class CrearCategoriaView(CreateView):
	model = Categoria
	#form_class = PostForm
	template_name = 'crear_categoria.html'
	fields = '__all__'
	#fields = ('titulo', 'autor', 'body')
	success_url = reverse_lazy('crear_categoria_success')

	def get_context_data(self, *args, **kwargs):
		cat_menu = Categoria.objects.all()
		context = super(CrearCategoriaView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'
	#fields = ['titulo', 'body']
	success_url = reverse_lazy('update_post_success')

	def get_context_data(self, *args, **kwargs):
		cat_menu = Categoria.objects.all()
		context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('delete_post_success')

	def get_context_data(self, *args, **kwargs):
		cat_menu = Categoria.objects.all()
		context = super(DeletePostView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

def update_post_success(request):
	return render(request, 'update_post_success.html', {})

def delete_post_success(request):
	return render(request, 'delete_post_success.html', {})

def crear_categoria_success(request):
	return render(request, 'crear_categoria_success.html', {})

def crear_post_success(request):
	return render(request, 'crear_post_success.html', {})

def add_comment_success(request):
	return render(request, 'add_comment_success.html', {})

def edit_comment_success(request):
	return render(request, 'edit_comment_success.html', {})

def delete_comment_success(request):
	return render(request, 'delete_comment_success.html', {})

def search(request):
	if request.method == "POST":
		#Guardo lo que se busca
		search = request.POST['search']
		#Busco en la base de datos
		searched = Post.objects.filter(body__contains = search)

		return render(request, 'search.html', {'search':search, 'searched':searched})
	else:
		return render(request, 'search.html', {})


def search_user(request):
	if request.method == "POST":
		#Guardo lo que se busca
		search = request.POST['search']
		#Busco en la base de datos
		searched = User.objects.filter(username__contains = search)

		return render(request, 'search_user.html', {'search':search, 'searched':searched})
	else:
		return render(request, 'search_user.html', {})


def about(request):
	return render(request, 'about.html')