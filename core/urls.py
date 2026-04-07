from django.contrib import admin
from django.urls import path
from tracker.views import skill_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', skill_list, name='home'),
]
