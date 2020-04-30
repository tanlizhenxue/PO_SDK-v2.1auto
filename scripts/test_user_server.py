import os
import time

from base.base_driver import init_driver
from page.page import Page


# 运行 清空后台 - 打开app - 进入 一键注册登录 页面的流程
def enter_onekeyreg_login(self):
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


class TestUserServer:

    def setup(self):
        self.driver = init_driver(no_reset=True)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    # 50 在用户注册、登录等画面上的 用户协议 的 标题和地址 能否从服务器端读取
    def test_user_server_050(self):
        print('\n\n-------- 正在测试 登录 - 用户服务协议 模块 --------')
        enter_onekeyreg_login(self)  # 进入 一键注册登录 页面
        time.sleep(0.5)
        if self.page.user_server.is_element_exist(self.page.user_server.user_service_button, 1) is True:
            assert 1
            self.page.onekeyreg_login.click_other_reg()
            time.sleep(0.5)
            if self.page.user_server.is_element_exist(self.page.user_server.user_service_button, 1) is True:
                assert 1
                self.page.manually_login.click_fast_reg()
                self.page.phonenum_reg.click_username_reg()
                time.sleep(0.5)
                if self.page.user_server.is_element_exist(self.page.user_server.user_service_button, 1) is not True:
                    assert 1
                else:
                    assert 0
            else:
                assert 0
        else:
            assert 0

    # 51 在用户注册、登录等画面上点击 用户协议 后能否通过 webview 打开协议
    def test_user_server_051(self):
        enter_onekeyreg_login(self)  # 进入 一键注册登录 页面
        self.page.user_server.click_user_service()
        if self.page.user_server.is_element_exist(self.page.user_server.user_service_title) is True:
            assert 1
            self.page.user_server.click_close_user_server()
        else:
            assert 0
        self.page.onekeyreg_login.click_other_reg()
        self.page.user_server.click_user_service()
        if self.page.user_server.is_element_exist(self.page.user_server.user_service_title) is True:
            assert 1
            self.page.user_server.click_close_user_server()
        else:
            assert 0
        self.page.manually_login.click_fast_reg()
        self.page.phonenum_reg.click_username_reg()
        self.page.user_server.click_user_service()
        if self.page.user_server.is_element_exist(self.page.user_server.user_service_title) is True:
            assert 1
            self.page.user_server.click_close_user_server()
        else:
            assert 0

    # 52 点击协议的 WebView 右上角的关闭按钮能否直接关闭，如备注图所示
    def test_user_server_052(self):
        enter_onekeyreg_login(self)  # 进入 一键注册登录 页面
        self.page.user_server.click_user_service()
        if self.page.user_server.is_element_exist(self.page.user_server.close_user_server_button) is True:
            self.page.user_server.click_close_user_server()
            time.sleep(1)
        assert self.page.user_server.is_element_exist(self.page.super_user.superuser_title) is False

    # 53 协议的 WebView 左侧的是否有返回按钮
    # 54 用户协议是否有错别字，是否简洁易懂
    # 55 用户协议的设计风格是否与UI的设计风格统一
    def test_user_server_053_054_055(self):
        enter_onekeyreg_login(self)  # 进入 一键注册登录 页面
        self.page.user_server.click_user_service()
        if self.page.user_server.is_element_exist(self.page.user_server.close_user_server_button) is True:
            time.sleep(3)
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/user_server_ui.png')

    # 56 打开协议后能否进行滑动操作查看，能否完全正确展示
    def test_user_server_056(self):
        enter_onekeyreg_login(self)  # 进入 一键注册登录 页面
        self.page.user_server.click_user_service()
        time.sleep(3)
        for i in range(0, 5):
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + f'./ui/user_server 0{i + 1}.png')
            self.driver.swipe((39 / 40) * self.page.custom_functions.get_window_size_x(),
                              (2750 / 2792) * self.page.custom_functions.get_window_size_y(),
                              (39 / 40) * self.page.custom_functions.get_window_size_x(),
                              (342 / 2792) * self.page.custom_functions.get_window_size_y(),
                              1500)

    # 57 在用户服务协议页面把app置于后台打开系统计算器应用计算数字后返回app能否继续过程
    def test_user_server_057(self):
        enter_onekeyreg_login(self)  # 进入 一键注册登录 页面
        self.page.user_server.click_user_service()
        time.sleep(3)
        self.page.custom_functions.calculator()
        self.page.custom_functions.click_all_apps_handle()
        self.page.custom_functions.click_start_app()
        print('\n-------- 登录 - 用户服务协议 模块测试完成 --------')
        assert self.page.user_server.is_element_exist(self.page.user_server.user_service_title) is True
