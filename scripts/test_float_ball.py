import os
import time

from base.base_driver import init_driver
from page.page import Page


# 运行 清空后台 - 打开app - 进入 已登录 页面的流程
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


class TestFloatBall:

    def setup(self):
        self.driver = init_driver(no_reset=True)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    # 01 游戏加载完成后，默认情况下能否显示悬浮球
    def test_float_ball_001(self):
        print('\n\n-------- 正在测试 悬浮球 模块 --------')
        enter_login(self)
        time.sleep(1)
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/float_ball_ui_01.png")

    # 02 在显示登录、自动登录、注册、自动注册、实名认证、支付、个人中心 webview等页面的时候，悬浮球是否会直接隐藏
    def test_float_ball_002(self):
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
        # 在一键注册登录页面是否不显示悬浮球
        if self.page.onekeyreg_login.is_element_exist(self.page.onekeyreg_login.onekeyreg_login_button) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/float_ball_ui_02.png")
        else:
            assert 0
        self.page.onekeyreg_login.click_onekeyreg_login()
        self.page.onekeyreg_login.click_enter_game()
        # 在实名认证页面是否不显示悬浮球
        if self.page.realname.is_element_exist(self.page.realname.realname_auth_title) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/float_ball_ui_03.png")
        else:
            assert 0
        self.page.realname.pass_auth()
        self.page.home.click_login()
        # 在自动登录时是否不显示悬浮球
        if self.page.auto_login.is_element_exist(self.page.auto_login.auto_login_title) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/float_ball_ui_04.png")
        else:
            assert 0
        time.sleep(3)
        self.page.realname.pass_auth()
        self.page.home.click_logout()
        self.page.onekeyreg_login.click_other_reg()
        # 在手动登录页面是否不显示悬浮球
        if self.page.manually_login.is_element_exist(self.page.manually_login.manually_login_title) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/float_ball_ui_05.png")
        else:
            assert 0
        self.page.manually_login.click_fast_reg()
        # 在手机号注册页面是否不显示悬浮球
        if self.page.phonenum_reg.is_element_exist(self.page.phonenum_reg.phonenum_reg_title) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/float_ball_ui_06.png")
        else:
            assert 0
        self.page.phonenum_reg.click_username_reg()
        # 在用户名注册页面是否不显示悬浮球
        if self.page.username_reg.is_element_exist(self.page.username_reg.username_reg_title) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/float_ball_ui_07.png")
        else:
            assert 0
        self.page.username_reg.input_username_password(self.page.custom_functions.letters_num_count(8),
                                                       self.page.custom_functions.letters_num_count(8))
        self.page.username_reg.click_now_reg()
        self.page.realname.pass_auth()
        self.page.home.click_pay()
        self.page.realname.pass_auth()
        # 在收银台页面是否不显示悬浮球
        if self.page.pay.is_element_exist(self.page.pay.pay_title) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/float_ball_ui_08.png")
        else:
            assert 0
        self.page.pay.click_close_pay()
        self.page.pay.click_quit()
        time.sleep(3.5)
        self.page.float_ball.click_float_ball_fold()
        time.sleep(1)
        self.page.float_ball.click_me()
        time.sleep(3)
        # 在个人中心是否不显示悬浮球
        if self.page.my_center.is_element_exist(self.page.my_center.my_center_title) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/float_ball_ui_09.png")
        else:
            assert 0

    # 03 当拖拽悬浮球并释放后，悬浮球是否会停靠在距离最近的屏幕边缘，且只能在屏幕左测或右侧贴边展示
    # 04 悬浮球在屏幕左边或在右边时, 能否正常展开
    # 05 检查悬浮球大小36*36px，背景及文字透明度为40%（开发时需要根据显示效果具体微调下），距离屏幕边缘10px 贴边显示
    # 06 点击一次悬浮球，当悬浮球处于正常状态没有被点击，3秒后是否会自动贴边半隐藏
    # 09 悬浮球页面是否有错别字，是否简洁易懂
    # 10 悬浮球页面的设计风格是否与UI的设计风格统一
    def test_float_ball_003_004_005(self):
        enter_login(self)  # 进入 已登录 页面
        time.sleep(self.page.float_ball.fold_time)
        self.page.float_ball.click_float_ball_fold()
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/float_ball_ui_在左边展开.png")
        time.sleep(self.page.float_ball.fold_time)
        self.driver.swipe(15, 90, (3 / 5) * self.page.custom_functions.get_window_size_x(), 90, 3000)
        time.sleep(self.page.float_ball.fold_time)
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/float_ball_ui_滑动后在右边贴边.png")
        os.system("adb shell input tap 1425 90")
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/float_ball_ui_在右边展开.png")
        time.sleep(self.page.float_ball.fold_time)
        self.driver.swipe(1425, 90, (2 / 5) * self.page.custom_functions.get_window_size_x(), 90, 3000)
        time.sleep(self.page.float_ball.fold_time)
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/float_ball_ui_滑动后在左边贴边.png")

    # 07 当悬浮球在展开状态下，再次点击悬浮球时，能否动画收起按钮组
    def test_float_ball_007(self):
        enter_login(self)  # 进入 已登录 页面
        time.sleep(self.page.float_ball.fold_time)
        self.page.float_ball.click_float_ball_fold()
        self.page.float_ball.click_float_ball_unfold()
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/float_ball_ui_收起按钮.png")

    # 13 点击悬浮球中的 我的 按钮是否可以跳转到个人中心页面
    def test_float_ball_013(self):
        enter_login(self)  # 进入 已登录 页面
        time.sleep(self.page.float_ball.fold_time)
        self.page.float_ball.click_float_ball_fold()
        self.page.float_ball.click_me()
        assert self.page.my_center.is_element_exist(self.page.my_center.my_center_title) is True

    # 14 点击悬浮球中的 我的 按钮跳转到个人中心页面后，把app置于后台打开系统计算器应用计算数字后返回app能否继续
    def test_float_ball_014(self):
        enter_login(self)  # 进入 已登录 页面
        time.sleep(self.page.float_ball.fold_time)
        self.page.float_ball.click_float_ball_fold()
        self.page.float_ball.click_me()
        self.page.custom_functions.calculator()
        self.page.custom_functions.click_all_apps_handle()
        self.page.custom_functions.click_start_app()
        assert self.page.my_center.is_element_exist(self.page.my_center.my_center_title) is True

    # 16 在 个人中心 中点击 关闭× 按钮是否能够返回
    def test_float_ball_016(self):
        enter_login(self)  # 进入 已登录 页面
        time.sleep(self.page.float_ball.fold_time)
        self.page.float_ball.click_float_ball_fold()
        self.page.float_ball.click_me()
        if self.page.my_center.is_element_exist(self.page.my_center.my_center_title) is True:
            time.sleep(1)
            self.page.my_center.click_close_my_center()
        else:
            assert 0
        assert self.page.home.is_element_exist(self.page.home.login_button) is True

    # 18 当悬浮球展开时，点击 注销 按钮，是否能够注销成功
    def test_float_ball_018(self):
        enter_login(self)  # 进入 已登录 页面
        time.sleep(self.page.float_ball.fold_time)
        self.page.float_ball.click_float_ball_fold()
        self.page.float_ball.click_logout()
        assert self.page.onekeyreg_login.is_element_exist(self.page.onekeyreg_login.onekeyreg_login_title) is True

    # 19 在个人中心时点击home键返回桌面, 再次进入app, 悬浮球是否会出现
    def test_float_ball_019(self):
        enter_login(self)  # 进入 已登录 页面
        time.sleep(self.page.float_ball.fold_time)
        self.page.float_ball.click_float_ball_fold()
        self.page.float_ball.click_me()
        self.page.custom_functions.click_home_key()
        self.page.custom_functions.click_all_apps_handle()
        self.page.custom_functions.click_start_app()
        if self.page.my_center.is_element_exist(self.page.my_center.my_center_title) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/float_ball_ui_不显示悬浮球.png")
        else:
            assert 0

    # 23 点击 隐藏浮球 菜单，能否弹出带背景遮罩的模态对话框，提示文字如备注图示
    def test_float_ball_023(self):
        enter_login(self)  # 进入 已登录 页面
        time.sleep(self.page.float_ball.fold_time)
        self.page.float_ball.click_float_ball_fold()
        self.page.float_ball.click_me()
        self.page.my_center.click_hide_float_ball()
        assert self.page.my_center.is_element_exist(self.page.my_center.hide_float_ball_title) is True

    # 25 点击对话框中的 确定 按钮后能否正常隐藏浮球
    def test_float_ball_025(self):
        enter_login(self)  # 进入 已登录 页面
        time.sleep(self.page.float_ball.fold_time)
        self.page.float_ball.click_float_ball_fold()
        self.page.float_ball.click_me()
        self.page.my_center.click_hide_float_ball()
        self.page.my_center.click_hide_float_ball_sure()
        assert self.page.custom_functions.get_toast_text("隐藏悬浮球") == "隐藏悬浮球"
        self.page.my_center.click_close_my_center()
        if self.page.home.is_element_exist(self.page.home.login_button) is True:
            self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/float_ball_ui_不显示悬浮球02.png")
        else:
            assert 0

    # 26 隐藏后，在该菜单右侧是否显示 已隐藏 字样，如备注图所示
    def test_float_ball_026(self):
        enter_login(self)  # 进入 已登录 页面
        time.sleep(self.page.float_ball.fold_time)
        self.page.float_ball.click_float_ball_fold()
        self.page.float_ball.click_me()
        self.page.my_center.click_hide_float_ball()
        self.page.my_center.click_hide_float_ball_sure()
        assert self.page.my_center.is_element_exist(self.page.my_center.already_hide_float_ball_button) is True

    # 27 隐藏后，点击 隐藏浮球 菜单是否显示 悬浮球已隐藏，下次重新打开游戏时将会重新显示悬浮球 的提示，如备注图所示
    def test_float_ball_027(self):
        enter_login(self)  # 进入 已登录 页面
        time.sleep(self.page.float_ball.fold_time)
        self.page.float_ball.click_float_ball_fold()
        self.page.float_ball.click_me()
        self.page.my_center.click_hide_float_ball()
        self.page.my_center.click_hide_float_ball_sure()
        self.page.my_center.click_already_hide_float_ball()
        assert self.page.my_center.is_element_exist(self.page.my_center.already_hide_float_ball_title) is True

    # 28 隐藏悬浮球后, 重新打开app, 悬浮球是否已恢复
    def test_float_ball_028(self):
        enter_login(self)  # 进入 已登录 页面
        time.sleep(self.page.float_ball.fold_time)
        self.page.float_ball.click_float_ball_fold()
        self.page.float_ball.click_me()
        self.page.my_center.click_hide_float_ball()
        self.page.my_center.click_hide_float_ball_sure()
        self.page.custom_functions.background_task_start_app()
        self.page.home.click_login()
        self.page.realname.pass_auth()
        time.sleep(0.5)
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + "./ui/float_ball_ui_悬浮球已恢复.png")
        print('\n-------- 悬浮球 模块测试完成 --------')
