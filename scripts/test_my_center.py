import os
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


# 运行 清空后台 - 打开app - 进入 个人中心 页面的流程(随机生成账号)
def enter_my_center(self):
    # self.driver.switch_to.context("NATIVE_APP")  # 后续查找元素时在原生应用中查找
    self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
    self.page.home.click_login()  # 点击 登录 按钮
    for i in range(0, 3):
        if self.page.onekeyreg_login.is_element_exist(self.page.onekeyreg_login.onekeyreg_login_button, 1
                                                      ) is True:
            break
        elif self.page.auto_login.is_element_exist(self.page.auto_login.auto_login_title, 1) is True or \
                self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True:
            self.page.realname.pass_auth()  # 通过认证实名认证
            self.page.home.click_logout()
        else:
            print(f'error: 没有打开 一键注册登录 页面, 第{i + 1}次重试---------------')  # 再次重试打开
            self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
            self.page.home.click_login()  # 点击 登录 按钮
    self.page.onekeyreg_login.click_onekeyreg_login()  # 点击 一键注册登录 按钮
    self.page.onekeyreg_login.click_enter_game()  # 点击 进入游戏 按钮
    self.page.realname.pass_auth()  # 通过认证实名认证
    time.sleep(self.page.float_ball.fold_time)  # 悬浮球贴边的时间
    self.page.float_ball.click_float_ball_fold()  # 点击已经贴边的 悬浮球 , 然后会自动展开
    self.page.float_ball.click_me()  # 点击悬浮球中的 我的
    # self.driver.switch_to.context("WEBVIEW_com.hzhy.sdk")  # 后续查找元素时在 WEBVIEW_com.hzhy.sdk 程序中查找


# 运行 清空后台 - 打开app - 进入 个人中心 页面的流程(登录已绑定手机账号)
def enter_my_center_bound_phonenum(self, args):
    username_phonenum = args["username_phonenum"]
    password = args["password"]
    self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
    self.page.home.click_login()  # 点击 登录 按钮
    for i in range(0, 2):
        if self.page.onekeyreg_login.is_element_exist(self.page.onekeyreg_login.onekeyreg_login_button, 1
                                                      ) is True:
            break
        elif self.page.auto_login.is_element_exist(self.page.auto_login.auto_login_title, 1) is True or \
                self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True:
            self.page.realname.pass_auth()  # 通过认证实名认证
            self.page.home.click_logout()
            break
        else:
            print(f'error: 没有打开 一键注册登录 页面, 第{i + 1}次重试---------------')  # 再次重试打开
            self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
            self.page.home.click_login()  # 点击 登录 按钮
    self.page.onekeyreg_login.click_other_reg()
    self.page.manually_login.input_username_phonenum_password(username_phonenum, password)
    self.page.manually_login.click_now_login()
    self.page.realname.pass_auth()  # 通过认证实名认证
    time.sleep(self.page.float_ball.fold_time)  # 悬浮球贴边的时间
    self.page.float_ball.click_float_ball_fold()
    self.page.float_ball.click_me()


# 运行 清空后台 - 打开app - 进入 忘记密码(找回密码) 页面的流程
def enter_retrieve_password(self):
    self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
    self.page.home.click_login()  # 点击 登录 按钮
    for i in range(0, 2):
        if self.page.onekeyreg_login.is_element_exist(self.page.onekeyreg_login.onekeyreg_login_button, 1
                                                      ) is True:
            break
        elif self.page.auto_login.is_element_exist(self.page.auto_login.auto_login_title, 1) is True or \
                self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True:
            self.page.realname.pass_auth()  # 通过认证实名认证
            self.page.home.click_logout()
            break
        else:
            print(f'error: 没有打开 一键注册登录 页面, 第{i + 1}次重试---------------')  # 再次重试打开
            self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
            self.page.home.click_login()  # 点击 登录 按钮
    self.page.onekeyreg_login.click_other_reg()
    self.page.manually_login.click_forget_password()


# 运行 清空后台 - 打开app - 进入 实名认证 页面的流程
def enter_realname(self):
    self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
    self.page.home.click_login()  # 点击 登录 按钮
    for i in range(0, 3):
        if self.page.onekeyreg_login.is_element_exist(self.page.onekeyreg_login.onekeyreg_login_button, 1
                                                      ) is True:
            self.page.onekeyreg_login.click_onekeyreg_login()
            self.page.onekeyreg_login.click_enter_game()
            break
        elif self.page.auto_login.is_element_exist(self.page.auto_login.auto_login_title, 1) is True or \
                self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True:
            break
        else:
            print(f'error: 没有打开 一键注册登录 页面, 第{i + 1}次重试---------------')  # 再次重试打开
            self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
            self.page.home.click_login()  # 点击 登录 按钮


