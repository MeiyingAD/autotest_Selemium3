from selenium.webdriver.common.by import By

from base.login_base import LoginBase
from base.ObjectMap import ObjectMap
from common.yaml_config import GetConf


class LoginPage(LoginBase, ObjectMap):
    def login_input_value(self, driver, input_placeholder, input_value):
        """
        登录页输入值
        :param driver:
        :param input_placeholder:
        :param input_value:
        :return:
        """
        input_xpath = self.login_input(input_placeholder)
        return self.element_fill_value(driver=driver, locate_type=By.XPATH, locator_expression=input_xpath,
                                       fill_value=input_value)

    def click_login(self, driver, button_name):
        """
        点击登录
        :param driver:
        :param button_name:
        :return:
        """
        button_xpath = self.login_button(button_name)
        return self.element_click(driver=driver, locate_type=By.XPATH, locator_expression=button_xpath)

    def login(self, driver, user):
        """
        登入
        :param driver:
        :param user:
        :return:
        """
        self.element_to_url(driver, "/login")
        username, password = GetConf().get_username_password(user)
        self.login_input_value(driver=driver, input_placeholder="用户名", input_value=username)
        self.login_input_value(driver=driver, input_placeholder="密码", input_value=password)
        self.click_login(driver, button_name="登录")

    def login_assert(self, driver, img_name):
        """
        登录后判断头像
        :param driver:
        :param img_name:
        :return:
        """
        return self.find_img_in_source(driver, img_name)
