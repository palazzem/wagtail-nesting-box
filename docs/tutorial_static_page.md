# Getting started

## Get the nesting box

Install the toolkit using ``pip``:

    $ pip install wagtail-nesting-box

After that, a working Wagtail website is required. If you don't have a properly configured
website, you may follow the [official guidelines][1] to create a new one.

## Create a static page

Wagtail is built on top of the [Django web framework][2] and it acts as a traditional Django app.
The toolkit is just a set of models already configured to work out of the box on your Wagtail
instance, so to activate them you should update the ``INSTALLED_APPS`` variable in your Django
settings. Assuming that you want to add a simple static page for your *About us* page, just:

```python
    INSTALLED_APPS = [
        'wagtail_box',
        'wagtail_box.pages',

        # ...
        # all your other Wagtail, Django, and personal apps
    ]
```

Now you can update your database, launching a Django migration:

    $ python manage.py migrate

## Add the About us page

Access the Wagtail [admin site](http://127.0.0.1:8000/admin/login/).

* Add a new blog index page, clicking on **Page** > **Add child page** > **Static page**.
* In the creation page, write *About us* in the ``title`` field
* Fill the content of the page in the ``body`` field, through the Wagtail ``StreamField`` widget.
* Click the **Publish** button in the bottom menu, to save the page.
* Open the page by clicking the **Live** button.

If everything went well, you must see the new *About us* page.

## Write your custom template

The template is simple and without any kind of style. If you want to write your custom ``StaticPage``
template, it's enough to add this file in your Wagtail root folder:

* ``templates/pages/static_page.html``: defines the static page template

It could be a good idea copying the [provided template][3] so that you can be inspired while writing
basic functionalities such as how include the ``StreamField`` content.

[1]: http://docs.wagtail.io/en/latest/getting_started/index.html
[2]: https://www.djangoproject.com/
[3]: https://github.com/palazzem/wagtail-nesting-box/tree/master/wagtail_box/pages/templates/pages
