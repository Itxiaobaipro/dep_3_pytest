"""
1.学习目标
   掌握pytest中fixture中addfinalizer使用
2.概念

3.语法
    终结函数--addfinalizer(函数名称)

4.需求
5.总结
    使用fixture替代setup和teardown

    -yield         不支持带返回值的fixture
    -addfinalizer  支持带返回值的fixture


"""
from selenium import webdriver
import pytest
import time


@pytest.fixture()
def open_driver(request):
    driver = webdriver.Chrome()  # 打开浏览器

    def end():
        driver.quit()  # 关闭浏览器

    request.addfinalizer(end)  # 终结函数
    return driver


# def test_baidu(open_driver):
#     """访问百度"""
#
#     open_driver.get("http://www.baidu.com/")
#     time.sleep(2)
#
#
# def test_sina(open_driver):
#     """访问新浪"""
#
#     open_driver.get("http://www.sina.com/")
#     time.sleep(2)
