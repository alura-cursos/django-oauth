from django.urls import path
from tech.views import index

urlpatterns = [
    path('', index, name='index')
]