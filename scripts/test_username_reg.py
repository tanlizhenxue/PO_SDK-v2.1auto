import os
import time

from base.base_driver import init_driver
from page.page import Page


# 运行 清空后台全部任务 - 打开app - 进入 用户名注册 页面的流程
def enter_username_reg(self):
    self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
    self.page.home.click_login()  # 点击 登录 按钮
    for i in range(0, 2):
        if self.page.onekeyreg_login.is_element_exist(self.page.onekeyreg_login.onekeyreg_login_button, 1) is True:
            self.page.onekeyreg_login.click_other_reg()  # 点击 其他方式注册登录 按钮
            self.page.manually_login.click_fast_reg()  # 点击 快速注册 按钮
            self.page.phonenum_reg.click_username_reg()  # 点击 用户名注册 选项
            break
        elif self.page.auto_login.is_element_exist(self.page.auto_login.auto_login_title, 1) is True or \
                self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True:
            self.page.realname.pass_auth()  # 通过认证实名认证
            self.page.home.click_logout()  # 点击 登出 按钮
        else:
            print(f'error: 没有打开 一键注册登录 页面, 第{i + 1}次重试---------------')  # 再次重试打开
            self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
            self.page.home.click_login()  # 点击 登录 按钮


# 运行用户名注册后 关闭实名认证页面 - 登出 的流程
def close_realname_logout(self):
    self.page.realname.pass_auth()  # 通过认证实名认证
    self.page.home.click_logout()  # 点击 登出 按钮


# 运行用户名注册后 关闭实名认证页面 - 登出 - 用户名注册 的流程
def logout_username_reg(self):
    close_realname_logout(self)  # 关闭实名认证页面 - 登出
    self.page.onekeyreg_login.click_other_reg()  # 点击 其他方式给注册登录 按钮
    self.page.manually_login.click_fast_reg()  # 点击 快速注册 按钮
    self.page.phonenum_reg.click_username_reg()  # 点击 用户名注册 按钮


