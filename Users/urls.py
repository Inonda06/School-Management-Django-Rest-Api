from django.db import router
from django.urls import URLPattern, path,include
from rest_framework import routers
from .views import UserViewSet


router=routers.DefaultRouter()
router.register(r'',UserViewSet)
urlpatterns =[
    path('', include(router.urls)),
]