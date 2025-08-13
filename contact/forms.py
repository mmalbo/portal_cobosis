from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True,
                           widget=forms.TextInput(attrs={'placeholder':'Escribe tu nombre', 'class': 'form-control'}))
    email = forms.EmailField(label="Correo", required=True,
                           widget=forms.TextInput(attrs={'placeholder':'Escribe tu correo', 'class': 'form-control'}))
    content = forms.CharField(label="Mensaje", min_length=10, max_length=1000, required=True,
                           widget=forms.Textarea(attrs={'placeholder':'Escribe tu mensaje', 'rows':3, 'class': 'form-control'}))
