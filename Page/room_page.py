from time import sleep
from Common.base_page import BasePage
from selenium.webdriver.common.by import By


class RoomPage(BasePage):
    _create_btn = (By.ID, "add_onekey")
    _room_name = (By.ID, "name_et")
    _group_name = (By.ID, "group_name")
    _save_btn = (By.ID, "tv_right")
    _room_list = (By.ID, "esml")
    _add_btn = (By.ID, "add_iv")
    _back_btn = (By.ID, "iv_left")
    _delete_btn = (By.ID, "delete")
    _sure_btn = (By.ID, "button1")
    _device_list = (By.ID, "esml")
    _room_title = (By.XPATH, "//*[contains(@text,'房间管理')]")
    _title = (By.ID, "tv_title")
    _toast = (By.XPATH, "//*[@class='android.widget.Toast']")

    def get_toast(self):
        # 获取toast
        # return self.find_element_until_visibility(self._toast).text
        return self.find_element(self._toast).text

    def create_room(self, name):
        """
        创建房间组
        :param name: 房间名称
        :return:
        """
        self.find_element_until_visibility(self._create_btn).click()
        self.find_element_until_visibility(self._room_name).send_keys(name)
        self.logger.info(name)
        # self.hide_keyboard()
        self.find_element_until_visibility(self._save_btn).click()
        return self

    def delete_room(self, room_num=0):
        """
        删除房间组,默认删除第一个
        :param room_num: 房间序列
        :return:
        """
        room = self.find_elements_until_visibility(self._room_list)
        self.swipe_ele_left(room[room_num])
        self.find_element_until_visibility(self._delete_btn).click()
        self.find_element_until_visibility(self._sure_btn).click()
        return self

    def get_room_length(self):
        """
        获取房间个数
        :return:
        """
        room = self.find_elements_until_visibility(self._room_list)
        return len(room)

    def choose_room(self, room_num=0):
        """
        选择房间,默认选第一个
        :param room_num: 房间组序列
        :return:
        """
        room = self.find_elements_until_visibility(self._room_list)
        room[room_num].click()
        return self

    def get_room_name(self):
        """获取所选房间的名字"""
        name = self.find_element_until_visibility(self._group_name).text
        return name

    def back_list(self):
        """
        返回房间列表
        :return:
        """
        self.find_element_until_visibility(self._back_btn).click()
        sleep(1)
        return self

    def get_device_num(self, room):
        """
        获取房间列表中指定房间的设备个数,房间名称从get_room_name获取,用于校验添加设备和删除设备
        :param room: 指定房间的名称
        :return:
        """
        room = (By.XPATH, '//*[contains(@text,"{room}")]/..//*[contains(@resource-id,"tv_count")]'.format(room=room))
        num = self.find_element_until_visibility(room).text
        return num

    def add_device(self, device_num=0):
        """
        往房间组里添加设备,默认往房间组添加第一个设备
        :param device_num:设备序列,元祖传参默认只添加一个,添加多个时建议大的数字往前放
        :return:
        """
        device = self.find_elements_until_visibility(self._add_btn)
        if "int" in str(type(device_num)):
            device[device_num].click()
        else:
            for i in device_num:
                device[i].click()
        return self

    # def delete_device(self, device_num=(0)):
    #     """
    #     删除房间里的设备,默认删除房间的第一个设备
    #     :param device_num: 设备序列,默认删除第一个,删除多个时建议大的数字往前放
    #     :return:
    #     """
    #     device = self.find_elements_until_visibility(self._device_list)
    #     if "int" in str(type(device_num)):
    #         self.swipe_ele_left(device[device_num])
    #         self.find_element_until_visibility(self._delete_btn).click()
    #     else:
    #         for i in device_num:
    #             self.swipe_ele_left(device[i])
    #             self.find_element_until_visibility(self._delete_btn).click()
    #     return self

    def delete_device(self, device_num : list=[0]):
        """
        删除房间里的设备,默认删除房间的第一个设备
        :param device_num: 设备序列(必须是列表列表),默认删除第一个,删除多个时建议大的数字往前放
        :return:
        """
        device = self.find_elements_until_visibility(self._device_list)
        for i in device_num:
            self.swipe_ele_left(device[i])
            self.find_element_until_visibility(self._delete_btn).click()
        return self

    def get_device_length(self):
        """
        获取房间组设备个数
        :return: 
        """
        device = self.count_elements(self._device_list)
        return len(device)

    def modify_room_name(self, name):
        """
        修改房间组的名字
        :param name: 修改的名字
        :return:
        """
        self.find_element_until_visibility(self._group_name).send_keys(name)
        self.find_element_until_visibility(self._title).click()
        # self.hide_keyboard()
        # self.find_element_until_visibility(self._save_btn).click()
        return self

    def is_room_page(self):
        """用于判断当前页面是否在房间列表"""
        while 1:
            sleep(1)
            flag = self.is_element(self._room_title, timeout=3)
            if flag:
                break
            else:
                self.click_device_btn(4)

    def back_home_page(self):
        """返回Home页面"""
        self.find_element_until_visibility(self._back_btn).click()
        from Page.home_page import HomePage
        return HomePage(self.driver)
