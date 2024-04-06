from time import sleep

import pytest

from config.driver_config import DriverConfig


class TestPytestMClass:
    @pytest.mark.bing
    def test_open_bing(self):
        driver = DriverConfig().driver_config()
        driver.get("https://cn.bing.com")
        sleep(3)
        driver.quit()

    @pytest.mark.baidu
    def test_open_baidu(self):
        driver = DriverConfig().driver_config()
        driver.get("https://www.baidu.com")
        sleep(3)
        driver.quit()
