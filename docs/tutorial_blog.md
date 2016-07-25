# Getting started

## Get the nesting box

Install the toolkit using ``pip``:

    $ pip install wagtail-nesting-box

After that, a working Wagtail website is required. If you don't have a properly configured
website, you may follow the [official guidelines][1] to create a new one.

## Create a Wagtail blog

Wagtail is built on top of the [Django web framework][2] and it acts as a traditional Django app.
The toolkit is just a set of models already configured to work out of the box on your Wagtail
instance, so to activate them you should update the ``INSTALLED_APPS`` variable in your Django
settings. Assuming that you want to add a full fledged blog, simply:

```python
    INSTALLED_APPS = [
        'wagtail_box',
        'wagtail_box.blog',
        'wagtail.contrib.settings',

        # ...
        # all your other Wagtail, Django, and personal apps
    ]
```

**Note**: ``wagtail.contrib.settings`` is a pre-requisite for the ``wagtail_box.blog`` app.

Now you can update your database, launching a Django migration:

    $ python manage.py migrate

## Add the Blog index page

Access the Wagtail [admin site](http://127.0.0.1:8000/admin/login/).

* Add a new blog index page, clicking on **Page** > **Add child page** > **Blog**.
* In the creation page, set the page ``title``.
* In the **Promote** > **Slug** field, write ``blog``.
* Click the **Publish** button in the bottom menu, to save the page.
* Open the page by clicking the **Live** button.

If everything went well, you should see an empty page with the **Blog posts** header.

## Add your first Post

In the Wagtail admin site, add a subpage to the Blog page:

* Choose the **Post** page
* In the creation page, set the page ``title``.
* Write the post content in the ``body`` field, throught the Wagtail ``StreamField`` widget.
* Add at least one Tag
* Click the **Publish** button in the bottom menu, to save the page.
* Open the Blog page index again

At that point, you must see your first blog post with a tag filter at the top of the page! If you
click on the title, on the image or on the ``Read more`` link, you can access to the post detail.
Now it's the time to add more posts and try the tag filter above.

**Note**: the Post page is available only as a child of the Blog page. If you don't see the Post page,
it's because you're not adding a child to the Blog page (or because [you found a bug!][3]).

## Write your custom templates

Offered templates are simple and without any kind of style. If you want to write your custom ``Blog``
and ``Post`` templates, it's enough to add these files in your Wagtail root folder:

* ``templates/blog/blog.html``: defines the blog index page
* ``templates/blog/post.html``: defines the post detail

It could be a good idea copying the [provided templates][4] so that you can be inspired while writing
basic functionalities such as tag filtering.

[1]: http://docs.wagtail.io/en/latest/getting_started/index.html
[2]: https://www.djangoproject.com/
[3]: https://github.com/palazzem/wagtail-nesting-box/issues
[4]: https://github.com/palazzem/wagtail-nesting-box/tree/master/wagtail_box/blog/templates/blog
