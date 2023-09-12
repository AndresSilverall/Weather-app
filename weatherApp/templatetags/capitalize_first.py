from django import template

register= template.Library()


@register.simple_tag
def first_letter_to_uppercase(string):
    return string.capitalize()