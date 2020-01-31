from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
	path('category', views.category, name='category'),
	path('', views.support, name='index'),

]