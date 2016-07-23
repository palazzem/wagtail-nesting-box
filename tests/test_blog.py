import pytest

from datetime import datetime

from model_mommy import mommy

from .utils import get_root_page, link_page


@pytest.mark.django_db
def test_blog_articles():
    """
    Test the Blog model so that users may retrieve all published
    articles.
        - the Blog page is a child of the root page
        - the Blog page contains two posts
        - blog.articles must return two (live) posts
    """
    # create a blog post with two posts
    root_page = get_root_page()
    blog = mommy.prepare_recipe('tests.recipes.blog')
    posts = mommy.prepare_recipe('tests.recipes.post', _quantity=2)
    link_page(root_page, blog)
    link_page(blog, posts)

    assert len(blog.articles) == 2

@pytest.mark.django_db
def test_blog_articles_order():
    """
    Test the Blog model so that users may retrieve all published
    articles ordered by date (newest first).
        - the Blog page is a child of the root page
        - the Blog page contains two posts
        - post_1 is an old post, post_2 is a new post
        - blog.articles must return [post_2, post_1]
    """
    # create a blog post with two posts
    root_page = get_root_page()
    blog = mommy.prepare_recipe('tests.recipes.blog')
    link_page(root_page, blog)
    post_1 = mommy.prepare_recipe('tests.recipes.post', date=datetime(2000, 1, 1))
    link_page(blog, post_1)
    post_2 = mommy.prepare_recipe('tests.recipes.post', date=datetime(2000, 1, 2))
    link_page(blog, post_2)

    assert blog.articles[0] == post_2
    assert blog.articles[1] == post_1

@pytest.mark.django_db
def test_blog_articles_only_live():
    """
    Test the Blog model so that users may retrieve all published
    articles, while not published articles are hidden to users.
        - the Blog page is a child of the root page
        - the Blog page contains two posts
        - post_1 is published, post_2 is not published
        - blog.articles must return [post_1]
    """
    # create a blog post with two posts
    root_page = get_root_page()
    blog = mommy.prepare_recipe('tests.recipes.blog')
    link_page(root_page, blog)
    post_1 = mommy.prepare_recipe('tests.recipes.post')
    link_page(blog, post_1)
    post_2 = mommy.prepare_recipe('tests.recipes.post', live=False)
    link_page(blog, post_2)

    assert post_1 in blog.articles
    assert post_2 not in blog.articles

@pytest.mark.django_db
def test_blog_exposes_empty_tags_as_default():
    """
    The Blog model can retrieve a list of all available tags.
    By default, a Post doesn't have a Tag.
        - the Blog page is a child of the root page
        - the Blog page contains a post
        - blog.tags must return an empty list
    """
    # create a blog post with two posts
    root_page = get_root_page()
    blog = mommy.prepare_recipe('tests.recipes.blog')
    post = mommy.prepare_recipe('tests.recipes.post')
    link_page(root_page, blog)
    link_page(blog, post)

    assert len(blog.tags) == 0

@pytest.mark.django_db
def test_blog_exposes_articles_tags():
    """
    The Blog model can retrieve a list of all available tags.
        - the Blog page is a child of the root page
        - the Blog page contains a post
        - the Post has two Tag
        - blog.tags must return two tags
    """
    # create a blog page with a post
    root_page = get_root_page()
    blog = mommy.prepare_recipe('tests.recipes.blog')
    post = mommy.prepare_recipe('tests.recipes.post')
    link_page(root_page, blog)
    link_page(blog, post)
    # append two tags to the post
    tag_1 = mommy.make('blog.PostTag', content_object=post).tag
    tag_2 = mommy.make('blog.PostTag', content_object=post).tag

    assert len(blog.tags) == 2
    assert tag_1 in blog.tags
    assert tag_2 in blog.tags

@pytest.mark.django_db
def test_blog_exposes_articles_tags_are_order():
    """
    The Blog model can retrieve a list of all available tags.
    The list of tags is ordered according to the usage so that
    more used tags are listed first.
        - the Blog page is a child of the root page
        - the Blog page contains two posts
        - post_1 has two tags, post_2 has one tags
        - a tag is used twice while the other only once
        - blog.tags must return two tags; the first one should be
          the most common
    """
    # create a blog page with two posts
    root_page = get_root_page()
    blog = mommy.prepare_recipe('tests.recipes.blog')
    posts = mommy.prepare_recipe('tests.recipes.post', _quantity=2)
    link_page(root_page, blog)
    link_page(blog, posts)
    # append two tags to two different posts
    tag_1 = mommy.make('blog.PostTag', content_object=posts[0]).tag
    tag_2 = mommy.make('blog.PostTag', content_object=posts[1]).tag
    # one tag is used twice
    mommy.make('blog.PostTag', tag=tag_2, content_object=posts[0])

    assert len(blog.tags) == 2
    assert blog.tags[0] == tag_2
    assert blog.tags[1] == tag_1
