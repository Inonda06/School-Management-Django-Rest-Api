from django.db import router
from django.urls import URLPattern, path,include
from rest_framework import routers
from .views import CertificateViewset


router=routers.DefaultRouter()
router.register(r'',CertificateViewset)
urlpatterns =[
    path('', include(router.urls)),
]