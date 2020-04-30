from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class PhonenumRegPage(BaseAction):

    # 手机号注册页面左上角的 返回< 按钮
    phonenum_reg_back_button = By.ID, "com.hzhy.sdk:id/reg_back"

    # 手机号输入框
    phonenum_reg_inputbox = By.ID, "com.hzhy.sdk:id/et_phone"

    # 手机号注册页面的 验证身份 按钮
    authentication_button = By.ID, "com.hzhy.sdk:id/tv_identity"

    # 手机号注册页面的 用户名注册 选项
    username_reg_button = By.ID, "com.hzhy.sdk:id/other_reg"

    # 输入短信验证码页面左上角的 返回< 按钮
    msg_code_back_button = By.ID, "com.hzhy.sdk:id/iv_back"

    # 短信验证码输入框
    msg_code_inputbox = By.ID, "com.hzhy.sdk:id/et_msg_code"

    # 输入短信验证码页面的 重试 按钮
    retry_msg_code_button = By.ID, "com.hzhy.sdk:id/tv_countdown"

    # 你也可以使用 标题
    also_username_reg = By.XPATH, "//*[@text='你也可以使用']"

    # 手机号注册页面的 标题
    phonenum_reg_title = By.XPATH, "//*[@text='使用手机号注册']"

    # 输入短信验证码页面的 标题
    input_msg_code_title = By.XPATH, "//*[@text='验证手机号']"

    # 点击手机号注册页面左上角的 返回< 按钮
    def click_back_phonenum_reg(self):
        self.click(self.phonenum_reg_back_button)

    # 清空 手机号 输入框
    def clear_phonenum_reg(self):
        self.driver.clear(self.phonenum_reg_inputbox)

    # 输入 手机号
    def input_phonenum_reg(self, phonenum):
        self.input(self.phonenum_reg_inputbox, phonenum)

    # 点击手机号注册页面的 验证身份 按钮
    def click_authentication(self):
        self.click(self.authentication_button)

    # 点击 手机号注册页面的 用户名注册 按钮
    def click_username_reg(self):
        self.click(self.username_reg_button)

    # 点击输入短信验证码页面左上角的 返回< 按钮
    def click_back_msg_code(self):
        self.click(self.msg_code_back_button)

    # 在输入短信验证码页面输入 短信验证码
    def input_msg_code(self, msg_code):
        self.input(self.msg_code_inputbox, msg_code)

    # 点击输入短信验证码页面的 重试 按钮
    def click_retry_msg_code(self):
        self.click(self.retry_msg_code_button)
