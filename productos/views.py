from django.shortcuts import render
from datetime import date, datetime
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.safestring import mark_safe

# products/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import DemoRequestForm

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    if request.method == 'POST':
        form = DemoRequestForm(request.POST)
        if form.is_valid():
            demo_request = form.save(commit=False)
            demo_request.product = product
            demo_request.save()
            return render(request, 'demo_thankyou.html', {'product': product})
    else:
        form = DemoRequestForm()
    
    context = {
        'product': product,
        'form': form,
        'features': product.features_list(),
        'benefits': product.benefits_list()
    }
    return render(request, 'product_detail.html', context)

