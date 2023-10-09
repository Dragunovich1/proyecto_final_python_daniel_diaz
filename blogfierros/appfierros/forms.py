from django import forms
from .models import Post, Categoria, Comment

#choices = [('coupe', 'coupe'), ('sedan', 'sedan'), ('hatchback', 'hatchback'),]
choices = Categoria.objects.all().values_list('nombre','nombre')

choice_list = []

for item in choices:
	choice_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('titulo', 'titulo_tag', 'autor', 'categoria', 'header_image', 'body')

		widgets = {
			'titulo': forms.TextInput(attrs={'class': 'form-control'}),
			'titulo_tag': forms.TextInput(attrs={'class': 'form-control'}),
			'autor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'default', 'type':'hidden'}),
			#'autor': forms.Select(attrs={'class': 'form-control'}),
			'categoria': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}

class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('titulo', 'titulo_tag', 'categoria', 'body')

		widgets = {
			'titulo': forms.TextInput(attrs={'class': 'form-control'}),
			'titulo_tag': forms.TextInput(attrs={'class': 'form-control'}),
			'categoria': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'body')

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'default', 'type':'hidden'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}


class CommentEditForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)

		widgets = {
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}

