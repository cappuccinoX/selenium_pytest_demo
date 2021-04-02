import pytest
import os

class TestDepends2():
    # @pytest.mark.skip()
    @pytest.mark.dependency(name="test_t1")
    def test_t1(self):
        print("\ntest_1")
        assert True


if __name__ == "__main__":
    pytest.main(["-s", "-v", f"{os.path.abspath('testcases')}/example/depends/test_depends_2.py"])