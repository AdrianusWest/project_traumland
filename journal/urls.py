from django.urls import path
from . import views

urlpatterns = [
    path('journal/list', views.JournalListView.as_view(), name='journal_list'),
]
