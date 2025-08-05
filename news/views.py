from django.shortcuts import render
from .models import Event, Curio
from datetime import date, datetime
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar

class CuriosViews(DetailView):
    models = Curio

class CalendarView(ListView):
    model = Event
    template_name = 'news/cal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)
        cal.LocaleHTML

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

class CuriosViews(DetailView):
    model = Curio

        #curiosidad = Curio.objects.get()
    #return render(request, "curiosidades.html", curiosidad)

class Comment_Add(SuccessMessageMixin, CreateView):
    model = Comment
    forms = Comment
    fields = ('author', 'text', 'curio')
    success_message = 'Ha registrado correctamente su comentario. Gracias por compartir su sentir.'

    def get_success_url(self):
        return reverse('inicio')