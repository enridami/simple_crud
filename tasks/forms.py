from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important'] 
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un titulo'}),
            'description': forms.Textarea(attrs={'class': 'form-control' , 'placeholder': 'Descripcion de la tarea'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-text-input m-auto'}),
        }
        labels = {
            'title': 'Título',
            'description': 'Descripción',            
            'important': 'Importante'
        }