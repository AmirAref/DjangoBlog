from django import template
from django.db.models import Count, Q
from datetime import datetime, timedelta

from ..models import Category, Post

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


@register.inclusion_tag('blog/partials/popular_posts.html')
def popular_posts():
    # return the posts of the last month sort by views count
    last_month = datetime.today() - timedelta(days=30)
    return {
        'popular_posts' : Post.objects.published().annotate(
            count=Count(
                'hits', # add new 'count' field 
                filter=Q(posthit__created__gt=last_month), # filter only posts that their created view time greater than last month
            )).order_by('-count', '-publish')[:5] # sort the posts by their views and then by the publish time
        }