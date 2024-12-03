
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("contact.urls")),
    path('api-auth/',include('rest_framework.urls')),
    path('reader/', include("readers.urls")),
    path('books/', include("books.urls")),
    path('borrow/', include("borrow.urls")),
]
