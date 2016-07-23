from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def replace_query_link(context, field, value):
    """
    Returns the querystring in which the ``field`` is overridden
    by the given ``value``
    """
    # cloning the request
    request = context['request']
    querystring = request.GET.copy()

    # field overriding; returning the encoded url
    querystring[field] = value
    return "?{}".format(querystring.urlencode())
