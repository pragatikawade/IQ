from sys import modules

import pytest


class Test:

    @pytest.fixture(autouse=True,scope='function')
    def my_fixture(self):
        print("this is fixture function & it is called ------------")

    def test_fun1(self):
        print("\n this is function1 & it is called")

    def test_fun2(self):
        print("this is function2 & it is called")
