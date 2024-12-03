from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register('list',BooksViewsets,)
router.register('category',CategoryViewset,)
router.register('review',ReviewViewset,)

urlpatterns = [
    path('',include(router.urls)),
]

