===================
Wagtail nesting box
===================

.. image:: https://travis-ci.org/palazzem/wagtail-nesting-box.svg?branch=master
    :target: https://travis-ci.org/palazzem/wagtail-nesting-box

.. image:: https://codecov.io/gh/palazzem/wagtail-nesting-box/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/palazzem/wagtail-nesting-box

.. image:: https://readthedocs.org/projects/wagtail-nesting-box/badge/?version=latest
    :target: http://wagtail-nesting-box.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

A set of abstract and concrete models for your `Wagtail`_ website.

.. _Wagtail: https://wagtail.io/

Support
-------

If you need support, please use the `GitHub issue tracker`_.

.. _GitHub issue tracker: https://github.com/palazzem/wagtail-nesting-box/issues

Contributing
------------

We love contributions, so please feel free to fix bugs, improve things, provide documentation.
Just follow the guidelines and submit a PR.

Requirements
------------

* Python 2.7, 3.3, 3.4 and 3.5
* Django 1.8, 1.9 (only with Python 2.7 and 3.4+)
* Wagtail 1.4, 1.5

Overview
--------

Wagtail nesting box is a powerful and flexible toolkit that helps you to build your Wagtail
websites. Out of the box without extending any model, it provides:

* Static web pages: you can create a static page to write, for instance, your *About us* page.
* A full fledged blog: it includes an index page that provides pagination and tag filtering (based
  on tags usage).
* Streamfields as default: both static and post pages, use the Wagtail ``StreamField`` to
  write the text body.
* Template free: the package includes a set of demo template that you can copy to implement your
  own styles.
* Flexibility: the toolkit provides a set of models, templates and generic functions. If you need
  a slightly different behavior, you can simply extend our models.

Getting started
---------------

The best way to get started with this project, is following one of our tutorials:

* `Tutorial: create a blog`_
* `Tutorial: create a static page`_ (i.e. *About us* page)

.. _Tutorial\: create a blog: http://wagtail-nesting-box.readthedocs.io/en/latest/tutorial_blog/
.. _Tutorial\: create a static page: http://wagtail-nesting-box.readthedocs.io/en/latest/tutorial_static_page/

Documentation
-------------

Full documentation for the project is available at http://wagtail-nesting-box.readthedocs.io/

License
-------

wagtail-nesting-box is released under the terms of the **BSD license**. Full details in ``LICENSE`` file.
