from page.loginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.OrderPage import OrderPage
from config.driver_config import DriverConfig

from time import sleep


class TestSearchOrderBuy:
    def test_search_order_buy(self,driver):

        LoginPage().login(driver, user="william")
        LeftMenuPage().click_level_one_menu(driver=driver, menu_name="我的订单")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver=driver, menu_name="已买到的宝贝")
        sleep(2)
        tab_list = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]
        for tab in tab_list:
            OrderPage().click_order_tab(driver=driver, tab_name=tab)
            sleep(1)


