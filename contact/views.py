from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
from ..proyectos_muhia.settings import EMAIL_HOST_USER

def contact(request):
    contact_form = ContactForm
    if request.method == "POST":
        contact_form = contact_form(data=request.POST)
        if contact_form.is_valid:
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            e_mail = EmailMessage(
                "DRUIDA: Nuevo mensaje de la página",
                "De {} <{}>\n\n{}".format(name, email, content),
                EMAIL_HOST_USER,
                ['ycocab@gmail.com'],
            )
            try:
                e_mail.send()
                return redirect(reverse('contact'), "?ok")
            except:
                return redirect(reverse('contact'), "?fail")
    return render(request, "contact/contactos.html", {'form':contact_form})
