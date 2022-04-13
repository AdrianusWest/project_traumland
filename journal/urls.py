from django.urls import path
from . import views


urlpatterns = [
    path('journal/list', views.JournalListView.as_view(), name='journal_list'),
    path('journal/create_journal', views.JournalCreateView.as_view(), name='create_journal'),
    path('journal/update_journal/<pk>', views.JournalUpdateView.as_view(), name='update_journal'),
    path('journal/delete_journal/<pk>', views.JournalDeleteView.as_view(), name='delete_journal'),
]
