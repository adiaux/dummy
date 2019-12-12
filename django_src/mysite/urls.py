
from django.contrib import admin
from django.urls import path
from pickup.views import (
    itemDetail,
    itemDetailList,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', itemDetail),
    path('list/', itemDetailList),
    
]