class TestMyCenter:

    def setup(self):
        self.driver = init_driver(no_reset=True)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    # 01 从悬浮球中点击 我的 能否进入个人中心页面
    def test_my_center_001(self):
        print('\n\n-------- 正在测试 个人中心 - 修改昵称 模块 --------')
        enter_my_center(self)  # 进入 个人中心 页面
        assert self.page.my_center.is_element_exist(self.page.my_center.my_center_title) is True

    # 03 个人中心相关页面使用 H5页面，通过视图容器载入，查看容器的标题栏部分是否如备注图所示。个人中心目前只支持竖屏显示
    # 04 当用户没有设置头像时是否显示默认的头像图片, 用户昵称和用户ID展示是否如备注图所示
    # 05 在个人中心首页时，左侧的“<”是否不显示，如备注图所示
    # 06 个人中心页面是否有错别字，是否简洁易懂
    # 07 个人中心页面的设计风格是否与UI的设计风格统一
    def test_my_center_003_004_005_006_007(self):
        enter_my_center(self)  # 进入 个人中心 页面
        if self.page.my_center.is_element_exist(self.page.my_center.my_center_title) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/my_center_ui01.png")
        else:
            assert 0

    # 08 点击右上角的 关闭× 按钮是否能够关闭个人中心
    def test_my_center_008(self):
        enter_my_center(self)  # 进入 个人中心 页面
        self.page.my_center.click_close_my_center()
        time.sleep(0.2)  # 点击 关闭× 后个人中心页面可能关闭的比较慢, 所以需要等待一下
        assert self.page.my_center.is_element_exist(self.page.my_center.my_center_title, 2) is False

    # 09 在 个人中心 页面中，把app置于后台打开系统计算器应用计算数字后返回app能否继续
    def test_my_center_009(self):
        enter_my_center(self)  # 进入 个人中心 页面
        self.page.custom_functions.calculator()
        self.page.custom_functions.click_all_apps_handle()
        self.page.custom_functions.click_start_app()
        assert self.page.my_center.is_element_exist(self.page.my_center.my_center_title) is True

    # 10 点击个人中心中的 修改昵称 菜单，能否进入 修改昵称 页面
    def test_my_center_010(self):
        enter_my_center(self)  # 进入 个人中心 页面
        self.page.my_center.click_revise_nickname()  # 进入修改昵称页面
        assert self.page.my_center.is_element_exist(self.page.my_center.revise_nickname_title) is True

    # 11 清空昵称输入框后不输入任何信息，点击 确定 按钮，能否修改成功
    def test_my_center_011(self):
        enter_my_center(self)  # 进入 个人中心 页面
        self.page.my_center.click_revise_nickname()  # 进入修改昵称页面
        self.page.my_center.clear_nickname()  # 清空昵称输入框
        self.page.my_center.click_sure_revise_nickname()  # 点击 确定 按钮
        assert self.page.my_center.is_element_exist(self.page.my_center.revise_nickname_success_title, 0.5) is False

    # 12 在昵称输入框输入3个字符，点击 确定 按钮，能否修改成功
    def test_my_center_012(self):
        enter_my_center(self)  # 进入 个人中心 页面
        self.page.my_center.click_revise_nickname()  # 进入修改昵称页面
        self.page.my_center.clear_nickname()  # 清空昵称输入框
        self.page.my_center.input_nickname(self.page.custom_functions.letters_num_count(3))
        self.page.my_center.click_sure_revise_nickname()  # 点击 确定 按钮
        assert self.page.my_center.is_element_exist(self.page.my_center.revise_nickname_success_title, 0.5) is False

    # 13 在昵称输入框输入11个字符，点击 确定 按钮，能否修改成功
    def test_my_center_013(self):
        enter_my_center(self)  # 进入 个人中心 页面
        self.page.my_center.click_revise_nickname()  # 进入修改昵称页面
        self.page.my_center.clear_nickname()  # 清空昵称输入框
        self.page.my_center.input_nickname(self.page.custom_functions.letters_num_count(11))
        self.page.my_center.click_sure_revise_nickname()  # 点击 确定 按钮
        assert self.page.my_center.is_element_exist(self.page.my_center.revise_nickname_success_title, 0.5) is False

    # 14 在昵称输入框输入4个字符，点击 确定 按钮，能否修改成功
    def test_my_center_014(self):
        enter_my_center(self)  # 进入 个人中心 页面
        self.page.my_center.click_revise_nickname()  # 进入修改昵称页面
        self.page.my_center.clear_nickname()  # 清空昵称输入框
        self.page.my_center.input_nickname(self.page.custom_functions.letters_num_count(4))
        self.page.my_center.click_sure_revise_nickname()  # 点击 确定 按钮
        assert self.page.my_center.is_element_exist(self.page.my_center.revise_nickname_success_title, 0.5) is True

    # 15 在昵称输入框输入10个字符，点击 确定 按钮，能否修改成功
    def test_my_center_015(self):
        enter_my_center(self)  # 进入 个人中心 页面
        self.page.my_center.click_revise_nickname()  # 进入修改昵称页面
        self.page.my_center.clear_nickname()  # 清空昵称输入框
        self.page.my_center.input_nickname(self.page.custom_functions.letters_num_count(10))
        self.page.my_center.click_sure_revise_nickname()  # 点击 确定 按钮
        assert self.page.my_center.is_element_exist(self.page.my_center.revise_nickname_success_title, 0.5) is True

    # 16 在昵称输入框输入4个空格，点击 确定 按钮，能否修改成功
    def test_my_center_016(self):
        enter_my_center(self)  # 进入 个人中心 页面
        self.page.my_center.click_revise_nickname()  # 进入修改昵称页面
        self.page.my_center.clear_nickname()  # 清空昵称输入框
        self.page.my_center.input_nickname(" " + " " + " " + " ")
        self.page.my_center.click_sure_revise_nickname()  # 点击 确定 按钮
        assert self.page.my_center.is_element_exist(self.page.my_center.revise_nickname_success_title, 0.5) is False

    # 17 输入一个已经存在的昵称，点击 确定 按钮，在昵称输入框下方是否有提示语（以该句提示语为准）
    # 该昵称已经被占用了，请换一个吧~ ，示例如备注图所示
    def test_my_center_017(self):
        enter_my_center(self)  # 进入 个人中心 页面
        nickname = self.page.custom_functions.letters_num_count(6)
        for i in range(0, 2):
            if self.page.my_center.is_element_exist(self.page.my_center.revise_nickname_success_title, 1) is True:
                self.page.my_center.click_close_revise_nickname_success()
            else:
                pass
            self.page.my_center.click_revise_nickname()  # 点击 修改昵称 按钮
            self.page.my_center.clear_nickname()  # 清空昵称输入框
            self.page.my_center.input_nickname(nickname)
            self.page.my_center.click_sure_revise_nickname()  # 点击 确定 按钮
        assert self.page.my_center.is_element_exist(self.page.my_center.revise_nickname_success_title, 1) is False
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/revise_nickname_该昵称已经被占用了，请换一个吧~.png")

    # 18 昵称修改成功后返回个人中心页面, 查看昵称是否和修改的一致
    def test_my_center_018(self):
        enter_my_center(self)  # 进入 个人中心 页面
        global nickname
        nickname = self.page.custom_functions.letters_num_count(6)
        self.page.my_center.click_revise_nickname()  # 进入修改昵称页面
        self.page.my_center.clear_nickname()  # 清空昵称输入框
        self.page.my_center.input_nickname(nickname)
        if self.page.my_center.get_text(self.page.my_center.nickname_inputbox) != "":
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/revise_nickname_昵称修改1前.png")
        else:
            assert 0
        self.page.my_center.click_sure_revise_nickname()  # 点击 确定 按钮
        self.page.my_center.click_close_revise_nickname_success()
        if self.page.my_center.is_element_exist(self.page.my_center.my_center_title) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/revise_nickname_昵称修改2后.png")
        else:
            print(f"\nerror018: 修改昵称为{nickname}时没有修改成功")
            assert 0

    # 19 修改昵称页面是否有错别字，是否简洁易懂
    # 20 修改昵称页面的设计风格是否与UI的设计风格统一
    def test_my_center_019_020(self):
        enter_my_center(self)  # 进入 个人中心 页面
        self.page.my_center.click_revise_nickname()
        if self.page.my_center.is_element_exist(self.page.my_center.revise_nickname_title) is True and \
                self.page.my_center.is_element_exist(self.page.my_center.nickname_sure_button) is True:
            # 输入框为空时的ui
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/revise_nickname_ui01.png")
            self.page.my_center.click_sure_revise_nickname()
            time.sleep(0.5)
            # 输入框不输入时点击 确定 按钮时的ui
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/revise_nickname_ui02.png")
        else:
            assert 0
        self.page.my_center.clear_nickname()
        self.page.my_center.input_nickname(self.page.custom_functions.letters_count(2))
        self.page.my_center.click_sure_revise_nickname()
        time.sleep(0.5)
        # 输入框输入格式错误时的ui
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/revise_nickname_ui03.png")
        nickname = self.page.custom_functions.letters_num_count(6)
        self.page.my_center.clear_nickname()
        self.page.my_center.input_nickname(nickname)
        self.page.my_center.click_sure_revise_nickname()
        if self.page.my_center.is_element_exist(self.page.my_center.revise_nickname_success_title) is True:
            # 输入框输入格式正确时的ui
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/revise_nickname_ui04.png")
        else:
            print(f"\nerror019_020: 修改昵称为{nickname}时没有修改成功")
            assert 0
        self.page.my_center.click_close_revise_nickname_success()
        self.page.my_center.click_revise_nickname()
        self.page.my_center.input_nickname(nickname)
        self.page.my_center.click_sure_revise_nickname()
        time.sleep(1)
        # 输入框输入已存在的昵称时的ui
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/revise_nickname_ui05.png")

    # 21 在修改昵称过程中把app置于后台打开系统计算器应用计算数字后返回app能否继续
    def test_my_center_021(self):
        enter_my_center(self)  # 进入 个人中心 页面
        self.page.my_center.click_revise_nickname()
        self.page.custom_functions.calculator()
        self.page.custom_functions.click_all_apps_handle()
        self.page.custom_functions.click_start_app()
        assert self.page.my_center.is_element_exist(self.page.my_center.revise_nickname_title) is True

    # 26 如果当前用户未绑定手机，点击 登录密码 菜单项后，是否能够弹出 绑定手机后才能修改密码 提示, 如备注图所示
    def test_my_center_026(self):
        print('\n-------- 正在测试 个人中心 - 登录密码 模块 --------')
        enter_my_center(self)  # 进入 个人中心 页面
        self.page.my_center.click_login_password()  # 点击登录密码
        assert self.page.my_center.is_element_exist(self.page.my_center.unbound_phonenum_title) is True

    # 27 点击 登录密码 选项后，弹出未绑定手机的提示, 点击 确定 按钮后能否进入 绑定手机 页面
    def test_my_center_027(self):
        enter_my_center(self)  # 进入 个人中心 页面
        self.page.my_center.click_login_password()  # 点击登录密码
        self.page.my_center.click_sure_unbound_phonenum()
        assert self.page.my_center.is_element_exist(self.page.my_center.bound_phonenum_title) is True

    # 29 当用户已绑定手机时, 点击 登录密码 菜单项后是否会够弹出 修改密码 页面
    @pytest.mark.parametrize("args", analyze_file("my_center.yaml", "test_my_center"))
    def test_my_center_029(self, args):
        enter_my_center_bound_phonenum(self, args)
        self.page.my_center.click_login_password()
        assert self.page.my_center.is_element_exist(self.page.my_center.revise_password_title) is True

    # 30 当用户已绑定手机时, 点击 登录密码 菜单项后弹出 修改密码 页面, 点击 取消 按钮是否只关闭了 修改密码 页面
    @pytest.mark.parametrize("args", analyze_file("my_center.yaml", "test_my_center"))
    def test_my_center_030(self, args):
        enter_my_center_bound_phonenum(self, args)
        self.page.my_center.click_login_password()
        self.page.my_center.click_cancel_revise_password()
        assert self.page.my_center.is_element_exist(self.page.my_center.revise_password_title, 1) is False

    # 32 当用户已绑定手机时, 点击 登录密码 菜单项后弹出 修改密码 页面, 点击 继续 按钮是否进入 输入短信验证码 页面
    @pytest.mark.parametrize("args", analyze_file("my_center.yaml", "test_my_center"))
    def test_my_center_032(self, args):
        enter_my_center_bound_phonenum(self, args)
        self.page.my_center.click_login_password()
        self.page.my_center.click_continue_revise_password()
        assert self.page.my_center.is_element_exist(
            self.page.my_center.input_msg_code_title_revise_password) is True \
               or self.page.image_auth_code.is_element_exist(
            self.page.image_auth_code.image_auth_code_title) is True

    # 34 在 输入短信验证码 页面手机号码中间4位是否掩码显示
    @pytest.mark.parametrize("args", analyze_file("my_center.yaml", "test_my_center"))
    def test_my_center_034(self, args):
        enter_my_center_bound_phonenum(self, args)
        if self.page.my_center.is_element_exist(self.page.my_center.login_password_button) is True:
            self.page.my_center.click_login_password()
        else:
            print("error_034: 没有进入个人中心页面")
            assert 0
        self.page.my_center.click_continue_revise_password()
        if self.page.my_center.is_element_exist(self.page.my_center.input_msg_code_title_revise_password) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + "." + os.sep + "ui" + os.sep +
                                               "revise_password_手机号中间四位掩码显示.png")
        else:
            assert 0

    # 35 进入 输入短信验证码 页面后输入框右侧是否进入60s倒计时, 并且是不可点击状态, 如备注图所示
    # 59 修改密码页面是否有错别字，是否简洁易懂
    # 60 修改密码页面的设计风格是否与UI的设计风格统一
    @pytest.mark.parametrize("args", analyze_file("my_center.yaml", "test_my_center"))
    def test_my_center_035_059_060(self, args):
        enter_my_center_bound_phonenum(self, args)
        self.page.my_center.click_login_password()
        self.page.my_center.click_continue_revise_password()
        if self.page.my_center.is_element_exist(self.page.my_center.input_msg_code_title_revise_password) is True:
            time.sleep(1)
            self.driver.get_screenshot_as_file(os.getcwd() + "." + os.sep + "ui" + os.sep +
                                               "revise_password_进入60s倒计时.png")
        else:
            assert 0

    # 36 60s倒计时结束后该按钮是否可以点击, 点击后在60s内能否收到验证码
    @pytest.mark.parametrize("args", analyze_file("my_center.yaml", "test_my_center"))
    def test_my_center_036(self, args):
        enter_my_center_bound_phonenum(self, args)
        self.page.my_center.click_login_password()
        self.page.my_center.click_continue_revise_password()
        if self.page.my_center.is_element_exist(self.page.my_center.input_msg_code_title_revise_password) is True:
            self.page.custom_functions.time_sleep(60, self.page.my_center.revise_password_title)  # 等待60s
            assert self.page.my_center.get_enabled(self.page.my_center.retry_msg_code_button_revise_password
                                                   ) == "true"
        else:
            assert 0

    # 37 进入 输入短信验证码页面 后, 点击左上角的 返回< 按钮能否返回 个人中心 页面
    @pytest.mark.parametrize("args", analyze_file("my_center.yaml", "test_my_center"))
    def test_my_center_037(self, args):
        enter_my_center_bound_phonenum(self, args)
        self.page.my_center.click_login_password()
        self.page.my_center.click_continue_revise_password()
        if self.page.my_center.is_element_exist(self.page.my_center.image_code_title, 2) is True:
            self.page.my_center.click_close_image_code()
            self.page.my_center.click_back_input_msg_code_revise_password()
            assert self.page.my_center.is_element_exist(self.page.my_center.my_center_title) is True
        else:
            self.page.my_center.click_back_input_msg_code_revise_password()
            assert self.page.my_center.is_element_exist(self.page.my_center.my_center_title) is True

    # 38 在 短信验证码 输入框中不输入或输入无效的短信验证码后, 点击 下一步 能否进行下一步操作
    @pytest.mark.parametrize("args", analyze_file("my_center.yaml", "test_my_center"))
    def test_my_center_038(self, args):
        enter_my_center_bound_phonenum(self, args)
        self.page.my_center.click_login_password()
        self.page.my_center.click_continue_revise_password()
        if self.page.my_center.is_element_exist(self.page.my_center.image_code_title, 2) is True:
            self.page.my_center.click_close_image_code()
            self.page.my_center.clear_msg_code_revise_password()
            self.page.my_center.input_msg_code_revise_password(self.page.custom_functions.num_count(6))
            self.page.my_center.click_next_step_revise_password()
            assert self.page.my_center.is_element_exist(self.page.my_center.revise_password_title) is True
        else:
            self.page.my_center.clear_msg_code_revise_password()
            self.page.my_center.input_msg_code_revise_password(self.page.custom_functions.num_count(6))
            self.page.my_center.click_next_step_revise_password()
            assert self.page.my_center.is_element_exist(self.page.my_center.revise_password_title) is True

    # 61 在修改密码页面时，把app置于后台打开系统计算器应用计算数字后返回app能否继续修改密码
    @pytest.mark.parametrize("args", analyze_file("my_center.yaml", "test_my_center"))
    def test_my_center_061(self, args):
        enter_my_center_bound_phonenum(self, args)
        self.page.my_center.click_login_password()
        self.page.my_center.click_continue_revise_password()
        if self.page.my_center.is_element_exist(self.page.my_center.image_code_title, 2) is True:
            self.page.my_center.click_close_image_code()
        else:
            pass
        self.page.custom_functions.calculator()
        self.page.custom_functions.click_all_apps_handle()
        self.page.custom_functions.click_start_app()
        assert self.page.my_center.is_element_exist(self.page.my_center.revise_password_title) is True

    # 70 点击 忘记密码 （图示中找回密码表述有误，应为“忘记密码”），能否通过 webview 全屏打开 个人中心/忘记密码 页面
    def test_my_center_070(self):
        print('\n-------- 正在测试 个人中心 - 忘记密码(找回密码) 模块 --------')
        enter_retrieve_password(self)  # 进入找回密码页面
        assert self.page.my_center.is_element_exist(self.page.my_center.retrieve_password_title) is True
    #
    # # 71 进入 找回密码(忘记密码) 页面，在 请输入您的手机号或用户名 输入框中不输入任何信息，点击 下一步 按钮能否进行下一步
    # def test_my_center_071(self):
    #     enter_retrieve_password(self)  # 进入找回密码页面
    #     # self.page.my_center.clear_username_phonenum_retrieve_password()
    #     self.page.my_center.click_next_step_retrieve_password()
    #     time.sleep(1)
    #     assert self.page.my_center.is_element_exist(self.page.my_center.retrieve_password_title, 2) is True
    #
    # # 72 输入未注册过的 用户名，点击 下一步 按钮能否进行下一步，输入框下方是否有提示语
    # def test_my_center_072(self):
    #     enter_retrieve_password(self)  # 进入找回密码页面
    #     # self.page.my_center.clear_username_phonenum_retrieve_password()
    #     # self.page.my_center.input_username_phonenum_retrieve_password(
    #     #     self.page.custom_functions.letters_count(6))
    #     self.page.my_center.click_next_step_retrieve_password()
    #     time.sleep(1)
    #     self.driver.get_screenshot_as_file(os.getcwd() + "." + os.sep + "ui" + os.sep +
    #                                        "retrieve_password_提示用户不存在.png")
    #
    # # 73 输入未注册过的 手机号，点击 下一步 按钮能否进行下一步，输入框下方是否有提示语，如备注图所示
    # def test_my_center_073(self):
    #     enter_retrieve_password(self)  # 进入找回密码页面
    #     # self.page.my_center.clear_username_phonenum_retrieve_password()
    #     # self.page.my_center.input_username_phonenum_retrieve_password(
    #     #     "199" + self.page.custom_functions.letters_count(8))
    #     self.page.my_center.click_next_step_retrieve_password()
    #     time.sleep(1)
    #     self.driver.get_screenshot_as_file(os.getcwd() + "." + os.sep + "ui" + os.sep +
    #                                      "retrieve_password_提示用户不存在.png")
    #
    # # 74 输入已注册但未绑定手机号的 用户名，点击 下一步 按钮能否进行下一步，输入框下方是否有提示语
    # def test_my_center_074(self):
    #     self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
    #     self.page.home.click_login()  # 点击 登录 按钮
    #     for i in range(0, 2):
    #         if self.page.onekeyreg_login.is_element_exist(self.page.onekeyreg_login.onekeyreg_login_button, 1
    #                                                       ) is True:
    #             break
    #         elif self.page.auto_login.is_element_exist(self.page.auto_login.auto_login_title, 1) is True or \
    #                 self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True:
    #             self.page.realname.pass_auth()  # 通过认证实名认证
    #             self.page.home.click_logout()
    #             break
    #         else:
    #             print(f'error: 没有打开 一键注册登录 页面, 第{i + 1}次重试---------------')  # 再次重试打开
    #             self.page.custom_functions.background_task_start_app()  # 清空后台任务 - 启动app
    #             self.page.home.click_login()  # 点击 登录 按钮
    #     self.page.onekeyreg_login.click_onekeyreg_login()
    #     username = self.page.onekeyreg_login.get_text(self.page.onekeyreg_login.username)
    #     self.page.onekeyreg_login.click_enter_game()
    #     self.page.realname.pass_auth()
    #     self.page.home.click_logout()
    #     self.page.onekeyreg_login.click_other_reg()
    #     self.page.manually_login.click_forget_password()
    #     # self.page.my_center.clear_username_phonenum_retrieve_password()
    #     # self.page.my_center.input_username_phonenum_retrieve_password(username)
    #     self.page.my_center.click_next_step_retrieve_password()
    #     time.sleep(1)
    #     self.driver.get_screenshot_as_file(os.getcwd() + "." + os.sep + "ui" + os.sep +
    #                                        "retrieve_password_提示用户未绑定手机.png")
    #
    # # 75 输入已注册且已绑定手机号的 用户名，点击 下一步 按钮能否进入 找回密码 - 短信验证码 页面
    # def test_my_center_075(self):
    #     enter_retrieve_password(self)  # 进入找回密码页面
    #     # self.page.my_center.clear_username_phonenum_retrieve_password()
    #     # 在第18条用例中已声明 nickname 为全局变量, 是为了获取该测试账户最后一次修改昵称后的 昵称
    #     # self.page.my_center.input_username_phonenum_retrieve_password(nickname)
    #     self.page.my_center.click_next_step_retrieve_password()
    #     assert self.page.my_center.is_element_exist(
    #         self.page.my_center.input_msg_code_title_retrieve_password) is True
    #
    # # 76 输入已注册或已绑定过账号的 手机号，点击 下一步 按钮能否进入 找回密码 - 短信验证码 页面
    # @pytest.mark.parametrize("args", analyze_file("my_center.yaml", "test_my_center"))
    # def test_my_center_076(self, args):
    #     enter_retrieve_password(self)  # 进入找回密码页面
    #     phonenum = args["username_phonenum"]
    #     # self.page.my_center.clear_username_phonenum_retrieve_password()
    #     # self.page.my_center.input_username_phonenum_retrieve_password(phonenum)
    #     self.page.my_center.click_next_step_retrieve_password()
    #     assert self.page.my_center.is_element_exist(
    #         self.page.my_center.input_msg_code_title_retrieve_password) is True
    #
    # # 77 进入 找回密码 - 短信验证码 页面后点击左上角的 返回< 按钮能否返回上一个页面
    # @pytest.mark.parametrize("args", analyze_file("my_center.yaml", "test_my_center"))
    # def test_my_center_077(self, args):
    #     enter_retrieve_password(self)  # 进入找回密码页面
    #     phonenum = args["username_phonenum"]
    #     # self.page.my_center.clear_username_phonenum_retrieve_password()
    #     # self.page.my_center.input_username_phonenum_retrieve_password(phonenum)
    #     self.page.my_center.click_next_step_retrieve_password()
    #     self.page.my_center.click_back_input_msg_code_retrieve_password()
    #     assert self.page.my_center.is_element_exist(self.page.my_center.retrieve_password_title) is True
    #
    # # 78 在 短信验证码 输入框中不输入任何信息，点击 下一步 按钮能否进入 设置新的密码 页面
    # @pytest.mark.parametrize("args", analyze_file("my_center.yaml", "test_my_center"))
    # def test_my_center_078(self, args):
    #     enter_retrieve_password(self)  # 进入找回密码页面
    #     phonenum = args["username_phonenum"]
    #     # self.page.my_center.clear_username_phonenum_retrieve_password()
    #     # self.page.my_center.input_username_phonenum_retrieve_password(phonenum)
    #     self.page.my_center.click_next_step_retrieve_password()
    #     self.page.my_center.clear_msg_code_retrieve_password()
    #     self.page.my_center.input_msg_code_retrieve_password("")
    #     self.page.my_center.click_next_step_input_msg_code_retrieve_password()
    #     assert self.page.my_center.is_element_exist(
    #         self.page.my_center.input_msg_code_title_retrieve_password, 2) is True
    #
    # # 79 在 短信验证码 输入框中输入错误的验证码，点击 下一步 按钮能否进入 设置新的密码 页面
    # @pytest.mark.parametrize("args", analyze_file("my_center.yaml", "test_my_center"))
    # def test_my_center_079(self, args):
    #     enter_retrieve_password(self)  # 进入找回密码页面
    #     phonenum = args["username_phonenum"]
    #     # self.page.my_center.clear_username_phonenum_retrieve_password()
    #     # self.page.my_center.input_username_phonenum_retrieve_password(phonenum)
    #     self.page.my_center.click_next_step_retrieve_password()
    #     self.page.my_center.clear_msg_code_retrieve_password()
    #     self.page.my_center.input_msg_code_retrieve_password(self.page.custom_functions.num_count(6))
    #     self.page.my_center.click_next_step_input_msg_code_retrieve_password()
    #     assert self.page.my_center.is_element_exist(
    #         self.page.my_center.input_msg_code_title_retrieve_password, 2) is True
    #
    # # 95 忘记密码页面是否有错别字，是否简洁易懂
    # # 96 忘记密码页面的设计风格是否与UI的设计风格统一
    # @pytest.mark.parametrize("args", analyze_file("my_center.yaml", "test_my_center"))
    # def test_my_center_079(self, args):
    #     enter_retrieve_password(self)  # 进入找回密码页面
    #     if self.page.my_center.is_element_exist(self.page.my_center.retrieve_password_title) is True:
    #         self.driver.get_screenshot_as_file(os.getcwd() + "." + os.sep + "ui" + os.sep +
    #                                            "retrieve_password_ui01.png")
    #     else:
    #         assert 0
    #     phonenum = args["username_phonenum"]
    #     # self.page.my_center.clear_username_phonenum_retrieve_password()
    #     # self.page.my_center.input_username_phonenum_retrieve_password(phonenum)
    #     self.page.my_center.click_next_step_retrieve_password()
    #     if self.page.my_center.is_element_exist(self.page.my_center.input_msg_code_title_retrieve_password) is True: \
    #         self.driver.get_screenshot_as_file(os.getcwd() + "." + os.sep + "ui" + os.sep +
    #                                            "retrieve_password_ui01.png")
    #     else:
    #         assert 0

    # 99 在找回/修改密码过程中把app置于后台打开系统计算器应用计算数字后返回app能否继续
    def test_my_center_099(self):
        enter_retrieve_password(self)  # 进入找回密码页面
        self.page.custom_functions.calculator()
        self.page.custom_functions.click_all_apps_handle()
        self.page.custom_functions.click_start_app()
        assert self.page.my_center.is_element_exist(self.page.my_center.retrieve_password_title) is True

    # 101 如果用户已登录已绑定手机，在个人中心右侧是否能正确显示绑定手机的手机号，且中间四位数字是 **** 掩码显示，如备注图所示
    @pytest.mark.parametrize("args", analyze_file("my_center.yaml", "test_my_center"))
    def test_my_center_101(self, args):
        print('\n-------- 正在测试 个人中心 - 绑定手机号 模块 --------')
        enter_my_center_bound_phonenum(self, args)
        if self.page.my_center.is_element_exist(self.page.my_center.my_center_title) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + "." + os.sep + "ui" + os.sep +
                                               "bound_phonenum_手机号中间四位掩码显示.png")
        else:
            assert 0

    # 102 当用户没有绑定手机时，点击 绑定手机  按钮能否进入 绑定手机 页面
    def test_my_center_102(self):
        enter_my_center(self)
        self.page.my_center.click_bound_phonenum()
        assert self.page.my_center.is_element_exist(self.page.my_center.bound_phonenum_title) is True

    # 103 在 绑定手机 页面的手机号输入框中不输入任何信息，点击 下一步 按钮能否进入 输入验证码 页面
    def test_my_center_103(self):
        enter_my_center(self)
        self.page.my_center.click_bound_phonenum()
        self.page.my_center.clear_phonenum_bound_phonenum()
        self.page.my_center.click_next_step_bound_phonenum()
        assert self.page.my_center.is_element_exist(
            self.page.my_center.input_msg_code_bound_phonenum_title, 2) is False

    # 104 在 绑定手机 页面的手机号输入框中输入已经被绑定过的手机号，点击 下一步 按钮能否进入 输入短信验证码 页面
    @pytest.mark.parametrize("args", analyze_file("my_center.yaml", "test_my_center"))
    def test_my_center_104(self, args):
        phonenum = args["username_phonenum"]
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_bound_phonenum()  # 点击绑定手机
        self.page.my_center.clear_phonenum_bound_phonenum()
        self.page.my_center.input_phonenum_bound_phonenum(phonenum)  # 输入已绑定的手机号
        self.page.my_center.click_next_step_bound_phonenum()  # 点击 下一步 按钮
        if self.page.my_center.is_element_exist(
                self.page.my_center.already_bound_phonenum_title) is True:
            pass
        else:
            print(f"error_104: 用已绑定账号的手机号{phonenum}绑定别的账号时依然会进入 输入短信验证码页面")
            assert 0

    # 105 在 绑定手机 页面的手机号输入框中输入符合规则的手机号，点击 下一步 按钮能否进入 输入验证码 页面
    def test_my_center_105(self):
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_bound_phonenum()  # 点击绑定手机
        self.page.my_center.clear_phonenum_bound_phonenum()
        self.page.my_center.input_phonenum_bound_phonenum("199" + self.page.custom_functions.num_count(8))
        self.page.my_center.click_next_step_bound_phonenum()
        assert self.page.my_center.is_element_exist(
            self.page.my_center.input_msg_code_bound_phonenum_title, 2) is True

    # 107 在绑定手机号时, 进入 输入验证码 页面后输入焦点是否会自动聚焦在 短信验证码 输入框
    def test_my_center_107(self):
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_bound_phonenum()  # 点击绑定手机
        self.page.my_center.clear_phonenum_bound_phonenum()  # 清空手机号码输入框
        self.page.my_center.input_phonenum_bound_phonenum("199" + self.page.custom_functions.num_count(8))
        self.page.my_center.click_next_step_bound_phonenum()
        if self.page.my_center.is_element_exist(self.page.my_center.input_msg_code_bound_phonenum_title) is True:
            os.system("adb shell input keyevent 13")  # 对应数字 6
            assert self.page.my_center.get_text(self.page.my_center.msg_code_inputbox_bound_phonenum) == str(6)
        else:
            assert 0

    # 108 在绑定手机号时, 进入 输入验证码 页面后 重发 按钮是否显示60s倒计时
    def test_my_center_108(self):
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_bound_phonenum()  # 点击绑定手机
        self.page.my_center.clear_phonenum_bound_phonenum()  # 清空手机号码输入框
        self.page.my_center.input_phonenum_bound_phonenum("199" + self.page.custom_functions.num_count(8))
        self.page.my_center.click_next_step_bound_phonenum()  # 点击 下一步
        if self.page.my_center.is_element_exist(self.page.my_center.input_msg_code_bound_phonenum_title) is True:
            time.sleep(5)
            self.driver.get_screenshot_as_file(os.getcwd() + "." + os.sep + "ui" + os.sep +
                                               "bound_phonenum_进入倒计时.png")
            # assert self.page.my_center.get_content_desc(
            #     self.page.my_center.retry_msg_code_button_bound_phonenum) >= str(0)
        else:
            assert 0

    # 109 在绑定手机号时, 在 输入验证码 输入框中不输入任何信息，点击 完成 按钮能否完成绑定
    def test_my_center_109(self):
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_bound_phonenum()  # 点击绑定手机
        self.page.my_center.clear_phonenum_bound_phonenum()  # 清空手机号码输入框
        self.page.my_center.input_phonenum_bound_phonenum("199" + self.page.custom_functions.num_count(8))
        self.page.my_center.click_next_step_bound_phonenum()  # 点击 下一步
        self.page.my_center.clear_msg_code_bound_phonenum()  # 清空短信验证码输入框
        self.page.my_center.click_finish_bound_phonenum()  # 点击 完成 按钮
        assert self.page.my_center.is_element_exist(self.page.my_center.input_msg_code_bound_phonenum_title) is True

    # 110 在绑定手机号时, 在 输入验证码 输入框中输入错误的验证码，点击 完成 按钮能否完成绑定
    def test_my_center_110(self):
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_bound_phonenum()  # 点击绑定手机
        self.page.my_center.clear_phonenum_bound_phonenum()  # 清空手机号码输入框
        self.page.my_center.input_phonenum_bound_phonenum("199" + self.page.custom_functions.num_count(8))
        self.page.my_center.click_next_step_bound_phonenum()  # 点击 下一步
        self.page.my_center.clear_msg_code_bound_phonenum()  # 清空短信验证码输入框
        self.page.my_center.input_msg_code_bound_phonenum(self.page.custom_functions.num_count(6))
        self.page.my_center.click_finish_bound_phonenum()  # 点击 完成 按钮
        assert self.page.my_center.is_element_exist(self.page.my_center.input_msg_code_bound_phonenum_title) is True

    # 112 在绑定手机号时, 连续3次重新获取短信验证码后，第4次重新获取时，是否会弹出 图形验证码 页面
    def test_my_center_112(self):
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_bound_phonenum()  # 点击绑定手机
        self.page.my_center.clear_phonenum_bound_phonenum()  # 清空手机号码输入框
        self.page.my_center.input_phonenum_bound_phonenum("199" + self.page.custom_functions.num_count(8))
        self.page.my_center.click_next_step_bound_phonenum()  # 点击 下一步
        for i in range(0, 4):
            self.page.custom_functions.time_sleep(60, self.page.my_center.input_msg_code_bound_phonenum_title)
            self.page.my_center.click_retry_msg_code_bound_phonenum()
            if i <= 2 and self.page.my_center.is_element_exist(self.page.my_center.image_code_title, 2) is False:
                pass
            elif i >= 3 and self.page.my_center.is_element_exist(self.page.my_center.image_code_title, 2) is True:
                break
            else:
                # 正常情况下第4次点击后会弹出图形验证码, 此时 i == 3
                print(f"\nerror_112: 第{i + 1}次点击 重发 按钮后不能正确加载图形验证码 - 绑定手机号")
                assert 0

    # 113 在绑定手机号时, 在 图形验证码 输入框中不输入任何信息，点击 图形验证码 页面右上角 关闭× 按钮关闭 图形验证码 页面后，
    # 点击 完成 按钮能否完成绑定
    def test_my_center_113(self):
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_bound_phonenum()  # 点击绑定手机
        self.page.my_center.clear_phonenum_bound_phonenum()  # 清空手机号码输入框
        self.page.my_center.input_phonenum_bound_phonenum("199" + self.page.custom_functions.num_count(8))
        self.page.my_center.click_next_step_bound_phonenum()  # 点击 下一步
        for i in range(0, 4):
            self.page.custom_functions.time_sleep(60, self.page.my_center.input_msg_code_bound_phonenum_title)
            self.page.my_center.click_retry_msg_code_bound_phonenum()
            if self.page.my_center.is_element_exist(self.page.my_center.image_code_title, 2) is True:
                self.page.my_center.click_close_image_code()
                self.page.my_center.click_finish_bound_phonenum()  # 点击 完成 按钮
                assert self.page.my_center.is_element_exist(
                    self.page.my_center.input_msg_code_bound_phonenum_title, 2) is True
                break
            elif i == 3:
                assert 0

    # 117 绑定手机页面是否有错别字，是否简洁易懂
    # 118 绑定手机页面的设计风格是否与UI的设计风格统一
    def test_my_center_117_118(self):
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_bound_phonenum()  # 点击绑定手机
        if self.page.my_center.is_element_exist(self.page.my_center.bound_phonenum_title) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + "." + os.sep + "ui" + os.sep +
                                               "bound_phonenum_ui01.png")
        else:
            assert 0
        self.page.my_center.clear_phonenum_bound_phonenum()  # 清空手机号码输入框
        self.page.my_center.input_phonenum_bound_phonenum("199" + self.page.custom_functions.num_count(8))
        self.page.my_center.click_next_step_bound_phonenum()  # 点击 下一步
        if self.page.my_center.is_element_exist(self.page.my_center.input_msg_code_bound_phonenum_title) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + "." + os.sep + "ui" + os.sep +
                                               "bound_phonenum_ui02.png")
        else:
            assert 0
        self.page.my_center.clear_msg_code_bound_phonenum()  # 清空短信验证码输入框
        self.page.my_center.input_msg_code_bound_phonenum(self.page.custom_functions.num_count(6))
        self.page.my_center.click_finish_bound_phonenum()  # 点击 完成 按钮
        time.sleep(1)
        self.driver.get_screenshot_as_file(os.getcwd() + "." + os.sep + "ui" + os.sep +
                                           "bound_phonenum_ui03.png")

    # 119 在绑定手机过程中把app置于后台打开系统计算器应用计算数字后返回app能否继续绑定
    def test_my_center_119(self):
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_bound_phonenum()  # 点击绑定手机
        self.page.custom_functions.calculator()
        self.page.custom_functions.click_all_apps_handle()
        self.page.custom_functions.click_start_app()
        assert self.page.my_center.is_element_exist(self.page.my_center.bound_phonenum_title) is True

    # 125 已经绑定手机的，点击 绑定手机 菜单后，能否弹出浮层提示
    @pytest.mark.parametrize("args", analyze_file("my_center.yaml", "test_my_center"))
    def test_my_center_125(self, args):
        enter_my_center_bound_phonenum(self, args)
        self.page.my_center.click_bound_phonenum()
        assert self.page.my_center.is_element_exist(self.page.my_center.change_phonenum_title) is True

    # 126 点击 换绑手机 后，浮层显示是否有错别字，是否简洁易懂
    @pytest.mark.parametrize("args", analyze_file("my_center.yaml", "test_my_center"))
    def test_my_center_126(self, args):
        enter_my_center_bound_phonenum(self, args)
        self.page.my_center.click_bound_phonenum()
        if self.page.my_center.is_element_exist(self.page.my_center.change_phonenum_title) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + "." + os.sep + "ui" + os.sep +
                                               "change_phonenum_ui01.png")
        else:
            assert 0

    # 130 当用户未实名认证时，在 实名认证 菜单右侧是否显示 未认证 字样
    def test_my_center_130(self):
        print('\n-------- 正在测试 个人中心 - 实名认证 模块 --------')
        enter_my_center(self)  # 进入个人中心
        if self.page.my_center.is_element_exist(self.page.my_center.my_center_title) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + "." + os.sep + "ui" + os.sep +
                                               "realname_显示 未认证.png")
        else:
            assert 0

    # 131 当用户登录游戏后，游戏的实名认证（ realname_verify  ）配置为强制的（ force ）或 可选择的（optional）时，
    # 且用户未实名认证，是否显示 实名认证 页面
    def test_my_center_131(self):
        enter_realname(self)  # 进入实名认证页面
        assert self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True

    # 132 实名认证 页面的 完成认证 按钮默认是否为不可用状态
    def test_my_center_132(self):
        enter_realname(self)  # 进入实名认证页面
        assert self.page.realname.get_enabled(self.page.realname.finish_realname_button) == "false"

    # 133 进入 实名认证 页面后, 输入焦点默认是否聚焦在 真实姓名 输入框
    def test_my_center_133(self):
        enter_realname(self)  # 进入实名认证页面
        if self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True:
            os.system("adb shell input keyevent 13")  # 输入数字6
            if self.page.realname.get_text(self.page.realname.realname_inputbox) == str(6):
                pass
            else:
                print("error_133: 进入 实名认证 页面后, 输入焦点默认没有聚焦在 真实姓名 输入框")
                assert 0
        else:
            print("error_133: 没有正常进入实名验证页面")
            assert 0

    # 146 实名认证页面是否有错别字，是否简洁易懂
    def test_my_center_146(self):
        enter_realname(self)  # 进入实名认证页面
        if self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + "." + os.sep + "ui" + os.sep +
                                               "realname_ui01.png")
        else:
            assert 0

    # 151 在实名认证过程中把app置于后台打开系统计算器应用计算数字后返回app能否继续过程
    def test_my_center_151(self):
        enter_realname(self)  # 进入实名认证页面
        self.page.custom_functions.calculator()
        self.page.custom_functions.click_all_apps_handle()
        self.page.custom_functions.click_start_app()
        assert self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True

    # 158 检查帮助中心页面的内容是否如备注图所示
    # 159 帮助中心页面是否有错别字，是否简洁易懂
    # 160 帮助中心页面的设计风格是否与UI的设计风格统一
    def test_my_center_158_159_160(self):
        print('\n-------- 正在测试 个人中心 - 帮助中心 模块 --------')
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_help_center()  # 点击 帮助中心
        if self.page.my_center.is_element_exist(self.page.my_center.help_center_content) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + "." + os.sep + "ui" + os.sep +
                                               "help_center_ui01.png")
        else:
            assert 0

    # 161 点击帮助中心左上角的 返回< 按钮能否退出当前页面
    def test_my_center_161(self):
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_help_center()  # 点击 帮助中心
        self.page.my_center.click_back_help_center()
        assert self.page.my_center.is_element_exist(self.page.my_center.help_center_button, 2) is True

    # 163 在帮助中心页面时，把app置于后台打开系统计算器应用计算数字后返回app能否继续
    def test_my_center_163(self):
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_help_center()  # 点击 帮助中心
        self.page.custom_functions.calculator()
        self.page.custom_functions.click_all_apps_handle()
        self.page.custom_functions.click_start_app()
        assert self.page.my_center.is_element_exist(self.page.my_center.help_center_title) is True

    # 164 检查 意见反馈 页面是否存在，是否已放置客服联系方式
    # 168 意见反馈页面是否有错别字，是否简洁易懂
    # 169 意见反馈页面的设计风格是否与UI的设计风格统一
    def test_my_center_164_168_169(self):
        print('\n-------- 正在测试 个人中心 - 意见反馈 模块 --------')
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_help_center()
        if self.page.my_center.is_element_exist(self.page.my_center.help_center_title) is True:
            self.driver.get_screenshot_as_file(
                os.getcwd() + "." + os.sep + "ui" + os.sep + "feedback_ui01.png")
        else:
            assert 0

    # 170 点击意见反馈左上角的 返回< 按钮能否退出当前页面
    def test_my_center_170(self):
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_help_center()
        self.page.my_center.click_back_feedback()
        assert self.page.my_center.is_element_exist(self.page.my_center.feedback_title, 2) is False

    # 173 在意见反馈页面时，把app置于后台打开系统计算器应用计算数字后返回app能否返回之前页面
    def test_my_center_173(self):
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_feedback()
        self.page.custom_functions.calculator()
        self.page.custom_functions.click_all_apps_handle()
        self.page.custom_functions.click_start_app()
        assert self.page.my_center.is_element_exist(self.page.my_center.feedback_title) is True

    # 174 点击 退出登录 按钮后，是否显示带背景遮罩的模态对话框（由 JSAPI 提供），如备注图所示
    def test_my_center_174(self):
        print('\n-------- 正在测试 个人中心 - 退出登录 模块 --------')
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_logout()
        assert self.page.my_center.is_element_exist(self.page.my_center.logout_title) is True

    # 176 退出登录 页面是否有错别字，是否简洁易懂
    # 177 退出登录 页面的设计风格是否与UI的设计风格统一
    def test_my_center_176_177(self):
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_logout()
        if self.page.my_center.is_element_exist(self.page.my_center.logout_title) is True:
            self.driver.get_screenshot_as_file(
                os.getcwd() + "." + os.sep + "ui" + os.sep + "logout_ui01.png")
        else:
            assert 0

    # 179 点击 取消 按钮后，用户是否是登录状态
    def test_my_center_179(self):
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_logout()
        self.page.my_center.click_cancel_logout()
        assert self.page.my_center.is_element_exist(self.page.my_center.my_center_title) is True

    # 180 点击 确认 按钮后，是否能注销当前用户。并且在 callback 中关闭视图页面。
    def test_my_center_180(self):
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_logout()
        self.page.my_center.click_sure_logout()
        assert self.page.my_center.is_element_exist(self.page.my_center.my_center_title, 2) is False

    # 183 点击 退出登录 按钮后，此时会弹出对话框，把app置于后台打开系统计算器应用计算数字后返回app是否是未注销状态
    def test_my_center_183(self):
        enter_my_center(self)  # 进入个人中心
        self.page.my_center.click_logout()
        self.page.custom_functions.calculator()
        self.page.custom_functions.click_all_apps_handle()
        self.page.custom_functions.click_start_app()
        print('\n-------- 个人中心 模块测试完成 --------')
        assert self.page.my_center.is_element_exist(self.page.my_center.logout_title) is True
