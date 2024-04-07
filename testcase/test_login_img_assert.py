from time import sleep
import pytest

from page.loginPage import LoginPage


class TestLoginImgAssert:
    def test_login_img_assert(self, driver):
        """
        登录后断言图片
        :return:
        """
        LoginPage().login(driver, "william")
        sleep(3)
        assert LoginPage().login_assert(driver, "head_img.png") > 0.9
