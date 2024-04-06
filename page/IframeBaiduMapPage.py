from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.IframeBaiduMapBase import IframeBaiduMapBase


class IframeBaiduMapPage(ObjectMap, IframeBaiduMapBase):
    def get_baidu_map_search_button(self, driver):
        """
         获取百度地铁搜索按钮
         :return:
        """
        button_xpath = self.search_button()
        return self.element_get(driver=driver, locate_type=By.XPATH, locator_expression=button_xpath)

    def switch_2_baidu_map_iframe(self, driver):
        """
        切换到百度地图的iframe
        :param driver:
        :return:
        """
        iframe_xpath = self.baidu_map_iframe()
        return self.switch_2_iframe(driver, locate_iframe_type=By.XPATH,
                                    locate_iframe_expression=iframe_xpath)

    def iframe_out(self,driver):
        """
        从百度地图iframe切回
        :param driver:
        :return:
        """
        return self.switch_from_iframe_2_content(driver=driver)