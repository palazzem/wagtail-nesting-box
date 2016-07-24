import pytest

from model_mommy import mommy

from wagtail_box.blog.models import BlogSettings

from .utils import get_root_page, link_page, add_site_to_request


@pytest.mark.django_db
def test_blog_index_context(rf):
    """
    Alice is a user that wants to read our blog. She opens the
    /blog/ webpage and expects to find two new posts.
        - the Blog page contains two posts
        - Alice navigates to /blog/ page
        - Alice expects to see two posts
    """
    # create a blog page with two posts
    root_page = get_root_page()
    blog = mommy.prepare_recipe('tests.recipes.blog')
    posts = mommy.prepare_recipe('tests.recipes.post', _quantity=2)
    link_page(root_page, blog)
    link_page(blog, posts)
    # create a fake request
    request = add_site_to_request(rf.get(blog.slug))
    context = blog.get_context(request)
    assert len(context['articles']) == 2
    assert context['current_tag'] is None


@pytest.mark.django_db
def test_blog_tag_filter(rf):
    """
    Alice is a user that wants to read our blog. She opens the
    /blog/ webpage and choose a particular tag filter.
    She expects to find only a subset of posts, according to
    the chosen tag.
        - the Blog page contains three posts
        - two posts shares one tag while the other one has
          a different tag
        - Alice navigates to /blog/ page choosing the common tag
        - Alice expects to see two posts
    """
    # create a blog page with three posts
    root_page = get_root_page()
    blog = mommy.prepare_recipe('tests.recipes.blog')
    posts = mommy.prepare_recipe('tests.recipes.post', _quantity=3)
    link_page(root_page, blog)
    link_page(blog, posts)
    # append the proper tags
    tag_1 = mommy.make('blog.PostTag', content_object=posts[0]).tag
    tag_2 = mommy.make('blog.PostTag', content_object=posts[1]).tag
    # the third post is tagged with tag_1
    mommy.make('blog.PostTag', tag=tag_1, content_object=posts[2])
    # create a fake request with a tag attribute
    request = add_site_to_request(rf.get(blog.slug, {'tag': tag_1.name}))
    context = blog.get_context(request)
    assert len(context['articles']) == 2
    assert context['current_tag'] == tag_1.name


@pytest.mark.django_db
def test_blog_pagination_default(rf, site):
    """
    Alice is a user that wants to read our blog. She opens the
    /blog/ webpage and the default pagination is set to 5.
    Because of that, Alice sees 2 paginator pages with five
    article for each page.
        - the Blog page contains ten posts
        - Alice navigates to /blog/ page
        - Alice expects five post
        - Alice should change the current page to see remaining
          posts
    """
    # create a blog page with ten posts
    root_page = get_root_page()
    blog = mommy.prepare_recipe('tests.recipes.blog')
    posts = mommy.prepare_recipe('tests.recipes.post', _quantity=10)
    link_page(root_page, blog)
    link_page(blog, posts)
    # create a fake request for the main page
    request = add_site_to_request(rf.get(blog.slug))
    context = blog.get_context(request)
    assert len(context['articles']) == 5
    assert posts[0] in context['articles']
    assert posts[1] in context['articles']
    assert posts[2] in context['articles']
    assert posts[3] in context['articles']
    assert posts[4] in context['articles']
    # create a fake request for the second page
    request = add_site_to_request(rf.get(blog.slug, {'page': 2}))
    context = blog.get_context(request)
    assert len(context['articles']) == 5
    assert posts[5] in context['articles']
    assert posts[6] in context['articles']
    assert posts[7] in context['articles']
    assert posts[8] in context['articles']
    assert posts[9] in context['articles']


@pytest.mark.django_db
def test_blog_pagination(rf, site):
    """
    Alice is a user that wants to read our blog. She opens the
    /blog/ webpage, but the administrator has set the pagination
    to one. Because of that, Alice sees 3 paginator pages with one
    article for each page.
        - the ``BlogSettings`` pagination is set to one post for
          each page
        - the Blog page contains three posts
        - Alice navigates to /blog/ page
        - Alice expects one post
        - Alice should change the current page to see other posts
    """
    # update BlogSettings
    BlogSettings.objects.create(
        site=site,
        page_number=1
    )
    # create a blog page with two posts
    root_page = get_root_page()
    blog = mommy.prepare_recipe('tests.recipes.blog')
    posts = mommy.prepare_recipe('tests.recipes.post', _quantity=3)
    link_page(root_page, blog)
    link_page(blog, posts)
    # create a fake request for the main page
    request = add_site_to_request(rf.get(blog.slug))
    context = blog.get_context(request)
    assert len(context['articles']) == 1
    assert posts[0] in context['articles']
    # create a fake request for the second page
    request = add_site_to_request(rf.get(blog.slug, {'page': 2}))
    context = blog.get_context(request)
    assert len(context['articles']) == 1
    assert posts[1] in context['articles']
    # create a fake request for the first page
    request = add_site_to_request(rf.get(blog.slug, {'page': 3}))
    context = blog.get_context(request)
    assert len(context['articles']) == 1
    assert posts[2] in context['articles']
