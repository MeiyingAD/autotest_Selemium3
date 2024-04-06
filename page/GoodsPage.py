from selenium.webdriver.common.by import By
from time import sleep

from base.GoodsBase import GoodsBase
from base.ObjectMap import ObjectMap
from common.tools import get_img_path


class GoodsPage(GoodsBase, ObjectMap):

    def inputs_goods_title(self, driver, input_value):
        """
        输入商品标题
        :param driver:
        :param input_value:
        :return:
        """
        goods_title_xpath = self.goods_title()
        return self.element_fill_value(driver=driver, locate_type=By.XPATH, locator_expression=goods_title_xpath,
                                       fill_value=input_value)

    def input_goods_details(self, driver, input_value):
        """
        输入商品详情
        :param driver:
        :param input_value:
        :return:
        """
        good_details_xpath = self.goods_details()
        return self.element_fill_value(driver=driver, locate_type=By.XPATH, locator_expression=good_details_xpath,
                                       fill_value=input_value)

    def seelect_goods_num(self, driver, num):
        """
        选择商品数量
        :param driver:
        :param num:
        :return:
        """
        goods_num_add_xpath = self.goods_num(plus=True)
        for i in range(num):
            self.element_click(driver=driver, locate_type=By.XPATH, locator_expression=goods_num_add_xpath)
            sleep(0.5)

    def upload_goods_img(self, driver, img_name):
        """
        上传物品图片
        :param driver:
        :param img_name:
        :return:
        """
        goods_img_path = get_img_path(img_name)
        upload_img_path = self.goods_img()
        return self.upload(driver=driver, locate_type=By.XPATH, locator_expression=upload_img_path,
                           file_path=goods_img_path)

    def input_goods_price(self, driver, input_value):
        """
        输入商品单价
        :param driver:
        :param input_value:
        :return:
        """
        goods_price_xpath = self.goods_price()
        return self.element_fill_value(driver=driver, locate_type=By.XPATH, locator_expression=goods_price_xpath,
                                       fill_value=input_value)

    def select_goods_status(self, driver, select_name):
        """
        选择商品状态
        :param driver:
        :param select_name:
        :return:
        """
        goods_status_xpath = self.goods_status()
        self.element_click(driver=driver, locate_type=By.XPATH, locator_expression=goods_status_xpath)
        sleep(1)
        goods_status_select_xpath = self.goods_status_select(select_name)
        return self.element_click(driver=driver, locate_type=By.XPATH,
                                  locator_expression=goods_status_select_xpath)
    def click_botton_button(self,driver, button_name):
        """
        点击底部按钮
        :param driver:
        :param button_name:
        :return:
        """
        botton_xpath =self.add_goods_bottom_button(button_name)
        return self.element_click(driver=driver, locate_type=By.XPATH,
                                  locator_expression=botton_xpath)

    def add_new_goods(self,driver, goods_title, goods_details, goods_num,goods_img_list,
                      goods_price,goods_status,bottom_button_name):
        """
        新增二手商品
        :param driver:
        :param goods_title:
        :param goods_details:
        :param goods_num:
        :param goods_img_list:
        :param goods_price:
        :param goods_status:
        :param bottom_button_name:
        :return:
        """
        self.inputs_goods_title(driver=driver,input_value=goods_title)
        self.input_goods_details(driver=driver,input_value=goods_details)
        self.seelect_goods_num(driver=driver,num=goods_num)

        for goods_img in goods_img_list:
            self.upload_goods_img(driver=driver, img_name=goods_img)
            sleep(5)

        self.input_goods_price(driver=driver,input_value=goods_price)
        self.select_goods_status(driver=driver,select_name=goods_status)
        self.click_botton_button(driver=driver,button_name=bottom_button_name)
        return True
