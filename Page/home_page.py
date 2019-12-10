from time import sleep
from selenium.webdriver.common.by import By
from Common.base_page import BasePage
from Page.room_page import RoomPage


class HomePage(BasePage):
    _home_name = (By.ID, "tv_appName")
    _title = (By.ID, "et_homename")
    _home_save = (By.ID, "tv_right")
    _toast = (By.XPATH, "//*[@class='android.widget.Toast']")
    _room = (By.ID, "add_group_iv")

    def modify_title(self, name):
        self.find_element_until_visibility(self._home_name).click()
        self.find_element_until_visibility(self._title).clear()
        self.find_element_until_visibility(self._title).send_keys(name)
        # self.hide_keyboard()
        self.find_element_until_visibility(self._home_save).click()
        return self

    def modify_title_fail(self):
        print(self.find_element_until_visibility(self._home_name).rect)
        self.find_element_until_visibility(self._home_name).click()
        self.find_element_until_visibility(self._title).clear()
        self.find_element_until_visibility(self._home_save).click()
        return self

    def get_home_name(self):
        text = self.find_element_until_visibility(self._home_name).text
        return text

    def is_home_page(self):
        while 1:
            sleep(1)
            flag = self.is_element(self._home_name, timeout=3)
            if flag:
                break
            else:
                self.click_device_btn(4)

    # def get_toast(self):
    #     return self.find(self._toast).text

    def goto_room(self):
        self.find_element_until_visibility(self._room).click()
        return RoomPage(self.driver)
