from time import sleep


from page.loginPage import LoginPage
from page.ActionChainPage import ActionChainPage

from config.driver_config import DriverConfig



class TestClickExit:
    def test_text_click_exit(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver=driver,user="william")
        sleep(2)
        ActionChainPage().mouse_move_to_list(driver=driver)
        sleep(2)
        ActionChainPage().click_exit_button(driver=driver)
        sleep(10)
        driver.quit()


