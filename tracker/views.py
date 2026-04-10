from django.shortcuts import render, redirect  # Added redirect
from .models import Skill
from .forms import SkillForm  # Import the form you made yesterday


def skill_list(request):
    all_skills = Skill.objects.all()
    form = SkillForm()  # Create a blank form to show on the page

    return render(request, 'tracker/skill_list.html', {
        'skills': all_skills,
        'form': form  # Send the form to the template
    })
