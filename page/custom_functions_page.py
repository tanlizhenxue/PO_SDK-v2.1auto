import os
import random
import string
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class CustomFunctionsPage(BaseAction):

    # sdk放置路径
    # app_file_path = "." + os.sep + "汇游戏SDK-v2.1.apk" + os.sep + "汇游戏2.1,{2019年12月27日16时35分28秒}test.apk"

    # 大小写字母共 52 * 2 个
    letters = str(string.ascii_letters) * 2

    # 数字共 10 * 10 个
    num = str(string.digits) * 10

    # 字符共 32 * 3 个, \ 是转义字符, 查看时可忽略
    character = str(
        '`' + '~' + '!' + '@' + '#' + '$' + '%' + '^' + '&' + '*' + '(' + ')' + '-' + '_' + '=' + '+' + '['
        + ']' + '{' + '}' + ';' + ':' + '\'' + '\"' + '\\' + '|' + ',' + '<' + '.' + '>' + '/' + '?') * 3

    # 启动SDK
    app_xpath = By.XPATH, "//*[@text='竞竞游戏']"

    # 后台多任务中的 sdk 任务
    background_task_sdk = By.XPATH, "//*[@text='竞竞游戏']"

    # 后台多任务中的 关闭× 按钮
    close_background_task_button = By.ID, "com.android.systemui:id/dismiss_task"

    # 后台多任务中的 全部清除 按钮
    close_all_background_tasks_button = By.ID, "com.android.systemui:id/button"

    # 实体按键 back键 (返回键) 位置
    back_xy = "adb shell input tap 315 2875"

    # 实体按键 home键 (主页键) 位置
    home_xy = "adb shell input tap 718 2875"

    # 实体按键 menu键 (多任务键) 位置
    multitask_xy = "adb shell input tap 1125 2875"

    # 手机中进入桌面抽屉的组件
    all_apps_handle_button = By.ID, "com.android.launcher3:id/all_apps_handle"

    # 计算器的包名
    calculator_package = "com.android.calculator2"

    # 计算器的启动名
    calculator_activity = "com.android.calculator2.Calculator"

    # 计算器数字 8
    num_8_button = By.ID, "com.android.calculator2:id/digit_8"

    # 计算器运算符 加 +
    plus_sign_button = By.ID, "com.android.calculator2:id/op_add"

    # 计算器运算符 等于 =
    equal_sign = By.ID, "com.android.calculator2:id/eq"

    # 返回数量为count位的 大小写字母
    def letters_count(self, count):
        return ''.join(random.sample(self.letters, count))

    # 返回数量为count位的 数字
    def num_count(self, count):
        return ''.join(random.sample(self.num, count))

    # 返回数量为count位的 字符 组合
    def character_count(self, count):
        return ''.join(random.sample(self.character, count))

    # 返回1个大或小写字母 + 1个数字
    def a_letters_num(self):
        return ''.join(random.sample(self.letters, 1)) + ''.join(random.sample(self.num, 1))

    # 返回1个大或小写字母 + 1个字符
    def a_letters_character(self):
        return ''.join(random.sample(self.letters, 1)) + ''.join(random.sample(self.character, 1))

    # 返回1个数字 + 1个字符
    def a_num_character(self):
        return ''.join(random.sample(self.num, 1)) + ''.join(random.sample(self.character, 1))

    # 返回1个大或小写字母 + 1个数字 + 1个字符
    def a_letters_num_character(self):
        return ''.join(random.sample(self.letters, 1)) + ''.join(random.sample(self.num, 1)) + \
               ''.join(random.sample(self.character, 1))

    # 返回数量为count位的 大小写字母 + 数字 组合
    def letters_num_count(self, count):
        return self.a_letters_num() + ''.join(random.sample(''.join(random.sample(self.letters, 30)) +
                                                            ''.join(random.sample(self.num, 30)), count-2))

    # 返回数量为count位的 大小字母 + 字符 组合
    def letters_character_count(self, count):
        return self.a_letters_character() + ''.join(random.sample(''.join(random.sample(self.letters, 30)) +
                                                                  ''.join(random.sample(self.character, 30)), count-2))

    # 返回数量为count位的 数字 + 字符 组合
    def num_character_count(self, count):
        return self.a_num_character() + ''.join(random.sample(''.join(random.sample(self.num, 30)) +
                                                              ''.join(random.sample(self.character, 30)), count-2))

    # 返回数量为count位的 大小写字母 + 数字 + 字符 组合
    def letters_num_character_count(self, count):
        return self.a_letters_num_character() + ''.join(random.sample(''.join(random.sample(self.letters, 30)) +
                                                                      ''.join(random.sample(self.num, 30)) +
                                                                      ''.join(random.sample(self.character, 30)),
                                                                      count-3))

    # 点击后台多任务中的 竞竞游戏 任务
    def click_background_task_sdk(self):
        self.click(self.background_task_sdk)

    # 点击手机中进入桌面抽屉的 组件
    def click_all_apps_handle(self):
        self.click(self.all_apps_handle_button)

    # 点击 后台多任务中的 关闭× 按钮
    def click_close_background_task(self):
        self.click(self.close_background_task_button)

    # 点击 后台多任务中的 全部清除 按钮
    def click_close_all_background_tasks(self):
        self.click(self.close_all_background_tasks_button)

    # 点击启动sdk
    def click_start_app(self):
        self.click(self.app_xpath)

    # 点击实体按键 back键(返回键)
    def click_back_key(self):
        os.system(self.back_xy)

    # 点击实体按键 home键(主页键)
    def click_home_key(self):
        os.system(self.home_xy)

    # 点击实体按键 menu键(多任务键)
    def click_multitask_key(self):
        os.system(self.multitask_xy)

    # 获取屏幕横向分辨率并返回
    def get_window_size_x(self):
        return self.driver.get_window_size()['width']

    # 获取屏幕纵向分辨率并返回
    def get_window_size_y(self):
        return self.driver.get_window_size()['height']

    # 进入多任务页面分别清除每一个后台任务
    def close_every_background_task(self):
        self.click_multitask_key()
        if self.is_element_exist(self.close_background_task_button, 3) is True:
            while True:
                try:
                    self.find_element(self.close_background_task_button, 1)
                    self.click_close_background_task()
                except TimeoutException:
                    self.click_home_key()
                    break
        else:
            self.click_home_key()

    # 运行  清空后台任务 - 进入应用抽屉 - 启动sdk 的流程
    def background_task_start_app(self):
        self.close_every_background_task()
        time.sleep(0.5)
        self.click_all_apps_handle()
        self.click_start_app()

    # 打开计算器运算后返回桌面
    def calculator(self):
        time.sleep(0.1)
        self.click_home_key()  # 先返回桌面
        time.sleep(0.5)
        self.driver.start_activity(self.calculator_package, self.calculator_activity)
        self.click(self.num_8_button)
        self.click(self.plus_sign_button)
        self.click(self.num_8_button)
        self.click(self.equal_sign)
        self.click_home_key()  # 返回桌面
