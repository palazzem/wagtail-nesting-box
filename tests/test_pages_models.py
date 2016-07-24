from wagtail.wagtailcore.models import Page
from wagtail.tests.utils import WagtailPageTests

from wagtail_box.pages.models import StaticPage


class PagesModelTest(WagtailPageTests):
    def test_static_page_child_of_anything(self):
        """
        Ensures that a Static page can be child of any kind of Page
        """
        self.assertCanCreateAt(Page, StaticPage)
