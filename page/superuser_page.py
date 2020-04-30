from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class SuperuserPage(BaseAction):

    # 允许sdk访问您设备上的照片、媒体内容和文件 按钮
    allow_access_button = By.ID, "com.android.packageinstaller:id/permission_allow_button"

    # 允许显示在其他应用的上层 按钮
    allow_on_top_button = By.ID, "android:id/switch_widget"

    # 请求超级用户权限页面的 仅此次 按钮
    this_time_only_button = By.ID, "com.koushikdutta.superuser:id/this_time_only"

    # 请求超级用户权限页面的 记住选择10分钟 按钮
    remember_ten_minute_button = By.ID, "com.koushikdutta.superuser:id/remember_for"

    # 请求超级用户权限页面的 永久记住选择 按钮
    remember_forever_button = By.ID, "com.koushikdutta.superuser:id/remember_forever"

    # 请求超级管理权限时的 拒绝 按钮
    deny_superuser_button = By.ID, "com.koushikdutta.superuser:id/deny"

    # 请求超级管理权限时的 允许 按钮
    allow_superuser_button = By.ID, "com.koushikdutta.superuser:id/allow"

    # 请求超级用户权限页面的 标题
    superuser_title = By.XPATH, "//*[@text='超级用户请求']"

    # 点击 允许sdk访问您设备上的照片、媒体内容和文件 按钮
    def click_allow_access(self):
        self.click(self.allow_access_button)

    # 点击 允许显示在其他应用的上层 按钮
    def click_allow_on_top(self):
        self.click(self.allow_on_top_button)

    # 点击请求超级用户权限页面的 仅此次 按钮
    def click_this_time_only(self):
        self.click(self.this_time_only_button)

    # 点击请求超级用户权限页面的 记住选择10分钟 按钮
    def click_remember_ten_minute(self):
        self.click(self.remember_ten_minute_button)

    # 点击请求超级用户权限页面的 永久记住选择 按钮
    def click_remember_forever(self):
        self.click(self.remember_forever_button)

    # 点击请求超级用户权限时的 拒绝 按钮
    def click_deny_superuser(self):
        self.click(self.deny_superuser_button)

    # 点击请求超级用户权限时的 允许 按钮
    def click_allow_superuser(self):
        self.click(self.allow_superuser_button)
