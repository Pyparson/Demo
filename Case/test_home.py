import pytest

from Common.init_page import InitPage


class TestHome:
    def setup_class(self):
        self.driver = InitPage()
        self.home = self.driver.goto_home()

    def teardown(self):
        self.home.is_home_page()

    def teardown_class(self):
        self.driver.is_home_page()

    @pytest.mark.parametrize("name,expect_name", [("Ayla45", "Ayla45"),
                                                  ("Ayla 45", "Ayla 45"),
                                                  ("Ayla_45", "Ayla_45"),
                                                  ("Ayla45Ayla45Ayla45123", "Ayla45Ayla45Ayla4512"),
                                                   ("艾拉-45", "艾拉-45")])
    def test_modify_title(self, name, expect_name):
        # self.name = self.home.modify_title(name)
        self.home.modify_title(name)
        actual_name = self.home.get_home_name()
        assert expect_name == actual_name, "测试不通过"

    # todo
    def test_modify_title_fail(self):
        self.home.modify_title_fail()
        print(self.home.get_page_source())
        text = self.home.get_toast()
        assert "输入内容为空" in text,"测试不通过"

