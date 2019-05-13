"""PersonnalBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'^$', views.dashboard, name="home"),
    url(r'^load_article/(?P<catagory_id>\d+)/$', views.load_article, name="load_article"),
    url(r'^article_detail/(?P<article_id>\d+)/$', views.article_details, name="article_details"),
    url(r'^save_comment/$', views.save_comment, name="save_comment"),
    url(r'^about_me/$', views.AboutMe.as_view(), name="about_me"),
    url(r'^archives/$', views.archives, name="archives"),
]
