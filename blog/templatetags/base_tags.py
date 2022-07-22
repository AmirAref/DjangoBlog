from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag('blog/partials/category_navbar.html')
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

@register.inclusion_tag('registration/partials/errors_field.html')
def field_errors(errors):
    return {'errors' : errors}