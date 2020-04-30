import os

from base.base_action import BaseAction


class FloatBallPage(BaseAction):

    # 悬浮球贴边的时间
    fold_time = 6.5

    # 悬浮球贴边时的 坐标位置
    float_ball_fold = "adb shell input tap 15 90"

    # 悬浮球展开时的 坐标位置
    float_ball_unfold = "adb shell input tap 70 90"

    # 悬浮球中 我的 按钮的位置
    float_ball_me = "adb shell input tap 271 90"

    # 悬浮球中 帮助 按钮的位置
    float_ball_help = "adb shell input tap 475 90"

    # 悬浮球中 注销 按钮的位置
    float_ball_logout = "adb shell input tap 685 90"

    # 点击 贴边时的悬浮球
    def click_float_ball_fold(self):
        os.system(self.float_ball_fold)

    # 点击 展开时的悬浮球
    def click_float_ball_unfold(self):
        os.system(self.float_ball_unfold)

    # 点击悬浮球中的 我的
    def click_me(self):
        os.system(self.float_ball_me)

    # 点击悬浮球中的 帮助
    def click_help(self):
        os.system(self.float_ball_help)

    # 点击悬浮球中的 注销
    def click_logout(self):
        os.system(self.float_ball_logout)
