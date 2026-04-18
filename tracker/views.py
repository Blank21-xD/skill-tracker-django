from django.shortcuts import render, redirect  # Added redirect
from .models import Skill
from tracker.forms import SkillForm


def skill_list(request):
    # 1. If the user clicked "Submit" (POST)
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new skill to the database!
            return redirect('home')  # Refresh the page to show the new skill

    # 2. If the user is just looking at the page (GET)
    all_skills = Skill.objects.all()
    form = SkillForm()

    return render(request, 'tracker/skill_list.html', {
        'skills': all_skills,
        'form': form
    })


def delete_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill.delete()
    return redirect('skill_list')
