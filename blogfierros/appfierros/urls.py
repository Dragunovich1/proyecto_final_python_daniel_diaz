from django.urls import path
from . import views
from .views import AddCommentView, DeleteCommentView, EditCommentView, HomeView, ArticleDetailView, CrearPostView, UpdatePostView, DeletePostView, CrearCategoriaView, CategoriaView, CategoriaListView, LikeView

urlpatterns = [
	#path('', views.home, name="home"),
	path('', HomeView.as_view(), name="home"),
	path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
	path('crear_post/', CrearPostView.as_view(), name='crear_post'),
	path('crear_categoria/', CrearCategoriaView.as_view(), name='crear_categoria'),
	path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
	path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
	path('categoria/<str:cats>/', CategoriaView, name='categoria'),
	path('categoria-list', CategoriaListView, name='categoria-list'),
	path('like/<int:pk>', LikeView, name='like_post'),
	path('delete_post_success', views.delete_post_success, name="delete_post_success"),
	path('update_post_success', views.update_post_success, name="update_post_success"),
	path('crear_categoria_success', views.crear_categoria_success, name="crear_categoria_success"),
	path('crear_post_success', views.crear_post_success, name="crear_post_success"),
	path('add_comment_success', views.add_comment_success, name="add_comment_success"),
	path('delete_comment_success', views.delete_comment_success, name="delete_comment_success"),
	path('edit_comment_success', views.edit_comment_success, name="edit_comment_success"),	
	path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
	path('article/<int:pk>/comment/remove/', DeleteCommentView.as_view(), name='delete_comment'),
	path('article/<int:pk>/comment/edit/', EditCommentView.as_view(), name='edit_comment'),
	path('search_user/', views.search_user, name='search_user'),
	path('search/', views.search, name='search'),
	path('about', views.about, name='about'),
]