import markdown
from django import template
from django.utils.safestring import mark_safe
from markdown.extensions.extra import extensions

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def mark(value):
    return mark_safe(markdown.markdown(value,extensions=extensions))