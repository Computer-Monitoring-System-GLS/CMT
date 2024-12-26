from django.urls import path
from cmt import  views

urlpatterns = [
    # path("", views.index, name = 'home'),
    path("system-info/", views.system_info, name='system_info'),
]
