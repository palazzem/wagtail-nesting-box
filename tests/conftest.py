import pytest


@pytest.fixture
def site():
    """
    Returns the Wagtail test Site, as provided in the
    Django configuration settings
    """
    from django.conf import settings
    from wagtail.wagtailcore.models import Site

    return Site.objects.get(id=settings.SITE_ID)


def pytest_configure():
    """
    Settings configuration for the Django web framework. Update this
    configuration if you need to change the default behavior of
    Django during tests
    """
    from django.conf import settings

    settings.configure(
        DEBUG_PROPAGATE_EXCEPTIONS=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:'
            }
        },
        SITE_ID=1,
        SECRET_KEY='not_very_secret_in_tests',
        WAGTAIL_SITE_NAME = 'test-site',
        USE_I18N=True,
        USE_L10N=True,
        STATIC_URL='/static/',
        ROOT_URLCONF='tests.urls',
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ],
        MIDDLEWARE_CLASSES=(
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
            'django.middleware.security.SecurityMiddleware',

            'wagtail.wagtailcore.middleware.SiteMiddleware',
            'wagtail.wagtailredirects.middleware.RedirectMiddleware',
        ),
        INSTALLED_APPS=(
            'wagtail_box',
            'wagtail_box.blog',
            'wagtail_box.pages',

            'wagtail.contrib.settings',
            'wagtail.wagtailforms',
            'wagtail.wagtailredirects',
            'wagtail.wagtailembeds',
            'wagtail.wagtailsites',
            'wagtail.wagtailusers',
            'wagtail.wagtailsnippets',
            'wagtail.wagtaildocs',
            'wagtail.wagtailimages',
            'wagtail.wagtailsearch',
            'wagtail.wagtailadmin',
            'wagtail.wagtailcore',

            'modelcluster',
            'taggit',

            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        ),
    )

    try:
        import django
        django.setup()
    except AttributeError:
        pass
