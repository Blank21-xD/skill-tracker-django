from django.contrib import admin
from django.urls import path, include  # 'include' is mandatory here

urlpatterns = [
    path('admin/', admin.site.urls),
    # This sends traffic to your tracker/urls.py
    path('', include('tracker.urls')),
]
