"""
1.学习目标
   使用一个fixture同时实现setup和teardown
2.概念

3.语法
    yield
4.需求

"""
import pytest


# def setup():
#     print("连接数据库,准备测试数据")
#
#
# def teardown():
#     print("清除测试数据,关闭数据库连接")
@pytest.fixture()
def operation_database():
    print("连接数据库,准备测试数据")

    yield
    print("清除测试数据,关闭数据库连接")


def test_register(operation_database):
    print("执行注册用例")
