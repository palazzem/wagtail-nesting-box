from django.template import Template, Context


def test_blog_replace_query_link(rf):
    """
    Ensures that the replace_query_link clones the request query string, and
    updates a value with the given argument. The returned value must be URL
    encoded.
        - a template makes use of the replace_query_link templatetag
        - the request doesn't include any parameter
        - the resulting template must include a link with a 'page' parameter
    """
    # the fake template
    TEMPLATE = Template(
        """
        {% load blog_tags %}
        <a href="/blog/{% replace_query_link 'page' 1 %}">Link</a>
        """
    )
    # template rendering with an empty Context
    request = rf.get('/blog/')
    rendered = TEMPLATE.render(Context({'request': request}))
    # the result must have a different link
    assert '/blog/?page=1' in rendered


def test_blog_replace_query_link_with_parameter(rf):
    """
    Ensures that the replace_query_link clones the request query string, and
    updates a value with the given argument. The returned value must be URL
    encoded.
        - a template makes use of the replace_query_link templatetag
        - the request includes a 'page' parameter that should be replaced
        - the resulting template must include a link with a 'page' parameter
    """
    # the fake template
    TEMPLATE = Template(
        """
        {% load blog_tags %}
        <a href="/blog/{% replace_query_link 'page' 2 %}">Link</a>
        """
    )
    # template rendering with an empty Context
    request = rf.get('/blog/', {'page': 1})
    rendered = TEMPLATE.render(Context({'request': request}))
    # the result must have a different link
    assert '/blog/?page=1' not in rendered
    assert '/blog/?page=2' in rendered
