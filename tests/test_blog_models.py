from wagtail.wagtailcore.models import Page
from wagtail.tests.utils import WagtailPageTests

from wagtail_box.blog.models import Blog, Post


class BlogModelTest(WagtailPageTests):
    def test_blog_child_of_anything(self):
        """
        Ensures that the Blog page can be child of any kind of Page
        """
        self.assertCanCreateAt(Page, Blog)

    def test_post_child_of_blog(self):
        """
        Ensures that a Post page can be a child of Blog
        """
        self.assertCanCreateAt(Blog, Post)

    def test_post_cannot_be_child_of_anything(self):
        """
        Ensures that a Post page cannot be a child of a generic page
        """
        self.assertCanNotCreateAt(Page, Post)

    def test_post_cannot_have_children(self):
        """
        Ensures that a Post page cannot have any kind of children
        """
        self.assertCanNotCreateAt(Post, Page)
