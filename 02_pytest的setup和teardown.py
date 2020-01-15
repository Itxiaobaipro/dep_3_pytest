"""
1.学习目标
   掌握pytest中setup和teardown的使用
2.概念
    测试用例执行前的准备和执行后数据处理
3.语法(作用域)
    模块级别   setup_module/teardown_module         作用域针对整个.py文件   执行一次
    类级别     setup_class/teardown_class           作用域针对测试类        执行一次
    方法级别   setup_method/teardown_method         作用域针对测试类中的测试方法   执行次数和方法的个数相同
    函数级别   setup_function/teardown_function     作用域针对.py文件中的函数      执行次数和函数的个数相同
    
4.需求
5.总结

"""
# 1.导入pytest
import pytest

def setup_module():
    print("模块级别的setup")

def setup_function():
    print("函数级别的setup")


def teardown_function():
    print("函数级别的teardown")

def test_login():
    print("执行登录测试用例")
    assert True


class TestCart:
    def setup_class(self):
        print("类级别的setup")

    def teardown_class(self):
        print("类级别的teardown")

    def setup_method(self):
        print("方法级别setup")

    def test_add_cart(self):
        print("执行添加购物车用例")
        assert True



if __name__ == '__main__':
    pytest.main()
