from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag('blog/partial/category_navbar.html')
def category_navbar():
    return {
        'categories' : Category.objects.active,
    }

@register.simple_tag
def activate(request, url_name):
    # check the request url
    if request.resolver_match.url_name == url_name:
        return 'active'
    return ''