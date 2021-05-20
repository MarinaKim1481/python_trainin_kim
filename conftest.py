import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.sessionHelper.login("admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.sessionHelper.login("admin", password="secret")
    return fixture

@pytest.fixture (scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.sessionHelper.close_auth()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture