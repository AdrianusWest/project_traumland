from django.shortcuts import render
from .models import Journal
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Создаём JournalListView, который будет получать все записи Journal
# в базе данных и передавать информацию в шаблон для отображения

class JournalListView(ListView):
    model = Journal
    template_name = 'journal/journal_list.html'
    context_object_name = 'journal_list'


# Создаём JournalCreateView, который будет добавлять новую запись

class JournalCreateView(CreateView):
    model = Journal
    template_name = 'journal/create_journal_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('journal_list')


# Создаём JournalUpdateView, который будет обновлять записи

class JournalUpdateView(UpdateView):
    model = Journal
    template_name = 'journal/update_journal_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('journal_list')


# Создаём JournalDeleteView, который будет удалять записи

class JournalDeleteView(DeleteView):
    model = Journal
    template_name = 'journal/delete_journal_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('journal_list')
