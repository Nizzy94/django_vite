import json
from django import template

register = template.Library()


@register.filter
def to_json(value):
    return json.dumps(value)


@register.filter
def qset_to_json(value):
    val_arr = [data for data in value]
    # print(val_arr)
    # print(value)
    # print(list(value))
    # val_arr = list(value.values())
    return json.dumps(val_arr)
