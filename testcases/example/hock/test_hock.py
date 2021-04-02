import pytest

def setup_module():
    print('\nsetup module')

def teardown_module():
    print('\nteardown module')

def setup_function():
    print("\nsetup function")

def teardown_function():
    print("\nteardown function")

class Test1():

    @classmethod
    def setup_class(cls):
        print("\nsetup class")

    @classmethod
    def teardown_class(cls):
        print(("\nteardown class"))

    def setup_method(self):
        print("setup method")

    def teardown_method(self):
        print("teardown method")

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def test_1(self):
        assert 1 == 1

    def test_2(self):
        assert 2 == 2

# https://www.wjx.cn/jq/37766520.aspx 测试问卷填写