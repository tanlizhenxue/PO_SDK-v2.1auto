from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class UsernameRegPage(BaseAction):

    # 用户名注册页面左上角的 返回< 按钮
    username_reg_back_button = By.ID, "com.hzhy.sdk:id/iv_back"

    # 用户名注册页面的 用户名 输入框
    username_inputbox = By.ID, "com.hzhy.sdk:id/et_account"

    # 用户名注册页面的 密码 输入框
    password_inputbox = By.ID, "com.hzhy.sdk:id/et_password"

    # 用户名注册页面的 立即注册 按钮
    now_reg_button = By.ID, "com.hzhy.sdk:id/tv_sign_up"

    # 用户名注册 页面的标题
    username_reg_title = By.XPATH, "//*[@text='账号注册']"

    # 用户名注册成功后的页面 标题
    username_reg_success_title = By.XPATH, "//*[@text='注册成功！']"

    # 用户名注册成功后的账号
    account = By.ID, "com.hzhy.sdk:id/tv_count"

    # 用户名注册成功后显示 正在启动实名认证，请稍等...
    starting_realname_auth = By.XPATH, "//*[@text='正在启动实名认证，请稍等...']"

    # 点击 用户名注册页面左上角的 返回< 按钮
    def click_back_username_reg(self):
        self.click(self.username_reg_back_button)

    # 清空用户名注册页面的 用户名 输入框
    def clear_username(self):
        self.clear(self.username_inputbox)

    # 在用户名注册页面输入 用户名
    def input_username(self, username):
        self.input(self.username_inputbox, username)

    # 点击 用户名输入框
    def click_username_inputbox(self):
        self.click(self.username_inputbox)

    # 清空用户名注册页面的 密码 输入框
    def clear_password(self):
        self.clear(self.password_inputbox)

    # 在用户名注册页面输入账号的 密码
    def input_password(self, password):
        self.input(self.password_inputbox, password)

    # 点击 密码输入框
    def click_password_inputbox(self):
        self.click(self.password_inputbox)

    # 点击用户名注册页面的 立即注册 按钮
    def click_now_reg(self):
        self.click(self.now_reg_button)

    # 在用户名注册页面输入 账号 和 密码
    def input_username_password(self, username, password):
        self.clear_username()
        self.input_username(username)
        self.clear_password()
        self.input_password(password)
