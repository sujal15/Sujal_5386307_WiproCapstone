import pytest


@pytest.fixture(scope='function', autouse=True)
def setup_teardown():
    print("Start")
    yield
    print("End")
