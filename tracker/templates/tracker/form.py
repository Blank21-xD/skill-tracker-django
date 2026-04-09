from django import forms
from .models import Skill


class SkillForm(forms.ModelForm):
class Meta:


model = Skill
fields = ['name', 'category', 'is_learned']

widgets = {
    'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Skill Name'}),
    'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Backend'}),
    'is_learned': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
}
