import sys,os
sys.path.append(os.getcwd())
import pytest
from Base.read_yaml import ReadYaml
import allure
from Page.page_in import PageIn

def get_data():
    arrs=[]
    for data in ReadYaml("login_data.yaml").read_yaml().values():
        arrs.append((data.get("username"),data.get("password"),data.get("except_result"),data.get("except_toast")))
    return arrs

class TestLogin():
    @allure.step("开始执行初始化函数")
    def setup_class(self):
        # 实例化统一入口类
        self.page=PageIn()
        self.login= self.page.page_get_login()
        self.login.page_click_me()
        self.login.page_click_me_ok_link()

    def teardown_class(self):
        self.login.driver.quit()
    @pytest.mark.parametrize("username,password,except_result,except_toast",get_data())
    def test_login(self,username,password,except_result,except_toast):
        if except_result:
            # 断言
            try:
                # 输入用户名
                self.login.page_input_username(username)
                # 输入密码
                self.login.page_input_pwd(password)
                # 点击登陆
                self.login.page_click_login_btn()
                # 获取昵称
                nickname = self.login.page_get_nickname()
                assert except_result in nickname
                # 点击设置
                self.login.page_click_setting()
                # 滑动消息推送到密码修改
                self.login.page_drag_and_drop()
                # 点击退出
                self.login.page_click_exit_btn()
                # 确认退出按钮
                self.login.page_ok_exit_btn()
                # 点击我
                self.login.page_click_me()
                # 点击已有账号，登录
                self.login.page_click_me_ok_link()
            except:
                self.login.base_get_screenshot()
                with open("./Image/faild.png","rb") as f:
                        allure.attach("失败原因查看截图",f.read(),allure.attach_type.PNG)
                raise

        else:
            try:
                # 输入用户名
                self.login.page_input_username(username)
                # 输入密码
                self.login.page_input_pwd(password)
                # 点击登陆
                self.login.page_click_login_btn()
                # 断言
                assert except_toast in self.login.base_get_toast(except_toast)
            except:
                self.login.base_get_screenshot()
                with open("./Image/faild.png", "rb") as f:
                    allure.attach("失败原因查看截图", f.read(), allure.attach_type.PNG)
                raise