from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class ManuallyLoginPage(BaseAction):

    # 手动登录页面的 用户名/手机号 输入框
    username_phonenum_inputbox = By.ID, "com.hzhy.sdk:id/edit_sipnner_edit"

    # 手动登录页面的 密码输入框
    password_inputbox = By.ID, "com.hzhy.sdk:id/et_password"

    # 手动登录页面的 忘记密码 按钮
    forget_password_button = By.ID, "com.hzhy.sdk:id/tv_retrieve_password"

    # 手动登录页面的 立即登录 按钮
    now_login_button = By.ID, "com.hzhy.sdk:id/tv_login"

    # 手动登录页面的 快速注册 按钮
    fast_reg_button = By.ID, "com.hzhy.sdk:id/fast_sign_up"

    # 手动登录页面的 账号登录 标题
    manually_login_title = By.XPATH, "//*[@text='账号登录']"

    # 清空手动登录页面的 用户名/手机号 输入框
    def clear_username_phonenum(self):
        self.clear(self.username_phonenum_inputbox)

    # 在手动登录页面输入 用户名/手机号
    def input_username_phonenum(self, username_phonenum):
        self.input(self.username_phonenum_inputbox, username_phonenum)

    # 清空手动登录页面的 密码 输入框
    def clear_password(self):
        self.clear(self.password_inputbox)

    # 在手动登录页面输入 密码
    def input_password(self, password):
        self.input(self.password_inputbox, password)

    # 点击 手动登录 页面的 忘记密码 按钮
    def click_forget_password(self):
        self.click(self.forget_password_button)

    # 点击手动登录页面的 立即登录 按钮
    def click_now_login(self):
        self.click(self.now_login_button)

    # 点击手动登录页面的 快速注册 按钮
    def click_fast_reg(self):
        self.click(self.fast_reg_button)

    # 在手动登录页面输入 用户名/手机号 和 密码
    def input_username_phonenum_password(self, username_phonenum, password):
        self.clear_username_phonenum()  # 清空手动登录页面的 用户名/手机号 输入框
        self.input_username_phonenum(username_phonenum)  # 在手动登录页面输入 用户名/手机号
        self.clear_password()  # 清空手动登录页面的 密码 输入框
        self.input_password(password)  # 在手动登录页面输入 密码
