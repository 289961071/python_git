#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路
import unittest
class case(unittest.TestCase):
    def setUp(self):
        print('前置工作')
    def tearDown(self):
        print('后置工作')
    @classmethod
    def test_1(self):
        print('1业务')
    #skip装饰器一共有三个 unittest.skip(reason)、unittest.skipIf(condition,reason)、unittest.skipUnless(condition,reason)，
    # skip无条件跳过，skipIf当condition为True时跳过，skipUnless当condition为False时跳过。
    #每个测试方法均以 test 开头，否则是不被unittest识别的。
    @unittest.skip('跳过这个用例')
    def test_2(self):
        print('2业务')
if  __name__=="__main__":
    # 使用main()直接运行时，将按case的名称顺序执行
    #在unittest.main()中加 verbosity 参数
    # 可以控制输出的错误报告的详细程度，默认是 1，如果设为 0，则不输出每一用例的执行结果。
    # 如果参数为2则表示输出详细结果
    unittest.main(verbosity=2)

    # 1、构造用例集
    suite = unittest.TestSuite()
    # 2、执行顺序是安加载顺序：先执行test_sub，再执行test_add
    suite.addTest(TestOne("test_sub"))
    suite.addTest(TestOne("test_add"))
    # 3、实例化runner类
    runner = unittest.TextTestRunner()
    # 4、执行测试
    runner.run(suite)