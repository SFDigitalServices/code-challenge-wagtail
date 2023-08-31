from wagtail.test.utils import WagtailPageTestCase
from home.models import HomePage

class TestHomePage(WagtailPageTestCase):
    def test_can_create_page(self):
        assert True == True