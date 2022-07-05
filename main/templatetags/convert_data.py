import json
from django import template

register = template.Library()


@register.filter
def to_json(value):
    return json.dumps(value)


@register.filter
def qset_to_json(value):
    # print(value)
    val_arr = list(value.values())
    return json.dumps(val_arr)
