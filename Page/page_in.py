# 说明：统一入口管理类，主要解决一下两个方面
#   1.对Page页面对象统一进行管理
#   2，解决批量导入PAGE问题
from Base.get_driver import get_driver
from Page.page_address import PageAddress
from Page.page_login import PageLogin
class PageIn():
    def __init__(self):
        self.driver=get_driver()
    # 获取page_login页面对象
    def page_get_login(self):
        return PageLogin(self.driver)
    # 获取page_address页面对象
    def page_get_address(self):
        return PageAddress(self.driver)