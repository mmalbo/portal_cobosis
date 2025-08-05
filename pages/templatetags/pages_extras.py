from django import template
from pages.models import Paginas

register = template.Library()

@register.simple_tag
def get_page_list():
    pages = Paginas.objects.all()
    return pages

