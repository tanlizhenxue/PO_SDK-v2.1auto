import os
import time

from base.base_driver import init_driver
from page.page import Page


# 运行 清空后台 - 打开app - 进入 已登录 页面的流程(随机生成账号)
def enter_login(self):
    self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
    self.page.home.click_login()  # 点击 登录 按钮
    for i in range(0, 3):
        if self.page.onekeyreg_login.is_element_exist(self.page.onekeyreg_login.onekeyreg_login_button, 1.5
                                                      ) is True:
            self.page.onekeyreg_login.click_onekeyreg_login()
            self.page.onekeyreg_login.click_enter_game()
            break
        elif self.page.auto_login.is_element_exist(self.page.auto_login.auto_login_title, 2) is True or \
                self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True:
            self.page.realname.pass_auth()  # 通过认证实名认证
            self.page.home.click_logout()
        else:
            print(f'error: 没有打开 一键注册登录 页面, 第{i + 1}次重试---------------')  # 再次重试打开
            self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
            self.page.home.click_login()  # 点击 登录 按钮
    self.page.realname.pass_auth()  # 通过认证实名认证


# 如果需要 超级用户 权限就点击 允许, 不需要权限时就跳过
def allow_superuser(self):
    if self.page.superuser.is_element_exist(self.page.superuser.superuser_title, 2) is True:
        self.page.superuser.click_remember_forever()
        time.sleep(2)
        self.page.superuser.click_allow_superuser()
    else:
        pass