class TestUsernameReg:

    def setup(self):
        self.driver = init_driver(no_reset=True)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    # 54 进入用户名注册窗口，点击左上角返回按钮，是否可以返回到上一个页面
    def test_username_reg_054(self):
        print('\n\n-------- 正在测试 注册 - 用户名注册 模块 --------')
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.click_back_username_reg()
        assert self.page.phonenum_reg.find_element(self.page.phonenum_reg.phonenum_reg_title)

    # 55 在不输入任何信息下，账号输入框和密码输入框内是否有灰色提示文字
    # 69 用户名注册 页面是否有错别字，是否简洁易懂
    # 70 用户名注册 页面的设计风格是否与UI的设计风格统一
    def test_username_reg_055_069_070(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/username_reg_ui.png')
        assert self.page.username_reg.get_text(self.page.username_reg.username_inputbox) == "账号，数字和字母组合"
        assert self.page.username_reg.get_text(self.page.username_reg.password_inputbox) == "密码，6-20个字符"

    # 56 立即注册 按钮默认是否为禁用状态
    def test_username_reg_056(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        assert self.page.username_reg.get_enabled(self.page.username_reg.now_reg_button) == "false"

    # 57 当账号和密码输入都是符合规则的内容时，勾选 用户服务协议，立即注册 按钮是否为可用状态
    def test_username_reg_057(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_num_count(8))
        assert self.page.username_reg.get_enabled(self.page.username_reg.now_reg_button) == "true"

    # 58 当账号和密码输入都是符合规则的内容时，不勾选 用户服务协议，立即注册 按钮是否为可用状态
    def test_username_reg_058(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.user_server.click_checkbox_user_service()
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_num_count(8))
        assert self.page.username_reg.get_enabled(self.page.username_reg.now_reg_button) == "false"

    # 59 账号和密码输入框分别输入的 符合规则 时的样式是否如备注图所示
    # 60 账号和密码输入框分别输入的 不符合规则 时的样式是否如备注图所示
    # 61 账号输入正确，在输入密码没有移开输入焦点时，是否明文显示密码
    # 62 账号输入正确，在输入密码时移开输入焦点是否掩码显示
    def test_username_reg_059_060_061_062(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.clear_username()
        self.page.username_reg.input_username(self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_username_inputbox()
        time.sleep(0.5)
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/username_reg_用户名输入框输入的符合规则时的样式.png')
        self.page.username_reg.clear_password()
        self.page.username_reg.input_password(self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_password_inputbox()
        time.sleep(0.5)
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/username_reg_密码输入框输入的符合规则时的样式'
                                                                  '并查看密码输入框是否明文显示密码.png')
        self.page.username_reg.clear_username()
        self.page.username_reg.input_username(self.page.custom_functions.letters_num_count(2))
        self.page.username_reg.click_username_inputbox()
        time.sleep(0.5)
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/username_reg_用户名输入框输入的不符合规则时的样式'
                                                                  '并查看密码输入框是否已掩码显示.png')
        self.page.username_reg.clear_password()
        self.page.username_reg.input_password(self.page.custom_functions.letters_num_count(2))
        self.page.username_reg.click_password_inputbox()
        time.sleep(0.5)
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/username_reg_密码输入框输入的不符合规则时的样式.png')

    # 63 输入符合规则的账号和密码后点击 立即注册 按钮，账号和密码输入框、勾选框、立即注册按钮 和 返回< 按钮 是否为禁用状态，
    # 立即注册 按钮文字是否已修改为 正在注册...
    def test_username_reg_063(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        time.sleep(0.1)
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/username_reging.png')
        close_realname_logout(self)

    # 64 注册成功后是否显示 注册成功 页面
    def test_username_reg_064(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.find_element(self.page.username_reg.username_reg_success_title)
        close_realname_logout(self)

    # 65 注册后的用户名(不是昵称)和输入的用户名是否一致
    # 66 显示 注册成功 页面后，且当前游戏配置启用实名认证配置，是否显示 正在启动实名认证，请稍等... ，
    # 是否能够在3秒后关闭注册成功画面，显示实名认证页面
    def test_username_reg_065_066(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        username_065 = self.page.custom_functions.letters_num_count(8)
        self.page.username_reg.input_username_password(username_065, self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.get_text(self.page.username_reg.account) == username_065
        assert self.page.username_reg.find_element(self.page.username_reg.starting_realname_auth)
        assert self.page.realname.find_element(self.page.realname.realname_auth_title)
        close_realname_logout(self)

    # 67 进入游戏时，是否能够根据配置显示或隐藏悬浮球
    def test_username_reg_067(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        self.page.realname.pass_auth()
        time.sleep(0.5)
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './ui/username_reg_是否能够根据配置显示或隐藏悬浮球.png')
        self.page.home.click_logout()

    # 68 输入已经注册过的账号点击 立即注册 是否有相关提示
    def test_username_reg_068(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password('17605113956', 'hzhy2020')
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.get_toast_text("账号只能为数字加字母或字符的组合") == "账号只能为数字加字母或字符的组合"
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title) is False

    # 71 在注册过程中把app置于后台打开系统计算器应用计算数字后返回app能否继续过程
    def test_username_reg_071(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.custom_functions.calculator()
        self.page.custom_functions.click_all_apps_handle()
        self.page.custom_functions.click_start_app()
        assert self.page.username_reg.find_element(self.page.username_reg.username_reg_title)
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.find_element(self.page.username_reg.username_reg_success_title)
        close_realname_logout(self)

    # 72 输入符合规则的帐号，密码输入框不输入任何信息，是否可以注册
    def test_username_reg_072(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8), "")
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 73 输入符合规则的帐号，密码输入框输入 6位数字 ，是否可以注册
    def test_username_reg_073(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.num_count(6))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True
        close_realname_logout(self)

    # 74 输入符合规则的帐号，密码输入框输入 6位字母，是否可以注册
    def test_username_reg_074(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_count(6))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True
        close_realname_logout(self)

    # 75 输入符合规则的帐号，密码输入框输入 6位键盘字符 ，是否可以注册
    def test_username_reg_075(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.character_count(6))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True
        close_realname_logout(self)

    # 76 输入符合规则的帐号，密码输入框输入 20位数字 ，是否可以注册
    def test_username_reg_076(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.num_count(20))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True
        close_realname_logout(self)

    # 77 输入符合规则的帐号，密码输入框输入 20位字母 ，是否可以注册
    def test_username_reg_077(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_count(20))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True
        close_realname_logout(self)

    # 78 输入符合规则的帐号，密码输入框输入 20位键盘字符 ，是否可以注册
    def test_username_reg_078(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.character_count(20))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True
        close_realname_logout(self)

    # 79 输入符合规则的帐号，密码输入框输入 6位 字母+数字的组合 ，是否可以注册
    def test_username_reg_079(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_num_count(6))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True
        close_realname_logout(self)

    # 80 输入符合规则的帐号，密码输入框输入 6位 数字+键盘字符的组合 ，是否可以注册
    def test_username_reg_080(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.num_character_count(6))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True
        close_realname_logout(self)

    # 81 输入符合规则的帐号，密码输入框输入 6位 字母+键盘字符的组合 ，是否可以注册
    def test_username_reg_081(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_character_count(6))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True
        close_realname_logout(self)

    # 82 输入符合规则的帐号，密码输入框输入 20位 字母+数字的组合 ，是否可以注册
    def test_username_reg_082(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_num_count(20))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True
        close_realname_logout(self)

    # 83 输入符合规则的帐号，密码输入框输入 20位 数字+键盘字符的组合 ，是否可以注册
    def test_username_reg_083(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.num_character_count(20))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True
        close_realname_logout(self)

    # 84 输入符合规则的帐号，密码输入框输入 20位 字母+键盘字符的组合 ，是否可以注册
    def test_username_reg_084(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_character_count(20))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True
        close_realname_logout(self)

    # 85 输入符合规则的帐号，密码输入框输入 6位 字母+数字+键盘字符的组合 ，是否可以注册
    def test_username_reg_085(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_num_character_count(6))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True
        close_realname_logout(self)

    # 86 输入符合规则的帐号，密码输入框输入 20位 字母+数字+键盘字符的组合 ，是否可以注册
    def test_username_reg_086(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_num_character_count(20))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True
        close_realname_logout(self)

    # 87 输入符合规则的帐号，密码输入框输入 5位数字 ，是否可以注册
    def test_username_reg_087(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.num_count(5))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 88 输入符合规则的帐号，密码输入框输入 5位字母 ，是否可以注册
    def test_username_reg_088(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_count(5))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 89 输入符合规则的帐号，密码输入框输入 5位键盘字符 ，是否可以注册
    def test_username_reg_089(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.character_count(5))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 90 输入符合规则的帐号，密码输入框输入 21位数字 ，是否可以注册
    def test_username_reg_090(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.num_count(21))
        assert len(self.page.username_reg.get_text(self.page.username_reg.password_inputbox)) == 20
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True

    # 91 输入符合规则的帐号，密码输入框输入 21位字母 ，是否可以注册
    def test_username_reg_091(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_count(21))
        assert len(self.page.username_reg.get_text(self.page.username_reg.password_inputbox)) == 20
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True

    # 92 输入符合规则的帐号，密码输入框输入 21位键盘字符 ，是否可以注册
    def test_username_reg_092(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.character_count(21))
        assert len(self.page.username_reg.get_text(self.page.username_reg.password_inputbox)) == 20
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True

    # 93 输入符合规则的帐号，密码输入框输入 5位 字母+数字的组合 ，是否可以注册
    def test_username_reg_093(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_num_count(5))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 94 输入符合规则的帐号，密码输入框输入 5位 数字+键盘字符的组合 ，是否可以注册
    def test_username_reg_094(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.num_character_count(5))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 95 输入符合规则的帐号，密码输入框输入 5位 字母+键盘字符的组合 ，是否可以注册
    def test_username_reg_095(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_character_count(5))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 96 输入符合规则的帐号，密码输入框输入 21位 字母+数字的组合 ，是否可以注册
    def test_username_reg_096(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_num_count(21))
        assert len(self.page.username_reg.get_text(self.page.username_reg.password_inputbox)) == 20
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True

    # 97 输入符合规则的帐号，密码输入框输入 21位 数字+键盘字符的组合 ，是否可以注册
    def test_username_reg_097(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.num_character_count(21))
        assert len(self.page.username_reg.get_text(self.page.username_reg.password_inputbox)) == 20
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True

    # 98 输入符合规则的帐号，密码输入框输入 21位 字母+键盘字符的组合 ，是否可以注册
    def test_username_reg_098(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_character_count(21))
        assert len(self.page.username_reg.get_text(self.page.username_reg.password_inputbox)) == 20
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True

    # 99 输入符合规则的帐号，密码输入框输入 5位 字母+数字+键盘字符的组合 ，是否可以注册
    def test_username_reg_099(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_num_character_count(5))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 100 输入符合规则的帐号，密码输入框输入 21位 字母+数字+键盘字符的组合 ，是否可以注册
    def test_username_reg_100(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_num_character_count(21))
        assert len(self.page.username_reg.get_text(self.page.username_reg.password_inputbox)) == 20
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True

    # # 101 输入符合规则的帐号，密码输入正确后再添加一个空格 ，是否可以注册
    def test_username_reg_101(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_num_character_count(8) + " ")
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 102 输入符合规则的密码，账号输入框不输入任何信息，是否可以注册
    def test_username_reg_102(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password("",
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 103 输入符合规则的密码，账号输入框输入 6位数字，是否可以注册
    def test_username_reg_103(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.num_count(6),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 104 输入符合规则的密码，账号输入框输入 6位字母，是否可以注册
    def test_username_reg_104(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_count(6),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 105 输入符合规则的密码，账号输入框输入 6位键盘字符，是否可以注册
    def test_username_reg_105(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.character_count(6),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 106 输入符合规则的密码，账号输入框输入 20位数字，是否可以注册
    def test_username_reg_106(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.num_count(20),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 107 输入符合规则的密码，账号输入框输入 20位字母，是否可以注册
    def test_username_reg_107(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_count(20),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 108 输入符合规则的密码，账号输入框输入 20位键盘字符，是否可以注册
    def test_username_reg_108(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.character_count(20),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 109 输入符合规则的密码，账号输入框输入 6位 字母+数字的组合，是否可以注册	是
    def test_username_reg_109(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(6),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True

    # 110 输入符合规则的密码，账号输入框输入 6位 数字+键盘字符的组合，是否可以注册	是
    def test_username_reg_110(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.num_character_count(6),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True

    # 111 输入符合规则的密码，账号输入框输入 6位 字母+键盘字符的组合，是否可以注册
    def test_username_reg_111(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_character_count(6),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 112 输入符合规则的密码，账号输入框输入 20位 字母+数字的组合，是否可以注册	是
    def test_username_reg_112(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(20),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True

    # 113 输入符合规则的密码，账号输入框输入 20位 数字+键盘字符的组合，是否可以注册
    def test_username_reg_113(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.num_character_count(20),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True

    # 114 输入符合规则的密码，账号输入框输入 20位 字母+键盘字符的组合，是否可以注册
    def test_username_reg_114(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_character_count(20),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 115 输入符合规则的密码，账号输入框输入 6位 字母+数字+键盘字符的组合，是否可以注册
    def test_username_reg_115(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_character_count(6),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True

    # 116 输入符合规则的密码，账号输入框输入 20位 字母+数字+键盘字符的组合，是否可以注册
    def test_username_reg_116(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_character_count(20),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True

    # 117 输入符合规则的密码，账号输入框输入 5位数字，是否可以注册
    def test_username_reg_117(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.num_count(5),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 118 输入符合规则的密码，账号输入框输入 5位字母，是否可以注册
    def test_username_reg_118(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_count(5),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 119 输入符合规则的密码，账号输入框输入 5位键盘字符，是否可以注册
    def test_username_reg_119(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.character_count(5),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 120 输入符合规则的密码，账号输入框输入 21位数字，是否可以注册
    def test_username_reg_120(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.num_count(21),
                                                       self.page.custom_functions.letters_num_count(8))
        assert len(self.page.username_reg.get_text(self.page.username_reg.username_inputbox)) == 20
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 121 输入符合规则的密码，账号输入框输入 21位字母，是否可以注册
    def test_username_reg_121(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_count(21),
                                                       self.page.custom_functions.letters_num_count(8))
        assert len(self.page.username_reg.get_text(self.page.username_reg.username_inputbox)) == 20
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 122 输入符合规则的密码，账号输入框输入 21位键盘字符，是否可以注册
    def test_username_reg_122(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.character_count(21),
                                                       self.page.custom_functions.letters_num_count(8))
        assert len(self.page.username_reg.get_text(self.page.username_reg.username_inputbox)) == 20
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 123 输入符合规则的密码，账号输入框输入 5位 字母+数字的组合，是否可以注册
    def test_username_reg_123(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(5),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 124 输入符合规则的密码，账号输入框输入 5位 数字+键盘字符的组合，是否可以注册
    def test_username_reg_124(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.num_character_count(5),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 125 输入符合规则的密码，账号输入框输入 5位 字母+键盘字符的组合，是否可以注册
    def test_username_reg_125(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_character_count(5),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 126 输入符合规则的密码，账号输入框输入 21位 字母+数字的组合，是否可以注册
    def test_username_reg_126(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(21),
                                                       self.page.custom_functions.letters_num_count(8))
        assert len(self.page.username_reg.get_text(self.page.username_reg.username_inputbox)) == 20
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True

    # 127 输入符合规则的密码，账号输入框输入 21位 数字+键盘字符的组合，是否可以注册
    def test_username_reg_127(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.num_character_count(21),
                                                       self.page.custom_functions.letters_num_count(8))
        assert len(self.page.username_reg.get_text(self.page.username_reg.username_inputbox)) == 20
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True

    # 128 输入符合规则的密码，账号输入框输入 21位 字母+键盘字符的组合，是否可以注册
    def test_username_reg_128(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_character_count(21),
                                                       self.page.custom_functions.letters_num_count(8))
        assert len(self.page.username_reg.get_text(self.page.username_reg.username_inputbox)) == 20
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 129 输入符合规则的密码，账号输入框输入 5位 字母+数字+键盘字符的组合，是否可以注册
    def test_username_reg_129(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_character_count(5),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False

    # 130 输入符合规则的密码，账号输入框输入 21位 字母+数字+键盘字符的组合，是否可以注册
    def test_username_reg_130(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_character_count(21),
                                                       self.page.custom_functions.letters_num_count(8))
        assert len(self.page.username_reg.get_text(self.page.username_reg.username_inputbox)) == 20
        self.page.username_reg.click_now_reg()
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is True

    # 131 输入符合规则的密码，账号输入符合规则后再添加一个空格 ，是否可以注册
    def test_username_reg_131(self):
        enter_username_reg(self)  # 进入 用户名注册 页面
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8) + " ",
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        print('\n-------- 注册 - 用户名注册 模块测试完成 --------')
        assert self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_success_title,
                                                       timeout=1) is False
