'''
@author : NO.47
@Date : 3/7/2021
@Function: read yaml
'''
import yaml

#读取数据驱动的驱动
with open('./testdatas/cases', encoding='utf8') as f:
    datas=yaml.safe_load(f)

print(datas)


