import allure
import pytest
from Common.init_page import InitPage


class TestRoom:
    def setup_class(self):
        self.driver = InitPage()
        self.room = self.driver.goto_home().goto_room()

    def teardown(self):
        self.room.is_room_page()

    def teardown_class(self):
        self.room.back_home_page()

    @pytest.mark.parametrize("name,expect_name", [("Ayla45", "Ayla45"),
                                                  # ("Ayla 45", "Ayla 45"),
                                                  # ("Ayla_45", "Ayla_45"),
                                                  # ("Ayla45Ayla45Ayla45123", "Ayla45Ayla45Ayla4512"),
                                                  ("艾拉-45", "艾拉-45")])
    @allure.description("成功创建房间")
    def test_create_room(self, name, expect_name):
        before_total = self.room.get_room_length()
        self.room.allure_screenshot(story="创建前截图")
        self.room.create_room(name).back_list()
        after_total = self.room.get_room_length()
        self.room.allure_screenshot(story="创建后截图")
        assert expect_name in self.room.get_page_source(), "创建房间失败!!!"
        assert before_total < after_total, "创建房间失败!!!"

    @pytest.mark.parametrize("room_num,device_list", [(0, (3, 1)),
                                                      (1, 1),
                                                      (1, (2, 1))])
    def test_add_device(self, room_num, device_list):
        temp = self.driver.get_obj_num(device_list)
        name = self.room.choose_room(room_num).get_room_name()
        length = int(self.room.get_device_length())
        self.room.add_device(device_list).back_list()
        actual_num = self.room.get_device_num(name)
        expect_num = str(length + temp)
        self.room.logger.info("房间名称:" + name + ";预期设备个数:" + expect_num + ";实际设备个数:" + actual_num)
        assert expect_num in actual_num, "添加设备失败;预期个数:%s  实际个数:%s" % (expect_num, actual_num)

    @pytest.mark.parametrize("room_num,device_list", [(0, (3, 1)),
                                                      (1, 1),
                                                      (1, (2, 1))])
    def test_delete_device(self, room_num, device_list):
        temp = self.driver.get_obj_num(device_list)
        name = self.room.choose_room(room_num).get_room_name()
        length = int(self.room.get_device_length())
        self.room.delete_device(device_list).back_list()
        actual_num = self.room.get_device_num(name)
        expect_num = str(length - temp)
        self.room.logger.info("房间名称:" + name + ";预期设备个数:" + expect_num + ";实际设备个数:" + actual_num)
        assert expect_num in actual_num, "删除设备失败;预期个数:%s  实际个数:%s" % (expect_num, actual_num)

    # @pytest.mark.parametrize("room_num,device_list", [(1, [1]),
    #                                                   (0, [3, 1])
    #                                                   ])
    # def test_delete_device1(self, room_num, device_list):
    #     temp = self.driver.get_obj_num(device_list)
    #     name = self.room.choose_room(room_num).get_room_name()
    #     length = int(self.room.get_device_length())
    #     self.room.delete_device(device_list).back_list()
    #     actual_num = self.room.get_device_num(name)
    #     expect_num = str(length - temp)
    #     self.room.logger.info("房间名称:" + name + ";预期设备个数:" + expect_num + ";实际设备个数:" + actual_num)
    #     assert expect_num in actual_num, "删除设备失败;预期个数:%s  实际个数:%s" % (expect_num, actual_num)

    def test_modify_name(self, room_num=1, name='9999999'):
        self.room.choose_room(room_num).modify_room_name(name)
        # toast = self.room.get_toast()
        self.room.back_list()
        # assert "保存成功" in toast, "修改成功的toast有问题"
        assert name in self.room.get_page_source(), "修改名字失败"

    @pytest.mark.parametrize("num,", [1, 0])
    def test_delete_room(self, num):
        before_total = self.room.get_room_length()
        self.room.delete_room(num)
        after_total = self.room.get_room_length()
        assert before_total > after_total, "删除房间失败!!!"
