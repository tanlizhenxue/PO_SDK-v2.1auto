from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class OnekeyregLoginPage(BaseAction):

    # 一键注册登录 按钮
    onekeyreg_login_button = By.ID, "com.hzhy.sdk:id/iv_onekeylogin"

    # 一键注册登录页面的 其他方式注册登录 按钮
    other_reg_button = By.ID, "com.hzhy.sdk:id/tv_otherreg"

    # 进入游戏 按钮
    enter_game_button = By.ID, "com.hzhy.sdk:id/tv_start"

    # sdk_name
    sdk_name = By.ID, "com.hzhy.sdk:id/tv_sdkname"

    # 一键注册登录成功的账号
    username = By.ID, "com.hzhy.sdk:id/tv_username"

    # 一键注册登录成功的密码
    password = By.ID, "com.hzhy.sdk:id/tv_password"

    # 一键注册登录页面的 标题
    onekeyreg_login_title = By.ID, "com.hzhy.sdk:id/iv_onekeylogin"

    # 点击 一键注册登录 按钮
    def click_onekeyreg_login(self):
        self.click(self.onekeyreg_login_button)

    # 点击一键注册登录页面的 其他方式注册登录 按钮
    def click_other_reg(self):
        self.click(self.other_reg_button)

    # 点击 进入游戏 按钮
    def click_enter_game(self):
        self.click(self.enter_game_button)
