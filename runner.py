#author : NO.47
#Date : 2/28/2021

'''
运行入口
'''
import os
import pytest



pytest.main(['-s','testcases\\test_example.py','testcases\\test_web.py','--alluredir','./temp'])
os.system('allure generate ./temp -o ./report --clean')

#pytest --html=./reportX/reportX.html










