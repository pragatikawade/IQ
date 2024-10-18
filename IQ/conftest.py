import pytest

@pytest.fixture(autouse=True,scope='function')
def my_fixture():
    print("this is common fixture file And it is being called======================")
