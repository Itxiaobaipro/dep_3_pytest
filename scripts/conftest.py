"""
1.学习目标
   
2.概念

3.语法
    3.1 conftest.py 文件名不能随意修改
    3.2 conftest.py 放置的位置,和被执行的测试用例放在同一个位置
    3.3 conftest.py 存放测试用使用的到fixture
    
4.需求

"""
import pytest


@pytest.fixture(params=[["tom", "123"], ["jerry", "234"], ["tweety", "345"]])
def login(request):
    print("用户%s,密码%s登录" % (request.param[0], request.param[1]))
