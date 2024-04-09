from page.loginPage import LoginPage
from page.ExternalLinkPage import ExternalLinkPage
from page.LeftMenuPage import LeftMenuPage
from config.driver_config import DriverConfig
from common.report_add_img import add_img_2_report


from time import sleep
import allure


class TestSwitchWindowHandle:
    @allure.description("窗口句柄")
    def test_switch_window_handle(self, driver):
        with allure.step("登录"):
            LoginPage().login(driver=driver, user="william")
            sleep(3)
            add_img_2_report(driver=driver,step_name="登录")

        with allure.step("点击外链"):
            LeftMenuPage().click_level_one_menu(driver=driver, menu_name="外链")
            sleep(1)
            add_img_2_report(driver=driver, step_name="点击外链")

        with allure.step("断言title"):
            title = ExternalLinkPage().goto_imooc(driver=driver)
            print(title)
            assert title == "慕课网-程序员的梦工厂"
