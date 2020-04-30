from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class AutoLoginPage(BaseAction):

    # 自动登录时显示的该账号名字
    auto_login_account = By.ID, "com.hzhy.sdk:id/tv_phone"

    # 切换账号 按钮
    switch_account_button = By.ID, "com.hzhy.sdk:id/tv_switch"

    # 自动登录页面标题
    auto_login_title = By.XPATH, "//*[@text='登录中...']"

    # 点击 切换账号 按钮
    def click_switch_account(self):
        self.click(self.switch_account_button)
