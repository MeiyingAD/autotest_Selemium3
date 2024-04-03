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

        return "//span[starts-with(text(),'欢迎您回来')]"

    def show_data(self):
        """
        首页显示日期
        :return:
        """
        return "//div[text()='我的日历']/following-sibling::div"  # following-sibling方法用于找到元素同级的下一个元素

    def home_user_avatar(self):
        """
        首页用户头像大图
        :return:
        """
        return "//span[starts-with(text(),'欢迎您回来')]/parent::div/preceding-sibling::div//img"  # preceding-sibling方法用于找到元素同级的上一个元素
                                                                                                 # parent方法用于找到元素的父亲

    def home_user_avatar2(self):
        """
        首页用户头像大图
        :return:
        """
        return "//span[text()='我的地址']/ancestor::div[@class='first_card']/div[contains(@class,'avatar')]//img" #ancestor方法--祖先方法，用于寻找祖先元素