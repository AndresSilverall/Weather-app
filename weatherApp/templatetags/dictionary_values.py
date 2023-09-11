from django import template


register = template.Library()

#filtrar los valores del diccionario en el template
@register.filter('get_value')
def get_value(dictionay, key):
    return dictionay.get(key)