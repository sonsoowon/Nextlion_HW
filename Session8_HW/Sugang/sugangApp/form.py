
from django import forms
from .models import *

class MajorModelForm(forms.ModelForm):
    class Meta:
        model = Major
        fields = ('major_name',)
        widgets = {
            'major_name': forms.TextInput(attrs={'required': True, 'class':'name'})
        }
        labels = {
            'major_name': '전공명'
        }

class SubjectModelForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('name', 'belong_major', 'prof', 'memo')
        widgets = {
            'name': forms.TextInput(attrs={'required': True, 'class': 'name'}),
            'belong_major': forms.Select(attrs={'class': 'select'}),
            'prof': forms.TextInput(attrs={'class': 'name'}),
            'memo': forms.Textarea(attrs={'cols': '50', 'rows': '20', 'class':'memo'})
        }
        labels = {
            'name': '교과목명',
            'belong_major': '개설학과',
            'prof': '담당교수',
            'memo': '세부사항'
        }
