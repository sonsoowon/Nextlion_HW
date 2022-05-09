"""Sugang URL Configuration

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
from django.urls import path
from sugangApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('addMajor', MajorAddView.as_view(), name='addMajor'),
    path('editMajor/<int:pk>', MajorEditView.as_view(), name='editMajor'),
    path('deleteMajor/<int:major_pk>', delete_major, name='deleteMajor'),

    path('subjects/<str:major_name>', filter_subject,name='filterSubject'),

    path('addSubject', SubjectAddView.as_view(), name='addSubject'),
    path('detail/<int:pk>', SubjectDetailView.as_view(), name='detail'),
    path('editSubject/<int:pk>', SubjectEditView.as_view(), name='editSubject'),
    path('deleteSubject/<int:subject_pk>', delete_subject, name='deleteSubject')
]
