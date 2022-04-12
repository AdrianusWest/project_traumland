from django.shortcuts import render
from .models import Journal
from django.views.generic import ListView


# Создаем JournalListView, который будет получать все записи Journal
# в базе данных и передавать информацию в шаблон для отображения

class JournalListView(ListView):
    model = Journal
    template_name = 'journal_list.html'
    context_object_name = 'journal_list'
