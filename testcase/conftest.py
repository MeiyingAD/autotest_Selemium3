import pytest

from config.driver_config import DriverConfig


@pytest.fixture()
def driver():
    get_driver = DriverConfig().driver_config()
    yield get_driver
    get_driver.quit()


def pytest_collection_finish(session):
    print("当前执行测试的用例数为：" + str(len(session.items)))
