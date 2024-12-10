# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Tag siyahısını göstərəcək URL
    path('tags/', views.tag_list, name='tag_list'),
]
