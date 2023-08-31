from wagtail.test.utils import WagtailPageTestCase
# from home.models import HomePage

class TestHomePage(WagtailPageTestCase):
    def test_success(self):
        assert True == True

    def test_fail(self):
        assert True == False