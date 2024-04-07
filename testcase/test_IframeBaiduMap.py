from time import sleep

from page.loginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.IframeBaiduMapPage import IframeBaiduMapPage
from config.driver_config import DriverConfig


class TestIframeBaiduMap:
    def test_IframeBaiduMap(self,driver):

        LoginPage().login(driver=driver, user="william")
        LeftMenuPage().click_level_one_menu(driver=driver, menu_name="iframe测试")
        sleep(1)
        IframeBaiduMapPage().switch_2_baidu_map_iframe(driver=driver)
        IframeBaiduMapPage().get_baidu_map_search_button(driver=driver)
        IframeBaiduMapPage().iframe_out(driver=driver)
        LeftMenuPage().click_level_one_menu(driver, menu_name="首页")
        sleep(3)

