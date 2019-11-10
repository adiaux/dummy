
from django.contrib import admin
from django.urls import path
from pickup.views import itemDetail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', itemDetail),
]

