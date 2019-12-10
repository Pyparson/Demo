import logging
import os
from time import sleep

import allure
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    # black_list = [
    #     (By.ID, 'image_cancel'),
    # ]
    logging.basicConfig(level=logging.INFO, format='%(asctime)s  -  %(message)s')

    logger = logging.getLogger(__name__)

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element_until_visibility(self, locator, timeout=10) -> WebElement:
        # 在规定时间内找某控件,eg:find_element_until_visibility(("By.XPATH",".//*[contains(@text,'XXX')"))
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            # ele = WebDriverWait(self.driver, timeout).until(EC.visibility_of_any_elements_located((By.ID, locator)))
            return ele
        except NoSuchElementException:
            print("Retrying to find element by %s: %s" % (locator[0], locator[1]))
        raise NoSuchElementException

    def is_element(self, locator, timeout=10):
        # 判断当前页面包含某元素,有返回True,无返回FALSE
        Flag = None
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            Flag = True
        except NoSuchElementException:
            print("Retrying to find element by %s: %s" % (locator[0], locator[1]))
            Flag = False
        # raise NoSuchElementException
        finally:
            return Flag

    def count_elements(self, locator):
        if self.is_element(locator):
            ele = WebDriverWait(self.driver, 5).until(EC.visibility_of_any_elements_located(locator))
        else:
            ele = ()
        return ele

    def find_elements_until_visibility(self, locator, timeout=10) -> WebElement:
        # 在规定时间内找某控件,eg:find_element_until_visibility(("By.XPATH",".//*[contains(@text,'XXX')"))
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.visibility_of_any_elements_located(locator))
            return ele
        except NoSuchElementException:
            print("Retrying to find element by %s: %s" % (locator[0], locator[1]))
        raise NoSuchElementException

    def findElement(self, locator):  # locator变量是定位器，给的值比如id和value，等同于：查找元素通过id的值value   findElement(By.ID, "tests")
        try:
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(
                lambda x: x.find_element(*locator))  # *locator取变量locator的值，locator的值的类型是元祖
            return ele
        except NoSuchElementException:
            print("Retrying to find element by %s: %s" % (locator[0], locator[1]))
        raise NoSuchElementException

    # def find(self, locator) -> WebElement:
    #     #todo: 处理弹框 异常处理 动态浮动的元素的处理
    #
    #     try:
    #         print(locator)
    #         return self.driver.find_element(*locator)
    #     except Exception as e:
    #         #黑名单处理
    #         if BasePage.max>3:
    #             raise e
    #         BasePage.max=BasePage.max+1
    #         for black in self.black_list:
    #             elements=self.driver.find_elements(*black)
    #             if len(elements)>=1:
    #                 elements[0].click()
    #
    #         return self.find(locator)

    def adb_button(self, keyboard):
        # 安卓可用,通过adb指令模拟键盘输入
        str = "adb shell input keyevent {keyboard}".format(keyboard=keyboard)
        os.system(str)

    def click_device_btn(self, key_num):
        # 安卓设备物理按键
        return self.driver.keyevent(key_num)

    @classmethod
    def toast_locator(cls):
        return (By.XPATH, "//*[@class='android.widget.Toast']")

    def get_page_source(self):
        # 获取page_source
        return self.driver.page_source

    def find_element(self, locator) -> WebElement:
        return self.driver.find_element(*locator)

    def is_element_and_swipe(self, locator, timeout=10):
        # 判断页面是否存在指定控件，没有则向下滑动
        while 1:
            flag = self.is_element(locator, timeout)
            if flag:
                break
            else:
                self.swipe(465, 1200, 465, 0, 1000)
                sleep(1)
        return self

    # @classmethod
    def swipe(self, start_x, start_y, end_x, end_y, dur=800):
        # start_x: 滑动起始点横坐标
        # start_y: 滑动起始点纵坐标
        # end_x：滑动终点横坐标
        # end_y：滑动终点纵坐标
        # dur：在多少时间内完成滑动动作（单位：ms毫秒）
        return self.driver.swipe(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y, duration=dur)

    def swipe_ele_left(self, ele, dur=800):
        """
        基于控件元素左滑操作
        :param ele: 控件元素
        :param dur: 在多少时间内完成滑动动作（单位：ms毫秒）
        :return:
        """
        start_x = int(ele.rect["width"]) - 20
        end_x = int(ele.rect["x"])
        height = int(ele.rect["y"]) + int(ele.rect["height"]) / 2
        self.driver.swipe(start_x, height, end_x, height, duration=dur)
        sleep(1)
        return self

    def hide_keyboard(self):
        """隐藏键盘"""
        return self.driver.hide_keyboard()

    def get_screenshot_as_png(self):
        """获取截图"""
        return self.driver.get_screenshot_as_png()

    def allure_screenshot(self, step="测试截图", story="Nomal"):
        """allure报告截图"""
        with allure.step(step):
            allure.attach(self.driver.get_screenshot_as_png(), story, allure.attachment_type.PNG)
        return self
