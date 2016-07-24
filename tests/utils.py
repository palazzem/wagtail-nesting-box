from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.middleware import SiteMiddleware


def get_root_page():
    """
    Returns the root page of the Wagtail website. This
    page may be useful if you need to attach newly generated
    pages to the website. Unless a developer delete all pages,
    'root' is the Wagtail root page's slug.
    """
    return Page.objects.get(slug='root')


def link_page(parent, items):
    """
    Sets one or more items as parent children. This helper
    may be useful when you generate a lot of instances and
    you want to add all items at once.
    """
    try:
        for child in items:
            # items is an iterable so we add all items
            # as children
            parent.add_child(instance=child)
    except TypeError:
        # we don't have an iterable so we add just
        # this item
        parent.add_child(instance=items)


def add_site_to_request(request):
    """
    For the given ``RequestFactory`` object, use the Wagtail
    ``SiteMiddleware`` to add the ``Site`` object to the request.
    This is helpful if you don't want to use the ``Client``
    object to access to a view's context.
    """
    middleware = SiteMiddleware()
    middleware.process_request(request)
    return request
