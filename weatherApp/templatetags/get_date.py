from django import template
import datetime


register = template.Library()


@register.simple_tag
def get_date():
    return str(datetime.datetime.now().date())