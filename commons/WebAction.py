'''
@author : NO.47
@Date : 3/4/2021
@Function:关键字驱动
'''
from selenium import webdriver
import time


class WebActions:
    def __init__(self):
        '''
        构造函数，创建必要的实例变量
        '''
        # self.driver=webdriver.Chrome()
        self.driver = None

    def openbrowser(self, br='gc'):
        '''
        打开浏览器
        :param br: gc=google;ff=firefox;ie=IE
        :return:
        '''
        if br=='gc':
            self.driver=webdriver.Chrome()
        elif br=='ff':
            self.driver=webdriver.firefox()
        elif br=='ie':
            self.driver=webdriver.ie()
        else:
            print('sorry 暂不支持该浏览器！')

        #设置默认隐式等待,10s
        self.driver.implicitly_wait(10)
        #浏览器最大化
        self.driver.maximize_window()


    #打开网站
    def geturl(self, url=None):
        '''

        :param url: 网站地址
        :return:
        '''
        self.driver.get(url)


    def getele(self, locator=''):
        '''
        支持6定位方式,可扩展
        :param locator:
        :return: 定位到的元素
        '''
        ele=None
        self.ele=None
        if locator.startswith('xpath='):
            ele=self.driver.find_element_by_xpath(locator[locator.find('=')+1:])
        elif locator.startswith('id='):
            ele=self.driver.find_element_by_id(locator[locator.find('=')+1:])
        elif locator.startswith('name='):
            ele=self.driver.find_element_by_name(locator[locator.find('=')+1:])
        elif locator.startswith('tag_name='):
            ele=self.driver.find_element_by_tag_name(locator[locator.find('=')+1:])
        elif locator.startswith('link_text='):
            ele=self.driver.find_element_by_link_text(locator[locator.find('=')+1:])
        elif locator.startswith('class_name='):
            ele=self.driver.find_element_by_class_name(locator[locator.find('=')+1:])
        else:
            ele=self.driver.find_element_by_xpath(locator)
        self.ele=ele
        return ele



    def click(self,locator=None):
        '''
        找到并点击元素
        :param locator: 定位器，默认xpath
        :return:
        '''
        ele=self.getele(locator)
        ele.click()


    def input(self,locator=None,value=None):
        '''

        :param locator:定位器
        :param value:输入值
        :return:
        '''
        ele=self.getele(locator)
        ele.send_keys(value)

    def getiframe(self, locator=None):
        '''
        进入ifarme
        :param locator:xpath default
        :return:
        '''
        ele=self.getele(locator)
        self.driver.switch_to.frame(ele)

    def quit(self):
        self.driver.quit()

    def sleep(self,t=2):
        time.sleep(int(t))











