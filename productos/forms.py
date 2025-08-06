# products/forms.py
from django import forms
from .models import DemoRequest

class DemoRequestForm(forms.ModelForm):
    class Meta:
        model = DemoRequest
        fields = ['name', 'email', 'company', 'phone', 'message']
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Cuéntanos sobre tu negocio y necesidades específicas'
            })
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'