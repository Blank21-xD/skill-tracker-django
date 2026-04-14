from django.contrib import admin
from django.urls import path
from tracker.views import skill_list
from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', skill_list, name='home'),
    path('delete/<int:pk>/', views.delete_skill, name='delete_skill'),
]
