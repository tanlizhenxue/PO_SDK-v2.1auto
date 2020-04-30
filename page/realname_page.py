import pytest

from selenium.webdriver.common.by import By
from base.base_action import BaseAction
from base.base_analyze import analyze_file


class RealnamePage(BaseAction):

    # 实名认证页面右上角的 关闭× 按钮
    close_realname_button = By.ID, "com.hzhy.sdk:id/iv_close"

    # 真实姓名 输入框
    realname_inputbox = By.ID, "com.hzhy.sdk:id/et_name"

    # 身份证号码 输入框
    id_card_num_inputbox = By.ID, "com.hzhy.sdk:id/et_identification_num"

    # 实名认证页面的 完成认证 按钮
    finish_realname_button = By.ID, "com.hzhy.sdk:id/tv_workout"

    # 实名认证页面的标题
    realname_auth_title = By.XPATH, "//*[@text='用户实名认证']"

    # 点击 实名认证页面右上角的 关闭× 按钮
    # @pytest.mark.parametrize("args", analyze_file("realname.yaml", "realname_page"))
    def click_close_realname(self):
        self.click(self.close_realname_button)
    #     print(1)
    #     name = args["name"]
    #     id_num = args["id_num"]
    #     try:
    #         self.find_element(self.close_realname_button, 2)
    #         print(2)
    #         self.click(self.close_realname_button)
    #     except TimeoutError:
    #         try:
    #             self.find_element(self.realname_auth_title, 1)
    #             print(3)
    #             self.clear_realname()
    #             print(name)
    #             self.input_realname(name)
    #             self.clear_id_card_num()
    #             print(id_num)
    #             self.input_id_card_num(id_num)
    #             self.click_finish_realname()
    #         except TimeoutError:
    #             print(4)
    #             pass

    # def click_close_realname(self):
    #     if self.find_elements(self.close_realname_button, 2):
    #         print(1)
    #         self.click(self.close_realname_button)
    #     elif self.find_elements(self.realname_auth_title, 1):
    #         print(2)
    #         self.clear_realname()
    #         self.input_realname("ty")
    #         # self.input_realname("王大二")
    #         self.clear_id_card_num()
    #         self.input_id_card_num("330106200202086890")
    #         # self.input_id_card_num("330106200202085652")
    #         # self.input_id_card_num("330106200202086575")
    #         # self.input_id_card_num("33010620020208641X")
    #         # self.input_id_card_num("330106200202085433")
    #         self.click_finish_realname()
    #     else:
    #         print(3)
    #         pass

    # 清除 真实姓名输入框
    def clear_realname(self):
        self.clear(self.realname_inputbox)

    # 输入 真实姓名
    def input_realname(self, realname):
        self.input(self.realname_inputbox, realname)

    # 清除 身份证号码输入框
    def clear_id_card_num(self):
        self.clear(self.id_card_num_inputbox)

    # 输入 身份证号码输入框
    def input_id_card_num(self, id_card_num):
        self.input(self.id_card_num_inputbox, id_card_num)

    # 输入姓名和身份证号码
    def input_name_id_num(self, name, id_num):
        self.clear_realname()
        self.input_realname(name)
        self.clear_id_card_num()
        self.input_id_card_num(id_num)

    # 点击 完成认证 按钮
    def click_finish_realname(self):
        self.click(self.finish_realname_button)

    # 通过实名认证
    def pass_auth(self):
        """
        处理逻辑:
        如果没有弹出实名认证窗口则处理方式为直接通过
        如果弹出实名认证窗口, 但有 关闭× 按钮, 处理方式为点击该按钮, 关闭实名认证窗口
        如果弹出实名认证窗口, 但没有 关闭× 按钮, 处理方式为输入姓名和身份证号码, 并点击 完成认证 按钮
        :return:
        """
        if self.is_element_exist(self.realname_auth_title, 2) is False:
            pass
        elif self.is_element_exist(self.close_realname_button, 1) is True:
            self.click_close_realname()
        elif self.is_element_exist(self.realname_auth_title, 1) is True and \
                self.is_element_exist(self.close_realname_button, 1) is False:
            self.input_name_id_num("ty", "320114200003076874")
            self.click_finish_realname()
        else:
            print("error:不能正确处理实名认证窗口")
