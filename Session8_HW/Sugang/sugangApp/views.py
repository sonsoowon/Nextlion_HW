from django.shortcuts import render, redirect, get_object_or_404
from django .urls import reverse_lazy
from .models import Major, Subject
from .form import MajorModelForm, SubjectModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    majors = Major.objects.all()
    subjects = Subject.objects.all()
    
    return render(request, 'index.html', {
        'majors': majors,
        'subjects': subjects
    })

def filter_subject(request, major_name):
    major = Major.objects.get(major_name=major_name)
    subjects = Subject.objects.filter(belong_major=major)

    return render(request, 'list_subject.html', {
        'major': major,
        'subjects': subjects
    })


class MajorAddView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'add_major.html'
    success_url = reverse_lazy('home')

class MajorEditView(UpdateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'edit_major.html'
    success_url = reverse_lazy('home')

def delete_major(request, major_pk):
    Major.objects.get(pk=major_pk).delete()
    return redirect('home')



class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'detail.html'

class SubjectAddView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'add_subject.html'
    success_url = reverse_lazy('home')

class SubjectEditView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'edit_subject.html'
    success_url = reverse_lazy('home')


def delete_subject(request, subject_pk):
    Subject.objects.get(pk=subject_pk).delete()
    return redirect('home')