from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import ContactViewset
router=DefaultRouter()
router.register('contact',ContactViewset)
urlpatterns = [
    path('',include(router.urls)),
]
