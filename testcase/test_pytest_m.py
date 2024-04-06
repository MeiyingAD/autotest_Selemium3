from time import sleep

import pytest

from config.driver_config import DriverConfig


class TestPytestMClass:

    @pytest.fixture(scope="class")
    def scope_class(self):
        print("scope_class,只执行一次")
    @pytest.fixture(scope="function")
    def driver(self):
        driver_ = DriverConfig().driver_config()
        return driver_
    @pytest.mark.bing
    def test_open_bing(self,driver,scope_class):

        driver.get("https://cn.bing.com")
        sleep(3)
        driver.quit()

    @pytest.mark.baidu
    def test_open_baidu(self,driver,scope_class):
        driver.get("https://www.baidu.com")
        sleep(3)
        driver.quit()