class TestAutoLogin:

    def setup(self):
        self.driver = init_driver(no_reset=True)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    # 03 当前配置目录下该游戏有最近登录的用户记录，且最近的一个用户的 token 未过期，是否执行 自动登录 流程
    def test_auto_login_003(self):
        print('\n\n-------- 正在测试 登录 - 自动登录 模块 --------')
        self.driver.set_network_connection(6)  # 恢复网络
        allow_superuser(self)  # 如果需要 超级用户 权限就点击 允许
        enter_login(self)  # 进入 已登录 页面
        self.page.home.click_login()  # 点击 登录 按钮
        assert self.page.auto_login.is_element_exist(self.page.auto_login.auto_login_title) is True

    # 04 当前配置目录下该游戏有最近登录的用户记录，且最近的一个用户的 token 未过期，
    # 执行 自动登录 流程时登录失败，是否进入 4、登录 处理流程
    def test_auto_login_004(self):
        enter_login(self)
        self.page.custom_functions.click_home_key()
        self.driver.set_network_connection(1)  # 打开 飞行 模式
        allow_superuser(self)  # 如果需要 超级用户 权限就点击 允许
        self.page.custom_functions.click_all_apps_handle()
        self.page.custom_functions.click_start_app()
        self.page.home.click_login()
        assert self.page.manually_login.is_element_exist(self.page.manually_login.manually_login_title) is True

    # 05 先断开网络，打开游戏，自动登录已有账号，是否有 toast 出的 message 信息
    def test_auto_login_005(self):
        self.driver.set_network_connection(6)  # 恢复网络
        allow_superuser(self)  # 如果需要 超级用户 权限就点击 允许
        enter_login(self)  # 进入 已登录 页面
        self.page.custom_functions.click_home_key()
        self.driver.set_network_connection(1)  # 打开 飞行 模式
        allow_superuser(self)  # 如果需要 超级用户 权限就点击 允许
        self.page.custom_functions.click_all_apps_handle()
        self.page.custom_functions.click_start_app()
        self.page.home.click_login()
        assert self.page.home.get_toast_text("网络连接错误") == "网络连接错误"

    # 06 自动登录 的过程中，在 自动登录 页面显示后的3秒内点击 切换账号 按钮，
    # 能否直接中断登录过程，并关闭 自动登录 页面，显示手动登录页面
    def test_auto_login_006(self):
        self.driver.set_network_connection(6)  # 恢复网络
        allow_superuser(self)  # 如果需要 超级用户 权限就点击 允许
        enter_login(self)  # 进入 已登录 页面
        self.page.home.click_login()  # 点击 登录 按钮
        self.page.auto_login.click_switch_account()
        assert self.page.manually_login.is_element_exist(self.page.manually_login.manually_login_title) is True

    # 08 自动登录 的过程中，在 自动登录 页面显示3秒后，是否已禁用 切换账号 按钮，并执行 自动登录 操作
    def test_auto_login_008(self):
        enter_login(self)  # 进入 已登录 页面
        self.page.home.click_login()  # 点击 登录 按钮
        assert self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True

    # 09 自动登录 后，用户名能否从当前游戏配置信息获取，取得最后一次登录的用户名
    def test_auto_login_009(self):
        self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
        self.page.home.click_login()  # 点击 登录 按钮
        for i in range(0, 2):
            if self.page.onekeyreg_login.is_element_exist(
                    self.page.onekeyreg_login.onekeyreg_login_button, 1) is True:
                self.page.onekeyreg_login.click_other_reg()  # 点击 其他方式注册登录 按钮
                self.page.manually_login.click_fast_reg()  # 点击 快速注册 按钮
                self.page.phonenum_reg.click_username_reg()  # 点击 用户名注册 选项
                # 账号准备
                username = self.page.custom_functions.letters_num_count(8)  # 生成将要注册的用户名和密码
                password = self.page.custom_functions.letters_num_count(8)
                self.page.username_reg.input_username_password(username, password)
                self.page.username_reg.click_now_reg()  # 点击 立即注册 按钮
                self.page.realname.pass_auth()  # 通过认证实名认证
                # 运行自动登录
                self.page.home.click_login()  # 点击 登录 按钮
                assert self.page.auto_login.get_text(self.page.auto_login.auto_login_account) == username
                break
            elif self.page.auto_login.is_element_exist(self.page.auto_login.auto_login_title, 1) is True or \
                    self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True:
                self.page.realname.pass_auth()  # 通过认证实名认证
                self.page.home.click_logout()  # 点击 登出 按钮
            else:
                print(f'error: 没有打开 一键注册登录 页面, 第{i + 1}次重试---------------')  # 再次重试打开
                self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
                self.page.home.click_login()  # 点击 登录 按钮

    # 10 自动登录 页面是否有错别字，是否简洁易懂
    # 11 自动登录 页面的设计风格是否与UI的设计风格统一
    def test_auto_login_010_011(self):
        enter_login(self)
        self.page.home.click_login()
        if self.page.auto_login.is_element_exist(self.page.auto_login.auto_login_title, 3) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/auto_login_ui.png')
        else:
            assert 0

    # 13 在 自动登录 过程中把app置于后台打开自带计算器应用计算数字后返回app能否继续 自动登录 过程
    def test_auto_login_013(self):
        enter_login(self)
        self.page.home.click_login()
        if self.page.auto_login.is_element_exist(self.page.auto_login.auto_login_title, 3) is True:
            self.page.custom_functions.calculator()
            self.page.custom_functions.click_all_apps_handle()
            self.page.custom_functions.click_start_app()
            assert self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True
        else:
            assert 0

    # 15 自动登录 成功后，注销当前登录账号，再次使用 手动登录 输入 账号和密码 能否登录成功
    def test_auto_login_015(self):
        self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
        self.page.home.click_login()  # 点击 登录 按钮
        for i in range(0, 2):
            if self.page.onekeyreg_login.is_element_exist(self.page.onekeyreg_login.onekeyreg_login_button, 1
                                                          ) is True:
                self.page.onekeyreg_login.click_other_reg()  # 点击 其他方式注册登录 按钮
                self.page.manually_login.click_fast_reg()  # 点击 快速注册 按钮
                self.page.phonenum_reg.click_username_reg()  # 点击 用户名注册 选项
                # 账号准备
                username = self.page.custom_functions.letters_num_count(8)  # 生成将要注册的用户名和密码
                password = self.page.custom_functions.letters_num_count(8)
                self.page.username_reg.input_username_password(username, password)
                self.page.username_reg.click_now_reg()  # 点击 立即注册 按钮
                self.page.realname.pass_auth()  # 通过认证实名认证
                # 运行自动登录
                self.page.home.click_login()  # 点击 登录 按钮
                self.page.realname.pass_auth()
                self.page.home.click_logout()
                self.page.onekeyreg_login.click_other_reg()  # 点击 其他方式注册登录 按钮
                self.page.manually_login.input_username_phonenum_password(username, password)
                self.page.manually_login.click_now_login()
                print('\n-------- 登录 - 自动登录 模块测试完成 --------')
                assert self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True
                break
            elif self.page.auto_login.is_element_exist(self.page.auto_login.auto_login_title, 1) is True or \
                    self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True:
                self.page.realname.pass_auth()  # 通过认证实名认证
                self.page.home.click_logout()  # 点击 登出 按钮
            else:
                print(f'error: 没有打开 一键注册登录 页面, 第{i + 1}次重试---------------')  # 再次重试打开
                self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
                self.page.home.click_login()  # 点击 登录 按钮
