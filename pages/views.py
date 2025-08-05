from django.shortcuts import render, get_object_or_404
from .models import Pagina
from news.models import Event 

def page(request, page_id, page_slug):
    page = get_object_or_404(Pagina, id=page_id)
    return render(request, 'pages/sample.html', {'page':page})