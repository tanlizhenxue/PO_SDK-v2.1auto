import os
import time

from base.base_driver import init_driver
from page.page import Page


# 运行 清空后台 - 打开app - 进入 手动登录 页面的流程
def enter_manually_login(self):
    self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
    self.page.home.click_login()  # 点击 登录 按钮
    for i in range(0, 2):
        if self.page.onekeyreg_login.is_element_exist(self.page.onekeyreg_login.onekeyreg_login_button, 1) is True:
            break
        elif self.page.auto_login.is_element_exist(self.page.auto_login.auto_login_title, 1) is True or \
                self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True:
            self.page.realname.pass_auth()  # 通过认证实名认证
            self.page.home.click_logout()  # 点击 登出 按钮
        else:
            print(f'error: 没有打开 一键注册登录 页面, 第{i + 1}次重试---------------')  # 再次重试打开
            self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
            self.page.home.click_login()  # 点击 登录 按钮
    self.page.onekeyreg_login.click_other_reg()  # 点击 其他方式注册登录 按钮


# 如果需要 超级用户 权限就点击 允许, 不需要权限时就跳过
def allow_superuser(self):
    if self.page.superuser.is_element_exist(self.page.superuser.superuser_title, 2) is True:
        self.page.superuser.click_remember_forever()
        time.sleep(2)
        self.page.superuser.click_allow_superuser()
    else:
        pass


