"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('food',views.food,name='food'),
    path('e_shop',views.e_shop,name='e_shop'),
    path('another_home',views.another_home,name='another_home'),
    path('articles/', views.article_list, name='article_list'),  # Article list URL
    path('articles/create/', views.article_create, name='article_create'),
    path('articles/<int:article_id>/', views.article_details, name='article_details'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)