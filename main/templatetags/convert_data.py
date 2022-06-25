import json
from django import template

register = template.Library()


@register.filter
def to_json(value):
    return json.dumps(value)


@register.filter
def qset_to_json(value):
    val_arr = [data for data in value.values()]
    # print(json.dumps(val_arr))
    return json.dumps(val_arr)
