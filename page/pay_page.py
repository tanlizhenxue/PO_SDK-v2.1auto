from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class PayPage(BaseAction):

    # 右上角的 关闭× 按钮
    close_pay_button = By.ID, "com.hzhy.sdk:id/close_page"

    # 退出支付时的 退出 按钮
    quit_button = By.ID, "com.hzhy.sdk:id/button1"

    # 收银台页面的 标题
    pay_title = By.XPATH, "//*[@text='充值']"

    # 点击右上角的 关闭× 按钮
    def click_close_pay(self):
        self.click(self.close_pay_button)

    # 点击退出支付时的 退出 按钮
    def click_quit(self):
        self.click(self.quit_button)
