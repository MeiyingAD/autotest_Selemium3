import time
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException, \
    StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from common.yaml_config import GetConf
from common.tools import get_project_path, sep
from common.find_img import FindImg


class ObjectMap:
    # 获取基本地址
    base_url = GetConf().get_url()

    def element_get(self, driver, locate_type, locator_expression, timeout=10, must_be_visible=False):
        """
        单个元素获取
        :param driver: 浏览器驱动
        :param locate_type: 定位方式类型
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :param must_be_visible:元素是否必须可见
        :return:
        """
        # 开始时间
        start_ms = time.time() * 1000
        # 设置的结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            # TOdO 查找元素
            try:
                element = driver.find_element(by=locate_type, value=locator_expression)
                # 如果元素不是必须可见的
                if not must_be_visible:
                    return element
                # 如果元素是必须可见的，则需要判断元素是否可见
                else:
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()

            except Exception:
                now_time = time.time() * 1000
                if now_time >= stop_ms:
                    break
                time.sleep(0.1)
        raise ElementNotVisibleException("元素定位失败，定位方式：" + locate_type + "定位表达式" + locator_expression)

    def wait_for_ready_state_complete(self, driver, timeout=30):
        """
        等待页面完全加载完成
        :param driver:
        :param timeout:
        :return:
        """
        # 开始时间
        start_ms = time.time() * 1000.0
        # 设置的结束时间
        stop_ms = start_ms + (timeout * 1000.0)

        for x in range(int(timeout * 10)):
            try:
                # 获取页面的一个 "是否准备完成" 的属性
                ready_state = driver.execute_script("return document.readyState")
            except WebDriverException:
                # 如果有driver错误，执行js会失败，就直接跳过
                time.sleep(0.03)
                return True
            # 如果页面元素全部加载完，返回True
            if ready_state == "complete":
                time.sleep(0.01)
                return True
            else:
                now_ms = time.time() * 1000.0
                # 如果超时了就break
                if now_ms >= stop_ms:
                    break
                time.sleep(0.1)
        raise Exception("打开网页时，页面元素在%s秒后仍然没有完全加载完" % timeout)

    def element_disappear(self, driver, locate_type, locator_expression, timeout=30):
        """
        等待页面元素消失
        :param driver: 浏览器驱动
        :param locate_type: 定位方式类型
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :return:
        """
        if locate_type:
            # 开始时间
            start_ms = time.time() * 1000.0
            # 结束时间
            stop_ms = start_ms + (timeout * 1000.0)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        now_ms = time.time() * 1000.0
                        if now_ms >= stop_ms:
                            break
                        time.sleep(0.1)

                except Exception:
                    return True

            raise Exception("元素没有消失，定位方式：" + locate_type + "\n定位表达式：" + locator_expression)
        else:
            pass

    def element_appear(self, driver, locate_type, locator_expression, timeout=30):
        """
        等待页面元素出现
        :param driver: 浏览器驱动
        :param locate_type: 定位方式类型
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :return: 元素出现返回True
        """
        if locate_type:
            # 开始时间
            start_ms = time.time() * 1000.0
            # 设置的结束时间
            stop_ms = start_ms + (timeout * 1000.0)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(
                        by=locate_type, value=locator_expression
                    )
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    now_ms = time.time() * 1000.0
                    if now_ms >= stop_ms:
                        break
                    time.sleep(0.1)
            raise ElementNotVisibleException(
                "元素没有出现,定位方式:" + locate_type + " 定位表达式:" + locator_expression
            )
        else:
            pass

    def element_to_url(self,
                       driver,
                       url,
                       locate_type_disappear=None,
                       locator_expression_disappear=None,
                       locate_type_appear=None,
                       locator_expression_appear=None
                       ):
        """
        跳转地址
        :param driver: 浏览器驱动
        :param url: 跳转的地址
        :param locate_type_disappear:等待页面元素消失的定位方式
        :param locator_expression_disappear: 等待页面元素消失的定位表达式
        :param locate_type_appear:等待页面元素出现的定位方式
        :param locator_expression_appear:等待页面元素出现的定位表达式
        :return:
        """
        try:
            driver.get(self.base_url + url)
            # 等待页面元素加载完成
            self.wait_for_ready_state_complete(driver)

            # 跳转地址后等待页面元素消失
            self.element_disappear(driver,
                                   locate_type_disappear,
                                   locator_expression_disappear
                                   )

            # 跳转地址后等待元素出现
            self.element_appear(driver,
                                locate_type_appear,
                                locator_expression_appear
                                )
        except Exception as e:
            print(f"跳转地址失败异常原因{e}")
            return False

    def element_is_display(self, driver, locate_type, locator_expression):
        """
        元素是否显示
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :return:
        """
        try:
            driver.find_element(by=locate_type, value=locator_expression)
            return True
        except NoSuchElementException:
            # 未找到该元素，返回False
            return False

    def element_fill_value(self, driver, locate_type, locator_expression, fill_value, timeout=30):
        """
        元素填值（先清除元素中的值，再填值，如果填入的值以‘/n’结尾，则自动回车，输入值后检测输入的值是否与入参一致）
        :param driver:浏览器驱动
        :param locate_type:定位方式类型
        :param locator_expression:定位表达式
        :param fill_value:填入的值
        :param timeout:超时时间
        :return:
        """
        # 元素必须先出现
        element = self.element_appear(driver,
                                      locate_type=locate_type,
                                      locator_expression=locator_expression,
                                      timeout=timeout
                                      )
        try:
            # 清除元素中的原有值
            element.clear()
        except StaleElementReferenceException:  # 页面元素没有刷新出来，就对元素进行捕获
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(driver,
                                          locate_type=locate_type,
                                          locator_expression=locator_expression,
                                          timeout=timeout
                                          )

            try:
                element.clear()
            except Exception:
                pass
        except Exception:
            pass
        if type(fill_value) is int or type(fill_value) is float:
            fill_value = str(fill_value)
        try:
            if not fill_value.endswith("\n"):
                # 不是以\n 结尾
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)

            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.ENTER)
                self.wait_for_ready_state_complete(driver=driver)
        except StaleElementReferenceException as s:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(driver, locate_type=locate_type, locator_expression=locator_expression)
            element.clear()
            if not fill_value.endswith("\n"):
                # 不是以\n 结尾
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)

            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.ENTER)
                self.wait_for_ready_state_complete(driver=driver)
        except Exception:
            return Exception("元素填值失败")

        return True

    def element_click(
            self,
            driver,
            locate_type,
            locator_expression,
            wait_for_locate_type=None,
            wait_for_locator_expression=None,
            wait_for_disappear_locate_type=None,
            wait_for_disappear_locator_expression=None,
            timeout=30,
    ):
        """
        元素点击
        :param driver: 浏览器驱动
        :param locate_type: 定位方式类型
        :param locator_expression: 定位表达式
        :param wait_for_locate_type: 等待元素出现的元素定位方式类型
        :param wait_for_locator_expression: 等待元素出现的元素定位表达式
        :param wait_for_disappear_locate_type:等待元素消失的元素定位方式类型
        :param wait_for_disappear_locator_expression:等待元素消失的元素定位表达式
        :param timeout:
        :return:
        """
        # 元素要可见
        element = self.element_appear(
            driver=driver,
            locate_type=locate_type,
            locator_expression=locator_expression,
            timeout=timeout,
        )
        try:
            # 点击元素
            element.click()
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.05)
            element = self.element_appear(
                driver=driver,
                locate_type=locate_type,
                locator_expression=locator_expression,
                timeout=timeout,
            )
            element.click()
        except Exception as e:
            print("页面出现异常，元素不可点击", e)
            return False

        try:
            # 点击元素后的元素出现或元素消失
            self.element_appear(
                driver, wait_for_locate_type, wait_for_locator_expression
            )
            self.element_disappear(
                driver,
                wait_for_disappear_locate_type,
                wait_for_disappear_locator_expression,
            )
        except Exception as e:
            print("等待元素消失或出现失败", e)
            return False
        return True

    def upload(self, driver, locate_type, locator_expression, file_path):
        """
        文件上传
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param file_path:
        :return:
        """
        element = self.element_get(driver=driver, locate_type=locate_type, locator_expression=locator_expression)
        return element.send_keys(file_path)

    def switch_window_2_latest_handle(self, driver):
        """
        句柄切换窗口到最新的窗口
        :param driver:
        :return:
        """
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])

    def switch_2_iframe(self, driver, locate_iframe_type, locate_iframe_expression):
        """
        进入iframe
        :param driver:浏览器驱动
        :param locate_iframe_type:定位iframe的方式
        :param locate_iframe_expression:定位iframe的表达式
        :return:
        """
        iframe = self.element_get(driver=driver, locate_type=locate_iframe_type,
                                  locator_expression=locate_iframe_expression)
        driver.switch_to.frame(iframe)

    def switch_from_iframe_2_content(self, driver):
        """
        从iframe切回主文档
        :param driver:
        :return:
        """
        driver.switch_to.parent_frame()

    def ActionChains_click(self, driver, action_chains):
        """
        单击退出
        :param driver:
        :param action_chains:
        :return:
        """
        action = ActionChains(driver)
        action.click(action_chains).perform()

    def ActionChains_move(self, driver, action_chains):
        """
        光标移动
        :param driver:
        :param action_chains:
        :return:
        """
        action = ActionChains(driver)
        action.move_to_element(action_chains).perform()

    def find_img_in_source(self, driver, img_name):
        """
        截图并在截图中查找图片
        :param driver:
        :param img_name:
        :return:
        """
        # 截图后图片保存的路径
        source_img_path = get_project_path() + sep(["img", "source_img", img_name])
        # 需要查找的图片的路径
        search_img_path = get_project_path() + sep(["img", "assert_img", img_name])
        # 截图并保存图片
        driver.get_screenshot_as_file(source_img_path)
        time.sleep(3)
        # 在原图中查找是否有指定的图片
        confidence = FindImg().get_confidence(source_img_path, search_img_path)
        return confidence
