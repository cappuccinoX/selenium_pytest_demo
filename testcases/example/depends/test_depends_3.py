'''
使用pytest_dependency的坑
test_t3 依赖于 test_t1
如果 test_depends_2 文件位于 test_depends_3文件之前, test_t3是否执行取决于test_t1是否pass
如果 test_depends_2 文件位于 test_depends_3文件之后, test_t3会先执行, 因为依赖于test_t1, 而test_t1此时并没有执行, 导致test_t3会跳过
'''

import pytest
import sys, os
sys.path.append(os.getcwd())
from testcases.example.depends import TestDepends2
# from pytest_dependency import depends

class TestDepends3():

    def setup_class(self):
        self.x = TestDepends2()

    @pytest.mark.dependency(name="bb", depends=["test_t1"], scope="module")
    def test_t3(self):
        print("\ntest_t3")
        assert True
    
# class TestDepends1():

#     # def setup_class(self):
#         # self.x = TestDepends1()

#     @pytest.mark.dependency(depends=["bb"])
#     def test_t2(self):
#         print("\ntest_t2")
#         assert 1==1


  

if __name__ == "__main__":
    pytest.main(["-s", "-v", f"{os.path.abspath('testcases')}/example/depends/test_depends_3.py"])