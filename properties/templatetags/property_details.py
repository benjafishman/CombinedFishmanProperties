from django.template.defaultfilters import stringfilter

__author__ = 'benfishman'

from django import template

register = template.Library()


@register.filter
@stringfilter
def addresser(value):
    return value.split(".")
