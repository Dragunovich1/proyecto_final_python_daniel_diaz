from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Categoria(models.Model):
	nombre = models.CharField(max_length=255)

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)) )
		return reverse('home')

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	bio = models.TextField()
	profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")
	github_url = models.CharField(max_length=255, null=True, blank=True)
	linkedin_url = models.CharField(max_length=255, null=True, blank=True)
	facebook_url = models.CharField(max_length=255, null=True, blank=True)
	instagram_url = models.CharField(max_length=255, null=True, blank=True)
	twitter_url = models.CharField(max_length=255, null=True, blank=True)
	date_modified = models.DateTimeField(User, auto_now=True)


	def __str__(self):
		return str(self.user)

class Post(models.Model):
	titulo = models.CharField(max_length=255)
	header_image = models.ImageField(null=True, blank=True, upload_to="images/")
	titulo_tag = models.CharField(max_length=255, default="BlogFierros")
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	body = RichTextField(blank=True, null=True)
	#body = models.TextField()
	post_date = models.DateField(auto_now_add=True)
	post_time = models.TimeField(auto_now_add=True)
	categoria = models.CharField(max_length=255, default="Sin categoria")
	likes = models.ManyToManyField(User, related_name='blog_posts')


	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.titulo + ' | ' + str(self.autor)

	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)) )
		return reverse('home')

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	#name = models.CharField(max_length=255)
	name = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	comment_date = models.DateField(auto_now_add=True)
	comment_time = models.TimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.post.titulo, self.name)