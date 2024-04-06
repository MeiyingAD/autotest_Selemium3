from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.OrderBase import OrderBase

class OrderPage(OrderBase,ObjectMap):
    def click_order_tab(self,driver,tab_name):
        """
        点击订单tab栏按钮
        :param driver:
        :param tab_name:
        :return:
        """
        tab_xpath = self.order_tab(tab_name=tab_name)
        return self.element_click(driver=driver,locate_type=By.XPATH,locator_expression=tab_xpath)

