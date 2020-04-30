from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class UserServerPage(BaseAction):

    # 汇游戏用户服务协议 勾选框
    checkbox_user_service = By.ID, "com.hzhy.sdk:id/iv_check"

    # 汇游戏用户服务协议 按钮
    user_service_button = By.XPATH, "//*[@text='汇游戏用户服务协议']"

    # 汇游戏用户服务协议页面右上角的 关闭× 按钮
    close_user_server_button = By.ID, "com.hzhy.sdk:id/ib_close"

    # 汇游戏用户服务协议页面的 标题
    user_service_title = By.ID, "com.hzhy.sdk:id/tv_title"

    # 点击 汇游戏用户服务协议 勾选框
    def click_checkbox_user_service(self):
        self.click(self.checkbox_user_service)

    # 点击 汇游戏用户服务协议 按钮
    def click_user_service(self):
        self.click(self.user_service_button)

    # 点击 汇游戏用户服务协议 页面右上角的 关闭× 按钮
    def click_close_user_server(self):
        self.click(self.close_user_server_button)
