from Common.init_page import InitPage


class TestSmart:
    def setup(self):
        self.driver = InitPage()

    def test_smart(self):
        self.driver.goto_smart()
