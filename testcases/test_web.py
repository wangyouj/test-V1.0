'''
@author : NO.47
@Date : 3/6/2021
@Function:数据驱动演示
'''
import allure
import pytest

from commons.WebAction import WebActions
from testdatas.paramsRead import datas


@allure.feature('顺丰航空交易系统web自动化测试')
class Test_web:

    @allure.title('打开浏览器')
    def setup_class(self):
        '''
        构造函数
        初始化浏览器
        :return:
        '''
        self.web = WebActions()
        self.web.openbrowser()
        print('调用浏览器成功！')



    #无数据驱动的用例

    # def test_login(self):
    #     #get website
    #     self.web.geturl('http://testingedu.com.cn:8000/index.php/Home/user/login.html')
    #
    #     self.web.input('//*[@id="username"]','13800138006')
    #     self.web.input('//*[@id="password"]','123456')
    #     self.web.input('//*[@id="verify_code"]','1111')
    #     self.web.click('class_name=J-login-submit')

    #数据驱动的用例
    @allure.story('登录')
    @pytest.mark.parametrize('listcases',datas['loginPage'])
    def test_login(self,listcases):
        '''
        登录成功的用例
        :param listcases:
        :return: None
        '''
        allure.dynamic.title(listcases['title'])
        allure.description(listcases['description'])#添加描述
        testcases=listcases['cases']
        for cases in testcases:
            listcase=list(cases.values())
            with allure.step(listcase[0]):#用例执行步骤
                func=getattr(self.web,listcase[1])
                values=listcase[2:]
                func(*values)






# def teardown_class(self):
#     self.web.quit()


# def Userinfo(self):
#     time.sleep(2)
#     self.driver.get('')
#     # switch frame
#     self.driver.switch_to_frame(self.driver.find_element_by_class_name(''))
#
#
# def search(self):
#     '''
#     login is needed
#     :return:
#     '''
#
#
# def searchNoLogin(self):
#     '''
#     ligin is not needed
#     :return:
#     '''


if __name__ == '__main__':
    comm = Test_web()
    comm.test_login()
