"""
1.学习目标
   掌握pytest中fixture写法
2.概念

3.语法
    fixture写法:
        在普通函数前使用@pytest.fixture()装饰即可
        @pytest.fixture()
        def login():
            登录函数

        fixture名称就是函数名称

    fixture使用:
        将fixture当做参数传入需要使用的测试用例中

        def test_case(login):
            测试步骤

    fixture执行顺序:
        当运行测试用例时,先执行fixture,然后执行用例

4.需求

"""
import pytest

"""
在执行测试用例的过程中,有的用例需要登录,有的不需要登录,使用fixture实现
在同一文件下,不同的执行方式
"""


#
# def setup():
#     print("登录成功!")
# @pytest.fixture()
# def login():
#     print("登录成功!")


def test_get_address(login):
    print("进入个人中心,查看收货地址")


def test_get_collection(login):
    print("进入个人中心,查看收藏夹")


def test_browser_goods():
    print("不需要登录,直接浏览")
