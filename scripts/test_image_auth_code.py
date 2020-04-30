import os
import time

from base.base_driver import init_driver
from page.page import Page


# 运行 清空后台 - 打开app - 进入 图形验证码 页面的流程
def enter_image_auth_code(self):
    self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
    self.page.home.click_login()  # 点击 登录 按钮
    for i in range(0, 2):
        if self.page.onekeyreg_login.is_element_exist(self.page.onekeyreg_login.onekeyreg_login_button, 1) is True:
            self.page.onekeyreg_login.click_other_reg()  # 点击 其他方式注册登录 按钮
            self.page.manually_login.input_username_phonenum_password(self.page.custom_functions.letters_num_count(8),
                                                                      self.page.custom_functions.letters_num_count(8))
            for i in range(0, 6):
                self.page.manually_login.click_now_login()
                if i <= 2:
                    assert self.page.image_auth_code.is_element_exist(
                        self.page.image_auth_code.image_auth_code_title, 1) is False
                elif i == 3 and self.page.image_auth_code.is_element_exist(
                        self.page.image_auth_code.image_auth_code_title, 1) is True:
                    break
                elif i >= 3 and self.page.image_auth_code.is_element_exist(
                        self.page.image_auth_code.image_auth_code_title, 1) is False:
                    print(f"\n第{i+1}次点击 立即登录 后没有打开图形验证码(账号密码错误时)--------\n")
                else:
                    break
            break
        elif self.page.auto_login.is_element_exist(self.page.auto_login.auto_login_title, 1) is True or \
                self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True:
            self.page.realname.pass_auth()  # 通过认证实名认证
            self.page.home.click_logout()  # 点击 登出 按钮
        else:
            print(f'error: 没有打开 一键注册登录 页面, 第{i + 1}次重试---------------')  # 再次重试打开
            self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
            self.page.home.click_login()  # 点击 登录 按钮


class TestImageAuthCode:

    def setup(self):
        self.driver = init_driver(no_reset=True)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    # 137 在图形验证码界面，点击右上角的 关闭× 按钮，能否关闭当前页面，并取消下一步操作
    # （比如，如果是登录，则终止登录操作的后续流程）
    def test_image_auth_code_137(self):
        print('\n\n-------- 正在测试 注册 - 图形验证码 模块 --------')
        enter_image_auth_code(self)  # 进入 图形验证码 页面
        self.page.image_auth_code.click_close_image_auth_code()
        assert self.page.manually_login.is_element_exist(self.page.manually_login.manually_login_title, 1) is True

    # 140 当图形验证输入框为空时， 继续 按钮是否为禁用状态
    def test_image_auth_code_140(self):
        enter_image_auth_code(self)  # 进入 图形验证码 页面
        self.page.image_auth_code.clear_image_auth_code()
        assert self.page.image_auth_code.get_enabled(self.page.image_auth_code.go_on_button) == "false"

    # 141 当图形验证输入框不为空时， 继续 按钮是否可用
    def test_image_auth_code_141(self):
        enter_image_auth_code(self)  # 进入 图形验证码 页面
        self.page.image_auth_code.clear_image_auth_code()
        self.page.image_auth_code.input_image_auth_code(self.page.custom_functions.letters_num_count(4))
        assert self.page.image_auth_code.get_enabled(self.page.image_auth_code.go_on_button) == "true"

    # 142 当输入错误的图形验证码时, 能否通过验证
    # 144 点击 继续 按钮后，是否同时禁用 继续 按钮
    def test_image_auth_code_142_144(self):
        enter_image_auth_code(self)  # 进入 图形验证码 页面
        self.page.image_auth_code.clear_image_auth_code()
        self.page.image_auth_code.input_image_auth_code(self.page.custom_functions.letters_num_count(4))
        self.page.image_auth_code.click_go_on()
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/image_auth_code_应该禁用继续按钮.png')
        assert self.page.image_auth_code.is_element_exist(self.page.image_auth_code.image_auth_code_title) is True

    # 146 验证失败后，是否有 验证码不正确，请重新输入 的错误提示，并清空验证码输入框，并重新获取新的验证码图片
    # 147 图形验证码页面是否有错别字，是否简洁易懂
    # 148 图形验证码页面的设计风格是否与UI的设计风格统一
    def test_image_auth_code_146_147_148(self):
        enter_image_auth_code(self)  # 进入 图形验证码 页面
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/image_auth_code_图形验证对比1.png')
        self.page.image_auth_code.click_image_auth_code()  # 点击图形验证码, 应该会刷新
        time.sleep(1)
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/image_auth_code_图形验证对比2.png')

    # 152 在图形验证码页面把app置于后台打开系统计算器应用计算数字后返回app能否继续
    def test_image_auth_code_152(self):
        enter_image_auth_code(self)  # 进入 图形验证码 页面
        self.page.custom_functions.calculator()
        self.page.custom_functions.click_all_apps_handle()
        self.page.custom_functions.click_start_app()
        print('\n-------- 注册 - 图形验证码 模块测试完成 --------')
        assert self.page.image_auth_code.is_element_exist(self.page.image_auth_code.image_auth_code_title) is True
