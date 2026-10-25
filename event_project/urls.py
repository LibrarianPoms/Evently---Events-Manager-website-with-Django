# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/create/', views.create_event, name='create_event'),
    path('event/<int:pk>/edit/', views.update_event, name='update_event'),
    path('event/<int:pk>/delete/', views.delete_event, name='delete_event'),
]
