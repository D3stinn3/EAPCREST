from django.urls import path
from apievent.views import eventCreateView, eventDetailView

urlpatterns = [
    path('events/', eventCreateView, name='event-list-create'),
    path('events/<int:pk>/', eventDetailView, name='event-detail'),
]