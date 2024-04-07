from page.loginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.OrderPage import OrderPage
from config.driver_config import DriverConfig

from time import sleep
import pytest

tab_list = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]
class TestSearchOrderBuy:
    @pytest.mark.parametrize("tab", tab_list)
    def test_search_order_buy(self,driver,tab):

        LoginPage().login(driver, user="william")
        LeftMenuPage().click_level_one_menu(driver=driver, menu_name="我的订单")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver=driver, menu_name="已买到的宝贝")
        sleep(2)
        OrderPage().click_order_tab(driver=driver, tab_name=tab)
        sleep(1)


