from page.loginPage import LoginPage
from page.ExternalLinkPage import ExternalLinkPage
from page.LeftMenuPage import LeftMenuPage
from config.driver_config import DriverConfig

from time import sleep


class TestSwitchWindowHandle:
    def test_switch_window_handle(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver=driver, user="william")
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver=driver, menu_name="外链")
        sleep(1)
        title = ExternalLinkPage().goto_imooc(driver=driver)
        print(title)
        driver.quit()
