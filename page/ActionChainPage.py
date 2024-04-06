from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.ActionChainsBase import ActionChainsBase


class ActionChainPage(ObjectMap, ActionChainsBase):
    def click_exit_button(self, driver):
        button_xpath = self.click_exit()
        action_chain = self.element_get(driver,locate_type=By.XPATH,locator_expression=button_xpath)
        return self.ActionChains_click(driver=driver, action_chains=action_chain)

    def mouse_move_to_list(self, driver):
        _xpath = self.move_end()
        action_chain = self.element_get(driver=driver,locate_type=By.XPATH,locator_expression=_xpath)
        return self.ActionChains_move(driver=driver, action_chains=action_chain)

    def mouse_move_to_exit_button(self,driver):
        _xpath = self.click_exit()
        action_chain = self.element_get(driver=driver,locate_type=By.XPATH,locator_expression=_xpath)
        return self.ActionChains_move(driver=driver, action_chains=action_chain)