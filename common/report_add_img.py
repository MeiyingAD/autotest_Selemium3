from time import sleep

import allure


def add_img_2_report(driver, step_name, need_sleep=True):
    """
    截图并插入allure报告
    Args:
        driver: 浏览器驱动
        step_name: 步骤名称
        need_sleep:

    Returns:

    """
    if need_sleep:
        sleep(2)
    allure.attach(
        driver.get_screenshot_as_png(),
        step_name + ".png",
        allure.attachment_type.PNG
    )
