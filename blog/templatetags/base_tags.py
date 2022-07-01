from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag('blog/partial/category_navbar.html')
def category_navbar():
    return {
        'categories' : Category.objects.active,
    }