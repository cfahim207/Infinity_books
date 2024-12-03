from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()

router.register('list',ReaderViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('register/',UserRegisterView.as_view(),name='register'),
    path('login/',UserLoginApiView.as_view(),name='login'),
    path('logout/',UserLogoutApiView.as_view(),name='logout'),
    path('active/<uid64>/<token>', activate,name='activate'),
    
]
