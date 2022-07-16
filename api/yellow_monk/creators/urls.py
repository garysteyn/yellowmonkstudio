from django.urls import path
from . import views

#routes needing special views:

urlpatterns = [
    path('lol/', views.lol),
]
