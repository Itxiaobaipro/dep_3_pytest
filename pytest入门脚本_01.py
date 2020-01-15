"""
1.学习目标
   掌握在pytest框架下测试用例编写
2.概念

3.语法(操作步骤)
    测试函数:
        在py文件中以test开头的函数
    测试方法:
        在测试类中,以test开头的方法
    测试类:
        在py文件中以Test开头的类
    测试模块:
        py文件名以test开头命名
    编写步骤:
        1.导入pytest
        2.编写测试函数:
        3.执行测试函数
    
4.需求
5.总结
    在pytest框架下编写测试用例,
    1.可以将测试用例写成函数,测试函数必须以test开头
    2.pytest中的断言使用的是python自带的断言方式 assert关键字

        assert 条件表达式  ===,>,< in ,not in
        只有assert后条件表达式为True,表示断言成功,为False时,断言失败

    3.在pytest中,执行结果: .  表示用例通过
                           F  表示用例失败

"""
# 1.导入pytest
import pytest
# 2.编写测试用例
def test_register():
    print("输入用户名")
    print("输入邮箱")
    print("输入密码")
    print("点击注册")
    assert "user"in["user","password"]

def test_shopping():
    print("执行购物测试用例")
    assert 100 == 200-90  # 用户余额=购物前余额-商品价格
# 3.执行测试用例
if __name__ == '__main__':
    pytest.main(["-s","-v"])

