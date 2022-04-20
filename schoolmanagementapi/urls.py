from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users', include('Users.urls')),
    path('api/v1/certificates', include('certificates.urls')),
    path('api/v1/Lectures/',include('lectures.urls')),
]