# Wagtail nesting box

A set of abstract and concrete models for your [Wagtail][1] website.

## Support

If you need support, please use the [GitHub issue tracker][2].

## Contributing

We love contributions, so please feel free to fix bugs, improve things, provide documentation.
Just follow the guidelines and submit a PR.

## Requirements

* Python 2.7, 3.3, 3.4 and 3.5
* Django 1.8, 1.9 and 1.10 (only with Python 2.7 and 3.4+)
* Wagtail 1.5 and 1.6 (required by Django 1.10+)

## Overview

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

## License

wagtail-nesting-box is released under the terms of the **BSD license**. Full details in ``LICENSE`` file.

[1]: https://wagtail.io/
[2]: https://github.com/palazzem/wagtail-nesting-box/issues
