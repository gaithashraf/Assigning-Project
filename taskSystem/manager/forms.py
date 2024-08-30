from django import forms
from .models import Task,Report

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = widgets = {'dueDate': forms.NumberInput(attrs={'type': "date"})}

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = "__all__"
        widgets = widgets = {'report':forms.Textarea}