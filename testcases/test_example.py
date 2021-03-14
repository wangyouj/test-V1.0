'''
@author : NO.47
@Date : 3/2/2021
@Function:参数化实例
'''
import pytest


def sum(x,y):
    return x+y

params=[
    [1, 2, 3],
    [3, 5, 8],
    [4, 7, 10],
    [9, -2, 7]
]

class Test_Data:

    @pytest.mark.parametrize('x,y,z',params)
    def test_sum2(self,x,y,z):
        assert sum(x,y)==z

