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


# 运行一键注册登录成功后 进入游戏 - 关闭实名认证 - 点击 登出 按钮 的流程
def enter_game_logout(self):
    self.page.onekeyreg_login.click_enter_game()  # 点击 进入游戏
    self.page.realname.pass_auth()  # 点击 关闭实名认证 页面
    self.page.home.click_logout()  # 点击 登出


class TestOnekeyregLogin:

    def setup(self):
        self.driver = init_driver(no_reset=True)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    # 02 正常时能否打开 一键注册登录 页面
    def test_onekeyreg_login_002(self):
        print('\n\n-------- 正在测试 注册 - 一键注册登录 模块 --------')
        enter_onekeyreg_login(self)  # 清空后台到打开 一键注册登录 页面
        assert self.page.onekeyreg_login.is_element_exist(self.page.onekeyreg_login.onekeyreg_login_button) is True

    # 03 上文中的 汇游戏 文字，是否是动态的，从配置文件中的 sdk_name 字段读取。该字段的默认值为“汇游戏”
    def test_onekeyreg_login_003(self):
        enter_onekeyreg_login(self)  # 清空后台到打开 一键注册登录 页面
        assert self.page.onekeyreg_login.get_text(self.page.onekeyreg_login.sdk_name) == "汇游戏"

    # 04 当用户协议的checkbox未选中时，是否已经禁用 一键注册登录 按钮
    def test_onekeyreg_login_004(self):
        enter_onekeyreg_login(self)  # 清空后台到打开 一键注册登录 页面
        self.page.user_server.click_checkbox_user_service()  # 点击勾选框
        assert self.page.onekeyreg_login.get_enabled(self.page.onekeyreg_login.onekeyreg_login_button) == 'false'
        self.page.user_server.click_checkbox_user_service()  # 再次点击勾选框

    # 05 一键注册登录 页面是否有错别字，是否简洁易懂
    # 06 一键注册登录 页面的设计风格是否与UI的设计风格统一
    def test_onekeyreg_login_005_006(self):
        enter_onekeyreg_login(self)  # 清空后台到打开 一键注册登录 页面
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/onekeyreg_login_ui.png')

    # 07 点击 一键注册登录 按钮后，是否将该按钮置为不可用状态，
    # 并且将 其他方式注册登录 链接按钮的文字改为 请稍等，正在自动注册... ，并且取该链接按钮不可点击
    def test_onekeyreg_login_007(self):
        enter_onekeyreg_login(self)  # 清空后台到打开 一键注册登录 页面
        self.page.onekeyreg_login.click_onekeyreg_login()  # 点击 一键注册登录 按钮
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/onekeyreg_logining.png')
        enter_game_logout(self)  # 运行一键注册登录成功后 进入游戏 - 关闭实名认证 - 点击 登出 按钮 的流程

    # 08 点击 一键注册登录 按钮自动注册成功后，是否能够自动生成用户名及密码，并截图保存到手机相册中
    def test_onekeyreg_login_008(self):
        enter_onekeyreg_login(self)  # 清空后台到打开 一键注册登录 页面
        self.page.onekeyreg_login.click_onekeyreg_login()  # 点击 一键注册登录 按钮
        assert self.page.onekeyreg_login.find_element(self.page.onekeyreg_login.username)
        assert self.page.onekeyreg_login.find_element(self.page.onekeyreg_login.password)
        enter_game_logout(self)  # 运行一键注册登录成功后 进入游戏 - 关闭实名认证 - 点击 登出 按钮 的流程

    # 09 点击 一键注册登录 按钮自动注册成功后，是否 toast 提示: 汇游戏账号密码已经截图保存到您的相册
    def test_onekeyreg_login_009(self):
        enter_onekeyreg_login(self)  # 清空后台到打开 一键注册登录 页面
        self.page.onekeyreg_login.click_onekeyreg_login()  # 点击 一键注册登录 按钮
        assert (self.page.onekeyreg_login.get_toast_text("汇游戏账号密码已经截图保存到您的相册")
                == "汇游戏账号密码已经截图保存到您的相册")
        enter_game_logout(self)  # 运行一键注册登录成功后 进入游戏 - 关闭实名认证 - 点击 登出 按钮 的流程

    # 10 注册成功后，点击"进入游戏"按钮，如果当前游戏配置启用了实名认证功能，是否关闭了当前窗口，并且显示 实名认证 窗口
    def test_onekeyreg_login_010(self):
        enter_onekeyreg_login(self)  # 清空后台到打开 一键注册登录 页面
        self.page.onekeyreg_login.click_onekeyreg_login()  # 点击 一键注册登录 按钮
        self.page.onekeyreg_login.click_enter_game()  # 点击 进入游戏
        assert self.page.realname.find_element(self.page.realname.finish_realname_button)
        self.page.realname.pass_auth()  # 关闭实名认证页面
        self.page.home.click_logout()  # 点击 登出

    # 12 点击 其他方式注册登录 按钮，是否关闭 一键注册登录 窗口，并显示 手动登录 窗口
    def test_onekeyreg_login_012(self):
        enter_onekeyreg_login(self)  # 清空后台到打开 一键注册登录 页面
        self.page.onekeyreg_login.click_other_reg()  # 点击其他方式注册登录
        assert self.page.manually_login.find_element(self.page.manually_login.username_login_text)

    # 13 点击 其他方式注册登录 按钮后进入 手动登录 页面，点击back键是否可以返回或退出app
    def test_onekeyreg_login_013(self):
        enter_onekeyreg_login(self)  # 清空后台到打开 一键注册登录 页面
        self.page.onekeyreg_login.click_other_reg()  # 点击其他方式注册登录
        self.page.custom_functions.click_back_key()  # 点击 back 键
        assert self.page.manually_login.find_element(self.page.manually_login.username_login_text)

    # 18 一键注册登录 过程中自动生成的 账号 和 密码 能否在 手动登录 页面中登录成功
    def test_onekeyreg_login_018(self):
        enter_onekeyreg_login(self)  # 清空后台到打开 一键注册登录 页面
        self.page.onekeyreg_login.click_onekeyreg_login()  # 点击 一键注册登录 按钮
        get_username = self.page.onekeyreg_login.get_text(self.page.onekeyreg_login.username)
        get_password = self.page.onekeyreg_login.get_text(self.page.onekeyreg_login.password)
        enter_game_logout(self)
        self.page.onekeyreg_login.click_other_reg()  # 点击其他方式注册登录
        self.page.manually_login.input_username_phonenum_password(get_username, get_password)
        self.page.manually_login.click_now_login()
        assert self.page.realname.find_element(self.page.realname.realname_auth)
        self.page.realname.pass_auth()  # 点击 关闭实名认证 页面
        self.page.home.click_logout()  # 点击 登出

    # 19 在注册登录过程中把app置于后台打开系统计算器应用计算数字后返回app能否继续过程
    def test_onekeyreg_login_019(self):
        enter_onekeyreg_login(self)  # 清空后台到打开 一键注册登录 页面
        self.page.custom_functions.click_home_key()  # 点击home键返回桌面
        self.page.custom_functions.calculator()  # 计算数字并返回桌面
        self.page.custom_functions.click_all_apps_handle()  # 进入桌面抽屉
        self.page.custom_functions.click_start_app()  # 启动app
        print('\n-------- 注册 - 一键注册登录 模块测试完成 --------')
        assert self.page.onekeyreg_login.is_element_exist(self.page.onekeyreg_login.onekeyreg_login_button) is True
