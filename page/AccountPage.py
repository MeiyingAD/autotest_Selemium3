from selenium.webdriver.common.by import By

from base.AccountBase import AccountBase
from base.ObjectMap import ObjectMap
from common.tools import get_img_path


class AccountPage(AccountBase, ObjectMap):
    def upload_avatar(self, driver, img_name):
        """
        上传个人头像
        :param driver:
        :param img_name:
        :return:
        """
        img_path = get_img_path(img_name)
        upload_xpath = self.basic_info_avatar_input()
        return self.upload(driver=driver, locate_type=By.XPATH, locator_expression=upload_xpath,
                           file_path=img_path)

    def click_save(self, driver):
        """
        个人资料--保存
        :param driver:
        :return:
        """
        button_xpath = self.basic_info_save_button()
        return self.element_click(driver=driver, locate_type=By.XPATH, locator_expression=button_xpath)





