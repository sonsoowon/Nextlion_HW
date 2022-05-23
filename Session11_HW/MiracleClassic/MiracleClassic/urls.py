"""MiracleClassic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('post_list/<str:category>', views.post_list, name="post_list"),
    path('post_detail/<int:post_pk>', views.post_detail, name="post_detail"),
    path('edit_post/<int:post_pk>', views.edit_post, name="edit_post"),
    path('delete_post/<int:post_pk>', views.delete_post, name="delete_post"),
    path('new_post', views.new_post, name="new_post"),
    path('book_detail/<int:book_pk>', views.book_detail, name="book_detail"),

    path('delete_comment/<int:post_pk>/<int:comment_pk>', views.delete_comment, name="delete_comment"),

    path('logout', views.logout, name="logout"),
    path('accounts/', include("allauth.urls"))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)