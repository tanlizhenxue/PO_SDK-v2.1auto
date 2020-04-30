from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class ImageAuthCodePage(BaseAction):

    # 图形验证码右上角的 关闭× 按钮
    close_image_auth_code_button = By.ID, "com.hzhy.sdk:id/iv_close"

    # 图形验证码输入框
    image_auth_code_inputbox = By.ID, "com.hzhy.sdk:id/et_code"

    # 图形验证码
    image_auth_code = By.ID, "com.hzhy.sdk:id/iv_verified"

    # 图形验证码页面的 继续 按钮
    go_on_button = By.ID, "com.hzhy.sdk:id/tv_complete"

    # 图形验证码页面的标题
    image_auth_code_title = By.XPATH, "//*[@text='输入验证码']"

    # 点击 图形验证码右上角的 关闭× 按钮
    def click_close_image_auth_code(self):
        self.click(self.close_image_auth_code_button)

    # 清空 图形验证码输入框
    def clear_image_auth_code(self):
        self.clear(self.image_auth_code_inputbox)

    # 输入 图形验证码
    def input_image_auth_code(self, image_auth_code):
        self.input(self.image_auth_code_inputbox, image_auth_code)

    # 点击 图形验证码
    def click_image_auth_code(self):
        self.click(self.image_auth_code)

    # 点击 继续 按钮
    def click_go_on(self):
        self.click(self.go_on_button)
