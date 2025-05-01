from django import template

register = template.Library()

@register.filter(name='replace')
def replace(value, arg):
    """Replaces all instances of arg in value with empty string"""
    return value.replace(arg, '')