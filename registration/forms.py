from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    #{{ form.as_p }}
    email = forms.EmailField(required=True, help_text="Requerido. 254 caracteres como máximo y debe ser un email válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(u'El email ya está registrado, pruebe con otro.')
        return email

""" class test(forms.ModelForm):
    cantidad = forms.TextInput(label="Cantidad", widget = forms.TextInput)
    producto = forms.HiddenInput() """

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3', 'placeholder':'Subir'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografía'}),
            'link': forms.URLInput(attrs={'class': 'form-control mt-3', 'placeholder':'enlace'}),
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, max_length=254, help_text="Requerido. 254 caracteres máximo y debe ser un email válido.")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email
                             

