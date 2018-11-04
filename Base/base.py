import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class Base():
    def __init__(self,driver):
        self.driver=driver
     # 查找元素方法封装，给click,input等方法使用
    def base_find_element(self,loc,timeout=30,poll=0.5):
        # 封装查找元素的时候，记得使用显示等待
        # 使用driver.find_element(By.XPATH,"...")
        # 最后要通过return 进行返回元素
        return  WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))

     # 点击方法封装
    def base_click(self,loc):
        self.base_find_element(loc).click()

     # 输入方法封装
    def base_input(self,loc,text):
       el= self.base_find_element(loc)
       # 清除文本元素内容
       el.clear()
       el.send_keys(text)
    # 截图方法封装
    def base_get_screenshot(self):
        # 组合图片保存路径及文件名
        # 注意：调用的时候使用的是pytest，一定要注意路径问题 建议使用os.getcwd()
        img_path=os.getcwd()+os.sep+"Image"+os.sep+"faild.png"
        self.driver.get_screenshot_as_file(img_path)
    # 获取toast封装
    def base_get_toast(self,message):
        msg=By.XPATH,"//*[contains(@text,'"+message+"')]"
        return self.base_find_element(msg,poll=0.1).text
    # 获取元素文本方法
    def base_get_text(self,loc):
        return self.base_find_element(loc).text
    # 滑动方法封装，从一个元素滑动到另外一个元素
    def base_drag_and_drop(self,el1,el2):
        self.driver.drag_and_drop(el1,el2)