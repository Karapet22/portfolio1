from django.urls import path
from .views import (
    HomeListView, AboutListView, FAQsListView
)

urlpatterns = [
    path('', HomeListView.as_view()),
    path('about/', AboutListView.as_view()),
    path('faqs/', FAQsListView.as_view()),
]

 
