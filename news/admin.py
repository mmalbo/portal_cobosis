from django.contrib import admin
from .models import Curio, Event, Comment

class CurioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class EventAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
   # readonly_fields = ('created_date', 'updated')
   pass

admin.site.register(Curio, CurioAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Comment, CommentAdmin)