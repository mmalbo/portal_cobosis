from django.contrib import admin
from django.utils.html import format_html
from django_ckeditor_5.fields import CKEditor5Field
from .models import Profile, Experience, Project, Education, Publication, Event, Award, Skill, Certification
# admin.py
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

# Formulario personalizado para Profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'summary': CKEditor5Widget(
                attrs={'class': 'django_ckeditor_5'}, 
                config_name='extends'
            ),
        }

# Formulario para Experience
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        widgets = {
            'description': CKEditor5Widget(
                attrs={'class': 'django_ckeditor_5'}, 
                config_name='default'
            ),
            'achievements': CKEditor5Widget(
                attrs={'class': 'django_ckeditor_5'}, 
                config_name='default'
            ),
        }

# Formulario para Project
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'description': CKEditor5Widget(
                attrs={'class': 'django_ckeditor_5'}, 
                config_name='default'
            ),
        }

# Inlines
class ExperienceInline(admin.StackedInline):
    model = Experience
    form = ExperienceForm
    extra = 1
    fields = ['position', 'company', 'description', 'achievements', 'start_date', 'end_date', 'order']

class ProjectInline(admin.StackedInline):
    model = Project
    form = ProjectForm
    extra = 1
    fields = ['name', 'role', 'description', 'technologies', 'start_date', 'end_date', 'order']

class EducationInline(admin.StackedInline):
    model = Education
    extra = 1
    fields = ['degree', 'institution', 'description', 'start_date', 'end_date', 'order']

class PublicationInline(admin.StackedInline):
    model = Publication
    extra = 1
    fields = ['title', 'journal', 'description', 'year', 'role', 'order']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm
    list_display = ['user_full_name', 'title', 'is_public', 'created_at']
    list_filter = ['is_public', 'created_at']
    search_fields = ['user__first_name', 'user__last_name', 'title']
    
    fieldsets = (
        ('Información básica', {
            'fields': ('user', 'title', 'cargo', 'bio', 'profile_photo', 'avatar')
        }),
        ('Información de contacto', {
            'fields': ('location', 'email', 'phone')
        }),
        ('Redes sociales', {
            'fields': ('linkedin', 'twitter', 'github', 'website'),
            'classes': ('collapse',)
        }),
        ('Configuración', {
            'fields': ('is_public', 'created_at', 'updated_at')
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at', 'profile_photo']
    inlines = [EducationInline, ExperienceInline, ProjectInline, PublicationInline]
    
    def user_full_name(self, obj):
        return obj.user.get_full_name()
    user_full_name.short_description = 'Nombre completo'
    
    def profile_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="100" height="100" style="border-radius:50%;object-fit:cover;" />', obj.photo.url)
        return "Sin foto"
    profile_photo.short_description = 'Vista previa de la foto'

# Registrar otros modelos
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    form = ExperienceForm
    list_display = ['profile', 'position', 'company', 'start_date', 'end_date']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ['profile', 'name', 'role', 'client', 'start_date']

# Registrar el resto de modelos sin formularios personalizados
admin.site.register(Education)
admin.site.register(Publication)
admin.site.register(Event)
admin.site.register(Award)
admin.site.register(Skill)
admin.site.register(Certification)