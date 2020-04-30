import os
import random
import time

from base.base_driver import init_driver
from page.page import Page


# 运行 清空后台 - 打开app - 进入 手机号注册 页面的流程
def enter_phonenum_reg(self):
    self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
    self.page.home.click_login()  # 点击 登录 按钮
    for i in range(0, 2):
        if self.page.onekeyreg_login.is_element_exist(self.page.onekeyreg_login.onekeyreg_login_button, 1) is True:
            self.page.onekeyreg_login.click_other_reg()  # 点击 其他方式注册登录 按钮
            self.page.manually_login.click_fast_reg()  # 点击 快速注册 按钮
            break
        elif self.page.auto_login.is_element_exist(self.page.auto_login.auto_login_title, 1) is True or \
                self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True:
            self.page.realname.pass_auth()  # 通过认证实名认证
            self.page.home.click_logout()  # 点击 登出 按钮
        else:
            print(f'error: 没有打开 一键注册登录 页面, 第{i + 1}次重试---------------')  # 再次重试打开
            self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
            self.page.home.click_login()  # 点击 登录 按钮


class TestPhonenumReg:

    def setup(self):
        self.driver = init_driver(no_reset=True)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    # 23 进入 手机号注册 页面，点击左上角返回按钮，是否可以返回到上一个页面
    def test_phonenum_reg_023(self):
        print("\n\n-------- 正在测试 注册-手机号注册 模块 --------")
        enter_phonenum_reg(self)  # 进入 手机号注册 页面
        self.page.phonenum_reg.click_back_phonenum_reg()  # 点击 返回 按钮
        assert self.page.manually_login.find_element(self.page.manually_login.username_login_title)

    # 24 服务器端对当前游戏当前渠道未禁止注册，且当前游戏的注册配置值中允许使用手机号，是否显示 你也可以使用用户名注册
    def test_phonenum_reg_024(self):
        enter_phonenum_reg(self)  # 进入 手机号注册 页面
        assert self.page.phonenum_reg.get_text(self.page.phonenum_reg.also_username_reg) == "你也可以使用"
        assert self.page.phonenum_reg.get_text(self.page.phonenum_reg.username_reg_button) == "用户名注册"

    # 26 当输入的手机号码是非法的手机号码时，验证身份 按钮是否是不可用状态，是否显示 请输入正确的手机号码 提示信息
    def test_phonenum_reg_026(self):
        enter_phonenum_reg(self)
        self.page.phonenum_reg.input_phonenum_reg(self.page.custom_functions.num_count(11))
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/unrule_phonenum_reg.png')
        assert self.page.phonenum_reg.get_enabled(self.page.phonenum_reg.authentication_button) == "false"

    # 27 当输入的手机号码是合法的手机号码时，验证身份 按钮是否已启用
    # 42 手机号注册 页面是否有错别字，是否简洁易懂
    # 43 手机号注册 页面的设计风格是否与UI的设计风格统一
    def test_phonenum_reg_027_42_43(self):
        enter_phonenum_reg(self)
        self.page.phonenum_reg.input_phonenum_reg(str(177) + self.page.custom_functions.num_count(8))
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/phonenum_reg_page1.png')
        assert self.page.phonenum_reg.get_enabled(self.page.phonenum_reg.authentication_button) == "true"

    # 28 点击 验证身份 按钮后，是否同时禁用输入框、返回按钮、验证身份 按钮以及 用户名注册 按钮，
    # 是否同时将“验证身份”按钮文字修改为“正在验证”
    def test_phonenum_reg_028(self):
        enter_phonenum_reg(self)
        self.page.phonenum_reg.input_phonenum_reg(str(177) + self.page.custom_functions.num_count(8))
        self.page.phonenum_reg.click_authentication()
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/phonenum_reging.png')

    # 29 点击 验证身份 按钮后，是否能正常接收到 短信验证码
    def test_phonenum_reg_029(self):
        enter_phonenum_reg(self)
        self.page.phonenum_reg.input_phonenum_reg(13072522180)
        self.page.phonenum_reg.click_authentication()

    # 30 点击 验证身份 按钮后，是否能进入到输入 短信验证码 页面
    # 31 重试 按钮是否进入60秒倒计时状态, 且不可用
    # 32 在输入 短信验证码 页面，输入框是否默认聚焦
    def test_phonenum_reg_030_031_32(self):
        enter_phonenum_reg(self)
        self.page.phonenum_reg.input_phonenum_reg('176' + self.page.custom_functions.num_count(8))
        self.page.phonenum_reg.click_authentication()
        assert self.page.phonenum_reg.find_element(self.page.phonenum_reg.input_msg_code_title)
        assert self.page.phonenum_reg.get_text(self.page.phonenum_reg.retry_msg_code_button) >= str(0)
        assert self.page.phonenum_reg.get_enabled(self.page.phonenum_reg.retry_msg_code_button) == "false"
        os.system("adb shell input keyevent 13")
        assert self.page.phonenum_reg.get_text(self.page.phonenum_reg.msg_code_inputbox) == str(6)

    # 33 重试 按钮60秒倒计时结束后，是否已将按钮文字改为 重试，并启用该按钮
    def test_phonenum_reg_033(self):
        enter_phonenum_reg(self)
        self.page.phonenum_reg.input_phonenum_reg('176' + self.page.custom_functions.num_count(8))
        self.page.phonenum_reg.click_authentication()
        self.page.phonenum_reg.time_sleep(60, self.page.phonenum_reg.input_msg_code_title)
        assert self.page.phonenum_reg.get_text(self.page.phonenum_reg.retry_msg_code_button) == "重试"
        assert self.page.phonenum_reg.get_enabled(self.page.phonenum_reg.retry_msg_code_button) == "true"

    # 34 点击 重试 按钮后，是否已清空短信验证码输入框，并禁用 重试 按钮，并进入60秒倒计时
    def test_phonenum_reg_034(self):
        enter_phonenum_reg(self)
        self.page.phonenum_reg.input_phonenum_reg('176' + self.page.custom_functions.num_count(8))
        self.page.phonenum_reg.click_authentication()
        self.page.phonenum_reg.input_msg_code(666666)
        self.page.phonenum_reg.time_sleep(60, self.page.phonenum_reg.input_msg_code_title)
        self.page.phonenum_reg.click_retry_msg_code()
        assert self.page.phonenum_reg.get_enabled(self.page.phonenum_reg.retry_msg_code_button) == "false"
        assert self.page.phonenum_reg.get_text(self.page.phonenum_reg.retry_msg_code_button) >= str(0)
        assert self.page.phonenum_reg.get_text(self.page.phonenum_reg.msg_code_inputbox) == ""

    # 35 当连续第3次点击 重试 按钮后，是否已需要输入 图形验证码
    def test_phonenum_reg_035(self):
        enter_phonenum_reg(self)
        self.page.phonenum_reg.input_phonenum_reg('176' + self.page.custom_functions.num_count(8))
        self.page.phonenum_reg.click_authentication()
        for i in range(0, 3):
            self.page.phonenum_reg.time_sleep(60, self.page.phonenum_reg.input_msg_code_title)
            self.page.phonenum_reg.click_retry_msg_code()
            if i <= 1:
                assert self.page.phonenum_reg.find_element(self.page.phonenum_reg.input_msg_code_title)
            elif i >= 2:
                assert self.page.phonenum_reg.find_element(self.page.image_auth_code.image_auth_code_title)

    # 40 输入已经注册过的手机号后，点击 验证身份 按钮后是否有提示
    def test_phonenum_reg_040(self):
        enter_phonenum_reg(self)
        self.page.phonenum_reg.input_phonenum_reg(17605113956)
        self.page.phonenum_reg.click_authentication()
        assert self.page.phonenum_reg.get_toast_text("该手机号码已绑定") == "该手机号码已绑定"

    # 48 点击 验证身份 按钮后把app置于后台打开系统计算器应用计算数字后返回app能否继续注册
    def test_phonenum_reg_048(self):
        enter_phonenum_reg(self)
        self.page.custom_functions.calculator()
        self.page.custom_functions.click_all_apps_handle()
        self.page.custom_functions.click_start_app()
        assert self.page.phonenum_reg.phonenum_reg_title
        self.page.phonenum_reg.input_phonenum_reg("199" + self.page.custom_functions.num_count(8))
        self.page.phonenum_reg.click_authentication()
        print('\n-------- 注册 - 手机号注册 模块测试完成 --------')
        assert self.page.phonenum_reg.input_msg_code_title
