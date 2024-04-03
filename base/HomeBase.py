class HomeBase:
    def wallet_switch(self):
        """
        首页钱包开关
        :return:
        """
        return "//span[contains(@class, 'switch']"

    def log(self):
        """
        进入系统后，首页左上角的logo
        :return:
        """
        return "//span[contains(text(),'二手']"

    def welcome(self):
        """
        首页，欢迎您回来
        :return:
        """

        return "//span[start-with(text(),'欢迎您回来')]"

