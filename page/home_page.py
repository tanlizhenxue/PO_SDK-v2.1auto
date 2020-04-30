from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class HomePage(BaseAction):

    # 登录 按钮
    login_button = By.ID, "com.hzhy.sdk:id/tv_login"

    # 登出 按钮
    logout_button = By.ID, "com.hzhy.sdk:id/tv_logout"

    # 支付 按钮
    pay_button = By.ID, "com.hzhy.sdk:id/tv_pay"

    # H5 按钮
    h5_button = By.ID, "com.hzhy.sdk:id/tv_h5"

    # 点击sdk首页中的 登录 按钮
    def click_login(self):
        self.click(self.login_button)

    # 点击sdk首页中的 登出 按钮
    def click_logout(self):
        self.click(self.logout_button)

    # 点击sdk首页中的 支付 按钮
    def click_pay(self):
        self.click(self.pay_button)

    # 点击sdk首页中的 H5 按钮
    def click_h5(self):
        self.click(self.h5_button)
