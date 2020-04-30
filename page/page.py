from page.auto_login_page import AutoLoginPage
from page.custom_functions_page import CustomFunctionsPage
from page.float_ball_page import FloatBallPage
from page.home_page import HomePage
from page.image_auth_code_page import ImageAuthCodePage
from page.manually_login_page import ManuallyLoginPage
from page.my_center_page import MyCenterPage
from page.onekeyreg_login_page import OnekeyregLoginPage
from page.pay_page import PayPage
from page.phonenum_reg_page import PhonenumRegPage
from page.realname_page import RealnamePage
from page.superuser_page import SuperuserPage
from page.user_server_page import UserServerPage
from page.username_reg_page import UsernameRegPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def custom_functions(self):
        return CustomFunctionsPage(self.driver)

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def image_auth_code(self):
        return ImageAuthCodePage(self.driver)

    @property
    def manually_login(self):
        return ManuallyLoginPage(self.driver)

    @property
    def onekeyreg_login(self):
        return OnekeyregLoginPage(self.driver)

    @property
    def phonenum_reg(self):
        return PhonenumRegPage(self.driver)

    @property
    def realname(self):
        return RealnamePage(self.driver)

    @property
    def superuser(self):
        return SuperuserPage(self.driver)

    @property
    def user_server(self):
        return UserServerPage(self.driver)

    @property
    def username_reg(self):
        return UsernameRegPage(self.driver)

    @property
    def auto_login(self):
        return AutoLoginPage(self.driver)

    @property
    def float_ball(self):
        return FloatBallPage(self.driver)

    @property
    def pay(self):
        return PayPage(self.driver)

    @property
    def my_center(self):
        return MyCenterPage(self.driver)
