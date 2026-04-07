from django.shortcuts import render
from .models import Skill

def skill_list(request):
    # Grab ALL the skills from our "Pantry" (Database)
    all_skills = Skill.objects.all()
    
    # Send them to the "Plate" (HTML Template)
    return render(request, 'tracker/skill_list.html', {'skills': all_skills})