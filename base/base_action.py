import os
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=6, poll=0.1):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def find_elements(self, feature, timeout=6, poll=0.1):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    # 点击 的动作
    def click(self, feature):
        self.find_element(feature).click()

    # 清空 的动作
    def clear(self, feature):
        self.find_element(feature).clear()

    # 输入 的动作
    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    # 获取元素 text(文本) 的动作
    def get_text(self, feature):
        return self.find_element(feature).text

    # 获取 content-desc 属性, 如果为空则获取 text
    def get_content_desc(self, feature):
        return self.find_element(feature).get_attribute("name")

    # 获取元素 enabled属性 的动作 true
    def get_enabled(self, feature):
        return self.find_element(feature).get_attribute("enabled")

    # 判断某元素在当前页面是否存在(通过捕获异常的方式)
    def is_element_exist(self, feature, timeout=6):
        try:
            self.find_element(feature, timeout)
            return True
        except TimeoutException:
            return False

    # 根据部分 toast 出来的信息，判断toast动作是否存在
    def is_toast_exist(self, message):
        """
        :param message: 部分内容
        :return: 是否存在
        """
        message_xpath = By.XPATH, "//*[contains(@text,'%s')]" % message
        try:
            self.find_elements(message_xpath, 6, 0.1)
            return True
        except TimeoutException:
            return False

    # 根据部分 toast 出来的信息，获取toast出来的所有信息
    def get_toast_text(self, message):
        """
        :param message: 部分内容
        :return: 所有内容
        """
        if self.is_toast_exist(message):
            message_xpath = By.XPATH, "//*[contains(@text,'%s')]" % message
            return self.find_element(message_xpath, 6, 0.1).text
        else:
            raise Exception(f"error: 该toast未出现: {message} --------")

    # 等待一段时间, 但是要防止appium连接超时关闭
    def time_sleep(self, times, feature):
        for i in range(0, times):
            self.click(feature)
            time.sleep(1)
