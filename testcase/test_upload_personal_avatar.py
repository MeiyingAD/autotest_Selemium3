from time import sleep



from page.loginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.AccountPage import AccountPage
from config.driver_config import DriverConfig




class TestUploadPersonalAvatar:
    def test_upload_personal_avatar(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver=driver,user="william")
        LeftMenuPage().click_level_one_menu(driver=driver,menu_name="账户设置")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver=driver,menu_name="个人资料")
        sleep(2)

        AccountPage().upload_avatar(driver=driver,img_name="个人头像二.jpg")
        sleep(2)
        AccountPage().click_save(driver=driver)

        driver.quit()