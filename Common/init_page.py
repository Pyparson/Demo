import os
from time import sleep

import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from Common.base_page import BasePage
from Page.home_page import HomePage
from Page.smart_page import SmartPage


class InitPage(BasePage):
    _home = (By.XPATH, "//*[contains(@text,'家庭')]")
    _smart = (By.XPATH, "//*[contains(@text,'智能')]")
    _mine = (By.XPATH, "//*[contains(@text,'我的')]")
    _toast = (By.XPATH, "//*[@class='android.widget.Toast']")

    driver = None
    desired_caps = {}
    base_path = os.path.dirname(__file__)
    p = os.path.abspath(os.path.join(base_path, "..", "config.yaml"))
    with open(p, 'r')as f:
        data = yaml.load(f)
    platformName = data["platformName"]
    appPackage = data["appPackage"]
    appActivity = data["appActivity"]
    if platformName == "Android":
        desired_caps["platformName"] = platformName
        desired_caps["appPackage"] = appPackage
        desired_caps["appActivity"] = appActivity
        desired_caps["noReset"] = True
        desired_caps["deviceName"] = "Mi"
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        # desired_caps["automationName"] = "uiautomator2"
    elif data["platformName"] == "IOS":
        desired_caps["platformName"] = data["platformName"]
        desired_caps["udid"] = data["udid"]
        desired_caps["platformVersion"] = data["platformVersion"]
        desired_caps["app"] = os.path.abspath(os.path.join(base_path, "LarkApp.ipa"))
        desired_caps["noReset"] = True
        desired_caps["deviceName"] = "Mi"
        desired_caps["automationName"] = "XCUITest"
        desired_caps["xcodeOrgId"] = "692AM2VNT3"
        desired_caps["xcodeSigningId"] = "iPhone Developer"
    else:
        print("PlatformName must be Android or IOS")
        raise BaseException("PlatformName must be Android or IOS")

    def first_start(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(20)
        self.driver.hide_keyboard()
        InitPage.driver = self.driver

    def __init__(self):
        if InitPage.driver == None:
            self.first_start()
        elif self.platformName == "Android":
            print("Launch ...")
            self.driver.start_activity(self.appPackage, self.appActivity)
        else:
            pass

    def goto_home(self):
        self.find_element_until_visibility(self._home).click()
        return HomePage(self.driver)

    def goto_smart(self):
        self.find_element_until_visibility(locator=self._smart).click()
        return SmartPage(self.driver)


    def get_toast(self):
        # 获取toast
        # return self.find_element_until_visibility(self._toast).text
        return self.find_element(self._toast).text

    def is_home_page(self):
        while 1:
            sleep(1)
            flag = self.is_element(self._home, timeout=3)
            if flag:
                break
            else:
                self.click_device_btn(4)

    def get_obj_num(self, obj):
        """与业务无关,获取传参个数"""
        if "int" in str(type(obj)):
            temp = 1
        else:
            temp = len(obj)
        return temp


