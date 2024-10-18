from sys import modules

import pytest
import test_fixture1

class Test2:

    @pytest.fixture(autouse=True, scope='class')
    def my_fixture(self):
        print("this is fclass2 fixture called ------------")

    def test_fun1(self):
        print("\n this is function3 & it is called")

    def test_fun2(self):
        print("this is function4 & it is called")
