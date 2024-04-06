from base.leftMenuBase import LeftMenuBase
from base.ObjectMap import ObjectMap

from selenium.webdriver.common.by import By


class LeftMenuPage(LeftMenuBase, ObjectMap):
    def click_level_one_menu(self, driver, menu_name):
        """
        点击一级菜单
        :param driver:
        :param menu_name:
        :return:
        """
        menu_xpath = self.level_one_menu(menu_name=menu_name)
        return self.element_click(driver=driver, locate_type=By.XPATH, locator_expression=menu_xpath)

    def click_level_two_menu(self, driver, menu_name):
        """
        点击二级目录
        :param driver:
        :param menu_name:
        :return:
        """
        menu_xpath = self.level_two_menu(menu_name=menu_name)
        return self.element_click(driver=driver, locate_type=By.XPATH,locator_expression=menu_xpath)
