from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class MyCenterPage(BaseAction):

    # 个人中心右上角的 关闭× 按钮
    close_my_center_button = By.ID, "com.hzhy.sdk:id/ib_close"

    # 个人中心的 标题
    my_center_title = By.XPATH, "//*[@text='汇游戏个人中心']"

    # 昵称 按钮
    nickname_button = By.CLASS_NAME, 'android.view.View'

    # 修改昵称 按钮
    revise_nickname = By.XPATH, "//*[@content-desc='修改昵称 ']"

    # 修改昵称页面左上角的 返回< 按钮
    revise_nickname_back_button = By.ID, "com.hzhy.sdk:id/ib_back"

    # 昵称输入框
    nickname_inputbox = By.CLASS_NAME, "android.widget.EditText"

    # 修改昵称页面的 确定 按钮
    nickname_sure_button = By.XPATH, "//*[@content-desc='确定']"

    # 修改昵称页面的 标题
    revise_nickname_title = By.XPATH, "//*[@text='修改昵称']"

    # 修改昵称成功页面的 关闭 按钮
    revise_nickname_success_close_button = By.XPATH, "//*[@content-desc='关闭']"

    # 修改昵称成功页面的 标题
    revise_nickname_success_title = By.XPATH, "//*[@content-desc='修改昵称成功']"

    # 登录密码 按钮
    login_password_button = By.XPATH, "//*[@content-desc='登录密码']"

    # 未绑定手机页面的 确定 按钮
    sure_button_unbound_phonenum = By.XPATH, "//*[@text='确定']"

    # 未绑定手机页面的 标题
    unbound_phonenum_title = By.XPATH, "//*[@text='提示']"

    # 修改密码页面的 取消 按钮
    revise_password_cancel_button = By.XPATH, "//*[@text='取消']"

    # 修改密码页面的 继续 按钮
    revise_password_continue_button = By.XPATH, "//*[@text='继续']"

    # 修改密码页面的 标题
    revise_password_title = By.XPATH, "//*[@text='修改密码']"

    # 输入短信验证码页面左上角的 返回< 按钮
    input_msg_code_back_button_revise_password = By.ID, "com.hzhy.sdk:id/ib_back"

    # 输入短信验证码页面 短信验证码输入框
    msg_code_inputbox_revise_password = By.CLASS_NAME, "android.widget.EditText"

    # 输入短信验证码页面的 重发 按钮
    retry_msg_code_button_revise_password = By.CLASS_NAME, "android.view.View"

    # 输入短信验证码页面的 下一步 按钮
    next_step_button_revise_password = By.CLASS_NAME, "android.widget.Button"

    # 输入短信验证码页面的 标题
    input_msg_code_title_revise_password = By.XPATH, "//*[@text='修改密码']"

    # 图形验证码右上角的 关闭× 按钮
    close_image_code_button = By.XPATH, "//*[@content-desc='SXDD3RuPHe5wBXgMqLANGBD+pJviFa660YAAAAAElFTkSuQmCC']"

    # 图形验证码页面的标题
    image_code_title = By.XPATH, "//*[@content-desc='输入图形验证码']"

    # 找回密码页面的 手机号或用户名输入框
    username_phonenum_inputbox_retrieve_password = By.CLASS_NAME, "android.widget.EditText"

    # 找回密码页面的 下一步 按钮
    next_step_button_retrieve_password = By.XPATH, "//*[@content-desc='下一步']"

    # 找回密码页面的 标题
    retrieve_password_title = By.XPATH, "//*[@text='找回密码']"

    # 找回密码 - 输入短信验证码 页面左上角的 返回< 按钮
    input_msg_code_back_button_retrieve_password = By.ID, "com.hzhy.sdk:id/ib_back"

    # 找回密码 - 输入短信验证码 页面的输入框
    msg_code_inputbox_retrieve_password = By.CLASS_NAME, "android.widget.EditText"

    # 找回密码 - 输入短信验证码 页面的 重发 按钮
    retry_msg_code_button_retrieve_password = By.CLASS_NAME, "android.view.View"

    # 找回密码 - 输入短信验证码 页面的 下一步 按钮
    next_step_button_input_msg_code_retrieve_password = By.CLASS_NAME, "android.widget.Button"

    # 找回密码 - 输入短信验证码 页面的的标题
    input_msg_code_title_retrieve_password = By.XPATH, "//*[@content-desc='我们已经发送验证码到您的手机']"

    # 绑定手机 按钮
    bound_phonenum_button = By.XPATH, "//*[@content-desc='绑定手机']"

    # 绑定手机页面左上方的 返回< 按钮
    bound_phonenum_back_button = By.ID, "com.hzhy.sdk:id/ib_back"

    # 绑定手机号页面的 手机号输入框
    phonenum_inputbox_bound_phonenum = By.CLASS_NAME, "android.widget.EditText"

    # 绑定手机号页面的 下一步 按钮
    next_step_button_bound_phonenum = By.XPATH, "//*[@content-desc='下一步']"

    # 绑定手机号中输入短信验证码页面的 短信验证码 输入框
    msg_code_inputbox_bound_phonenum = By.CLASS_NAME, "android.widget.EditText"

    # 绑定手机号中输入短信验证码页面的 重发 按钮
    retry_msg_code_button_bound_phonenum = By.XPATH, "//*[@content-desc='重发']"

    # 绑定手机号中输入短信验证码页面的 完成 按钮
    finish_button_bound_phonenum = By.XPATH, "//*[@content-desc='完成']"

    # 绑定手机页面的 标题
    bound_phonenum_title = By.XPATH, "//*[@text='绑定手机']"

    # 绑定手机号中输入短信验证码页面的 标题
    input_msg_code_bound_phonenum_title = By.XPATH, "//*[@content-desc='我们已经发送验证码到您的手机']"

    # 已绑定手机页面的标题
    already_bound_phonenum_title = By.XPATH, "//*[@text='该手机号码已绑定,请返回上一页重新输入手机号']"

    # 换绑手机页面的 确定 按钮
    change_phonenum_sure_button = By.XPATH, "//*[@text='确定']"

    # 换绑手机页面的 标题
    change_phonenum_title = By.XPATH, "//*[@text='修改绑定手机']"

    # 帮助中心 按钮
    help_center_button = By.XPATH, "//*[@content-desc='帮助中心']"

    # 帮助中心页面左上角的 返回< 按钮
    back_button_help_center = By.ID, "com.hzhy.sdk:id/ib_back"

    # 帮助中心页面的 内容
    help_center_content = By.XPATH, "//*[@content-desc='任何疑问请添加QQ：1780035375（醉竹) 联系我们的客服专员。']"

    # 帮助中心页面 标题
    help_center_title = By.XPATH, "//*[@text='帮助中心']"

    # 意见反馈 按钮
    feedback_button = By.XPATH, "//*[@content-desc='意见反馈']"

    # 意见反馈页面左上角的 返回< 按钮
    back_button_feedback = By.ID, "com.hzhy.sdk:id/ib_back"

    # 意见反馈页面的 内容
    feedback_content = By.XPATH, "//*[@content-desc='任何疑问请添加QQ：1780035375（醉竹) 联系我们的客服专员。']"

    # 意见反馈页面的 标题
    feedback_title = By.XPATH, "//*[@text='意见反馈']"

    # 隐藏浮球 按钮(详见悬浮球)
    hide_float_ball_button = By.XPATH, "//*[@content-desc='隐藏浮球']"

    # 已隐藏 按钮
    already_hide_float_ball_button = By.XPATH, "//*[@content-desc='已隐藏']"

    # 隐藏浮球对话框中的 确定 按钮
    hide_float_ball_sure_button = By.XPATH, "//*[@text='确定']"

    # 隐藏浮球对话框中的 取消 按钮
    hide_float_ball_cancel_button = By.XPATH, "//*[@content-desc='取消']"

    # 已隐藏浮球弹窗中的 确定 按钮
    already_hide_float_ball_sure_button = By.XPATH, "//*[@text='确定']"

    # 隐藏浮球弹窗的 标题
    hide_float_ball_title = By.XPATH, "//*[@text='重启游戏后即可重新显示悬浮球，确定要隐藏么？']"

    # 已隐藏浮球弹窗的 标题
    already_hide_float_ball_title = By.XPATH, "//*[@text='提示']"

    # 退出登录 按钮
    logout_button = By.XPATH, "//*[@content-desc='退出登录']"

    # 退出登录页面的 取消 按钮
    cancel_button_logout = By.XPATH, "//*[@text='取消']"

    # 退出登录页面的 确定 按钮
    sure_button_logout = By.XPATH, "//*[@text='确定']"

    # 退出登录页面的 标题
    logout_title = By.XPATH, "//*[@text='你确定要退出当前登录的汇游戏帐号么？']"

    # 点击个人中心右上角的 关闭× 按钮
    def click_close_my_center(self):
        self.click(self.close_my_center_button)

    # 点击 修改昵称 按钮
    def click_revise_nickname(self):
        self.click(self.revise_nickname)

    # 点击修改昵称页面左上角的 返回< 按钮
    def click_back_revise_nickname(self):
        self.click(self.revise_nickname_back_button)

    # 清空输入昵称页面的输入框
    def clear_nickname(self):
        self.clear(self.nickname_inputbox)

    # 在修改昵称页面的输入框中输入新昵称
    def input_nickname(self, nickname):
        self.input(self.nickname_inputbox, nickname)

    # 点击修改昵称页面的 确定 按钮
    def click_sure_revise_nickname(self):
        self.click(self.nickname_sure_button)

    # 点击修改昵称成功页面的 关闭 按钮
    def click_close_revise_nickname_success(self):
        self.click(self.revise_nickname_success_close_button)

    # 点击 登录密码 按钮
    def click_login_password(self):
        self.click(self.login_password_button)

    # 点击修改密码页面的 取消 按钮
    def click_cancel_revise_password(self):
        self.click(self.revise_password_cancel_button)

    # 点击修改密码页面的 继续 按钮
    def click_continue_revise_password(self):
        self.click(self.revise_password_continue_button)

    # 点击输入短信验证码页面左上角的 返回< 按钮
    def click_back_input_msg_code_revise_password(self):
        self.click(self.input_msg_code_back_button_revise_password)

    # 清空输入短信验证码页面 短信验证码输入框
    def clear_msg_code_revise_password(self):
        self.clear(self.msg_code_inputbox_revise_password)

    # 在修改密码页面输入 短信验证码
    def input_msg_code_revise_password(self, msg_code):
        self.input(self.msg_code_inputbox_revise_password, msg_code)

    # 点击输入短信验证码页面的 重发 按钮
    def click_retry_msg_code_revise_password(self):
        self.click(self.retry_msg_code_button_revise_password)

    # 点击输入短信验证码页面的 下一步 按钮
    def click_next_step_revise_password(self):
        self.click(self.next_step_button_revise_password)

    # 点击未绑定手机页面的 确定 按钮
    def click_sure_unbound_phonenum(self):
        self.click(self.sure_button_unbound_phonenum)

    # 点击图形验证码右上角的 关闭× 按钮
    def click_close_image_code(self):
        self.click(self.close_image_code_button)

    # 清空找回密码页面的 手机号或用户名输入框
    def clear_username_phonenum_retrieve_password(self):
        self.clear(self.username_phonenum_inputbox_retrieve_password)

    # 输入需要找回的用户名或手机号
    def input_username_phonenum_retrieve_password(self, username_phonenum):
        self.input(self.username_phonenum_inputbox_retrieve_password, username_phonenum)

    # 点击找回密码页面的 下一步 按钮
    def click_next_step_retrieve_password(self):
        self.click(self.next_step_button_retrieve_password)

    # 点击 找回密码 - 输入短信验证码 页面左上角的 返回< 按钮
    def click_back_input_msg_code_retrieve_password(self):
        self.click(self.input_msg_code_back_button_retrieve_password)

    # 清空 找回密码 - 输入短信验证码 页面的输入框
    def clear_msg_code_retrieve_password(self):
        self.click(self.msg_code_inputbox_retrieve_password)

    # 在 找回密码 - 输入短信验证码 页面的输入输入短信验证码
    def input_msg_code_retrieve_password(self, msg_code):
        self.input(self.msg_code_inputbox_retrieve_password, msg_code)

    # 点击 找回密码 - 输入短信验证码 页面的 重发 按钮
    def click_retry_msg_code_retrieve_password(self):
        self.click(self.retry_msg_code_button_retrieve_password)

    # 点击 找回密码 - 输入短信验证码 页面的 下一步 按钮
    def click_next_step_input_msg_code_retrieve_password(self):
        self.click(self.next_step_button_input_msg_code_retrieve_password)

    # 点击 绑定手机 按钮
    def click_bound_phonenum(self):
        self.click(self.bound_phonenum_button)

    # 点击绑定手机页面左上方的 返回< 按钮
    def click_back_bound_phonenum(self):
        self.click(self.bound_phonenum_back_button)

    # 清空绑定手机号页面的 手机号输入框
    def clear_phonenum_bound_phonenum(self):
        self.clear(self.phonenum_inputbox_bound_phonenum)

    # 在绑定手机号页面的 手机号输入框 输入手机号
    def input_phonenum_bound_phonenum(self, phonenum):
        self.input(self.phonenum_inputbox_bound_phonenum, phonenum)

    # 点击绑定手机号页面的 下一步 按钮
    def click_next_step_bound_phonenum(self):
        self.click(self.next_step_button_bound_phonenum)

    # 清空绑定手机号中输入短信验证码页面的 短信验证码 输入框
    def clear_msg_code_bound_phonenum(self):
        self.clear(self.msg_code_inputbox_bound_phonenum)

    # 在绑定手机号中输入短信验证码页面的 短信验证码 输入框中输入短信验证码
    def input_msg_code_bound_phonenum(self, msg_code):
        self.input(self.msg_code_inputbox_bound_phonenum, msg_code)

    # 点击绑定手机号中输入短信验证码页面的 重发 按钮
    def click_retry_msg_code_bound_phonenum(self):
        self.click(self.retry_msg_code_button_bound_phonenum)

    # 点击绑定手机号中输入短信验证码页面的 完成 按钮
    def click_finish_bound_phonenum(self):
        self.click(self.finish_button_bound_phonenum)

    # 点击换绑手机页面的 确定 按钮
    def click_sure_change_phonenum(self):
        self.click(self.change_phonenum_sure_button)

    # 点击 帮助中心 按钮
    def click_help_center(self):
        self.click(self.help_center_button)

    # 点击帮助中心页面左上角的 返回< 按钮
    def click_back_help_center(self):
        self.click(self.back_button_help_center)

    # 点击 意见反馈 按钮
    def click_feedback(self):
        self.click(self.feedback_button)

    # 点击意见反馈页面左上角的 返回< 按钮
    def click_back_feedback(self):
        self.click(self.back_button_feedback)

    # 点击 隐藏浮球 按钮
    def click_hide_float_ball(self):
        self.click(self.hide_float_ball_button)

    # 点击 已隐藏 按钮
    def click_already_hide_float_ball(self):
        self.click(self.already_hide_float_ball_button)

    # 点击隐藏浮球对话框中的 确定 按钮
    def click_hide_float_ball_sure(self):
        self.click(self.hide_float_ball_sure_button)

    # 点击隐藏浮球对话框中的 取消 按钮
    def click_hide_float_ball_cancel(self):
        self.click(self.hide_float_ball_cancel_button)

    # 点击已隐藏浮球弹窗中的 确定 按钮
    def click_already_hide_float_ball_sure(self):
        self.click(self.already_hide_float_ball_sure_button)

    # 点击 退出登录 按钮
    def click_logout(self):
        self.click(self.logout_button)

    # 点击退出登录页面的 取消 按钮
    def click_cancel_logout(self):
        self.click(self.cancel_button_logout)

    # 点击退出登录页面的 确定 按钮
    def click_sure_logout(self):
        self.click(self.sure_button_logout)
