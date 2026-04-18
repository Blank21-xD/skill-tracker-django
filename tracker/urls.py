from django.urls import path
from . import views

urlpatterns = [
    path('', views.skill_list, name='skill_list'),
    path('delete/<int:pk>/', views.delete_skill, name='delete_skill'),
]
