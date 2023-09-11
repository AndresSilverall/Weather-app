from django import template


register = template.Library()

#filtrar los valores del diccionario en el template
@register.filter
def get_value(dictionay, value):
    return dictionay.get[value]