from django.urls import path

from . import views


urlpatterns = [
	path('chat/', views.chat, name='chat'),
	path('support', views.support, name='support'),
	path('unique', views.unique, name='unique'),
	path('calculator', views.calculator, name='calculator'),
	path('script', views.order, name='order'),
	path('articles/all/', views.articles, name='articles'),
	path('articles/get/<int:article_id>', views.article, name='article'),
	path('all/',views.all,name='all')

]

