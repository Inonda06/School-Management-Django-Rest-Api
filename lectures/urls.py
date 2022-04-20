from django.db import router
from django.urls import URLPattern, path,include
from rest_framework import routers
from .views import LecturesViewset


router=routers.DefaultRouter()
router.register(r'',LecturesViewset)
urlpatterns =[
    path('', include(router.urls)),
]