class TestManuallyLogin:

    def setup(self):
        self.driver = init_driver(no_reset=True)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    # 16 点击 快速注册 按钮，能否关闭当前页面
    def test_manually_login_016(self):
        print('\n\n-------- 正在测试 登录 - 手动登录 模块 --------')
        self.driver.set_network_connection(6)  # 恢复网络, 此时会请求 超级用户 权限
        allow_superuser(self)
        enter_manually_login(self)  # 进入 手动登录 页面
        self.page.manually_login.click_fast_reg()
        assert self.page.manually_login.is_element_exist(self.page.manually_login.manually_login_title, 2) is False

    # 17 服务协议的 checkbox 未勾选时，则 立即登录 、 快速注册 按钮是否已置为不可用状态
    def test_manually_login_017(self):
        enter_manually_login(self)  # 进入 手动登录 页面
        self.page.user_server.click_checkbox_user_service()
        assert self.page.manually_login.get_enabled(self.page.manually_login.now_login_button) == "false"
        assert self.page.manually_login.get_enabled(self.page.manually_login.fast_reg_button) == "false"

    # 18 不输入 用户名/手机号和密码 ，点击 立即登录 按钮能否执行登录操作
    def test_manually_login_018(self):
        enter_manually_login(self)  # 进入 手动登录 页面
        self.page.manually_login.clear_username_phonenum()
        self.page.manually_login.clear_password()
        self.page.manually_login.click_now_login()
        assert self.page.manually_login.is_element_exist(self.page.manually_login.manually_login_title,
                                                         1) is not False

    # 19 输入错误的 用户名/手机号和密码 ，点击 立即登录 按钮能否执行登录操作
    def test_manually_login_019(self):
        enter_manually_login(self)  # 进入 手动登录 页面
        self.page.manually_login.input_username_phonenum_password(self.page.custom_functions.letters_num_count(8),
                                                                  self.page.custom_functions.letters_num_count(8))
        self.page.manually_login.click_now_login()
        assert self.page.manually_login.is_element_exist(self.page.manually_login.manually_login_title,
                                                         1) is not False

    # 32 点击 立即登录 按钮后，此时是否已禁用 立即登录、输入框、以及其他按钮
    # 33 点击 立即登录 按钮后，立即登录 按钮文字是否已修改为 正在登录...
    def test_manually_login_032_033(self):
        enter_manually_login(self)  # 进入 手动登录 页面
        self.page.manually_login.click_fast_reg()  # 点击 快速注册 按钮
        self.page.phonenum_reg.click_username_reg()  # 点击 用户名注册 选项
        # 账号准备
        username = self.page.custom_functions.letters_num_count(8)  # 生成将要注册的用户名和密码
        password = self.page.custom_functions.letters_num_count(8)
        self.page.username_reg.input_username_password(username, password)
        self.page.username_reg.click_now_reg()  # 点击 立即注册 按钮
        self.page.realname.pass_auth()  # 通过认证实名认证
        self.page.home.click_logout()
        self.page.onekeyreg_login.click_other_reg()  # 点击 其他方式注册登录 按钮
        self.page.manually_login.input_username_phonenum_password(username, password)
        self.page.manually_login.click_now_login()
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/manually_logining.png')

    # 34 当登录失败时，是否显示接口返回的错误提示信息(网络原因导致)
    def test_manually_login_034(self):
        enter_manually_login(self)  # 进入 手动登录 页面
        self.page.manually_login.click_fast_reg()  # 点击 快速注册 按钮
        self.page.phonenum_reg.click_username_reg()  # 点击进入 用户名注册 选项
        # 账号准备
        username = self.page.custom_functions.letters_num_count(8)  # 生成将要注册的用户名和密码
        password = self.page.custom_functions.letters_num_count(8)
        self.page.username_reg.input_username_password(username, password)
        self.page.username_reg.click_now_reg()  # 点击 立即注册 按钮
        self.page.realname.pass_auth()  # 通过认证实名认证
        self.page.home.click_logout()
        self.page.onekeyreg_login.click_other_reg()  # 点击 其他方式注册登录 按钮
        self.page.manually_login.input_username_phonenum_password(username, password)
        self.driver.set_network_connection(1)  # 打开飞行模式
        allow_superuser(self)  # 如果请求超级用户权限就点击 允许
        self.page.manually_login.click_now_login()
        assert self.page.manually_login.get_toast_text("网络连接错误") == "网络连接错误"

    # 36 登录成功后，判断当前游戏的实名认证配置，如果可选实名认证，能否进入 实名认证 页面
    def test_manually_login_036(self):
        self.driver.set_network_connection(6)  # 恢复网络, 此时会请求 超级用户 权限
        allow_superuser(self)  # 如果请求超级用户权限就点击 允许
        enter_manually_login(self)  # 进入 手动登录 页面
        self.page.manually_login.click_fast_reg()  # 点击 快速注册 按钮
        self.page.phonenum_reg.click_username_reg()  # 点击 用户名注册 选项
        # 账号准备
        username = self.page.custom_functions.letters_num_count(8)  # 生成将要注册的用户名和密码
        password = self.page.custom_functions.letters_num_count(8)
        self.page.username_reg.input_username_password(username, password)
        self.page.username_reg.click_now_reg()  # 点击 立即注册 按钮
        self.page.realname.pass_auth()  # 通过认证实名认证
        self.page.home.click_logout()  # 点击 登出
        self.page.onekeyreg_login.click_other_reg()  # 点击 其他方式注册登录 按钮
        self.page.manually_login.input_username_phonenum_password(username, password)
        self.page.manually_login.click_now_login()
        assert self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True

    # 37 游戏打开登录期间， 用户 连续登录失败 超过3次，则点击登录按钮时，是否会弹出 图形验证码 验证页面
    def test_manually_login_037(self):
        enter_manually_login(self)  # 进入 手动登录 页面
        self.page.manually_login.input_username_phonenum_password(self.page.custom_functions.letters_num_count(8),
                                                                  self.page.custom_functions.letters_num_count(8))
        for i in range(0, 4):
            self.page.manually_login.click_now_login()
        assert self.page.image_auth_code.is_element_exist(self.page.image_auth_code.image_auth_code_title) is True

    # 38 游戏打开登录期间， 用户 连续登录失败 3次后, 再登录成功是否已将计数器清零（只要有一次登录成功，就将计数器清零）
    def test_manually_login_038(self):
        enter_manually_login(self)  # 进入 手动登录 页面
        self.page.manually_login.click_fast_reg()  # 点击 快速注册 按钮
        self.page.phonenum_reg.click_username_reg()  # 点击 用户名注册 选项
        # 手动登录账号准备
        username = self.page.custom_functions.letters_num_count(8)  # 生成将要注册的用户名和密码
        password = self.page.custom_functions.letters_num_count(8)
        self.page.username_reg.input_username_password(username, password)
        self.page.username_reg.click_now_reg()  # 点击 立即注册 按钮
        self.page.realname.pass_auth()  # 通过认证实名认证
        self.page.home.click_logout()  # 点击 登出 按钮
        self.page.onekeyreg_login.click_other_reg()  # 点击 其他方式注册登录 按钮
        # 先手动登录失败3次, 此时不会打开图形验证码
        self.page.manually_login.input_username_phonenum_password(
            self.page.custom_functions.letters_num_count(8),
            self.page.custom_functions.letters_num_count(8))
        for i in range(0, 3):
            self.page.manually_login.click_now_login()
        # 输入正确的账号和密码进行登录
        self.page.manually_login.input_username_phonenum_password(username, password)
        self.page.manually_login.click_now_login()
        self.page.realname.pass_auth()
        self.page.home.click_logout()  # 点击 登出
        self.page.onekeyreg_login.click_other_reg()  # 点击 其他方式注册登录 按钮
        # 输入随机生成的数据作为账号和密码进进行登录
        self.page.manually_login.input_username_phonenum_password(
            self.page.custom_functions.letters_num_count(8),
            self.page.custom_functions.letters_num_count(8))
        for i in range(0, 5):
            if i <= 2:
                self.page.manually_login.click_now_login()
                assert self.page.realname.is_element_exist(self.page.realname.realname_auth_title, 1) is False
            elif i >= 3:
                self.page.manually_login.click_now_login()
                assert self.page.image_auth_code.is_element_exist(
                    self.page.image_auth_code.image_auth_code_title, 1) is True
                break

    # 40 手动登录 页面是否有错别字，是否简洁易懂
    # 41 手动登录 页面的设计风格是否与UI的设计风格统一
    def test_manually_login_040_41(self):
        enter_manually_login(self)  # 进入 手动登录 页面
        time.sleep(0.5)
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/manually_login_ui.png')

    # 46 在 手动登录 过程中把app置于后台打开系统计算器应用计算数字后返回app能否继续操作
    def test_manually_login_046(self):
        enter_manually_login(self)  # 进入 手动登录 页面
        self.page.manually_login.click_fast_reg()  # 点击 快速注册 按钮
        self.page.phonenum_reg.click_username_reg()  # 点击 用户名注册 选项
        # 账号准备
        username = self.page.custom_functions.letters_num_count(8)  # 生成将要注册的用户名和密码
        password = self.page.custom_functions.letters_num_count(8)
        self.page.username_reg.input_username_password(username, password)
        self.page.username_reg.click_now_reg()  # 点击 立即注册 按钮
        self.page.realname.pass_auth()  # 通过认证实名认证
        self.page.home.click_logout()  # 点击 登出
        self.page.onekeyreg_login.click_other_reg()  # 点击 其他方式注册登录 按钮
        self.page.custom_functions.calculator()
        self.page.custom_functions.click_all_apps_handle()
        self.page.custom_functions.click_start_app()
        print('\n-------- 登录 - 手动登录 模块测试完成 --------')
        assert self.page.manually_login.is_element_exist(self.page.manually_login.manually_login_title
                                                         ) is True
        self.page.manually_login.input_username_phonenum_password(username, password)
        self.page.manually_login.click_now_login()
        assert self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True
