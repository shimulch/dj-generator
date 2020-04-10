from django import template
register = template.Library()


def _build_tag_str(*args, **kwargs):
    result = None
    if len(args) > 0:
        result = ' '.join(args)

    if len(kwargs) > 0:
        kwargs_str = ' '.join([f'{key}={val}' for key, val in kwargs.items()])
        if result:
            return f'{result} {kwargs_str}'
        else:
            return kwargs_str
    return result


@register.simple_tag
def print_tag(*args, **kwargs):
    return "{{ %s }}" % _build_tag_str(*args, **kwargs)


@register.simple_tag
def eval_tag(*args, **kwargs):
    return "{%% %s %%}" % _build_tag_str(*args, **kwargs)
