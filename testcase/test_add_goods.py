from time import sleep

from config.driver_config import DriverConfig
from page.loginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage


class TestAddGoods:
    def test_add_goods(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver,"william")
        LeftMenuPage().click_level_one_menu(driver,"产品")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver,"新增二手商品")
        sleep(2)
        GoodsPage().add_new_goods(
                                  driver=driver,
                                  goods_title="商品一",
                                  goods_price=1000,
                                  goods_details="测试",
                                  goods_num=10,
                                  goods_img_list=["商品图片一.jpg"],
                                  goods_status="上架",
                                  bottom_button_name="提交"
                                  )
        sleep(3)
        driver.quit()
