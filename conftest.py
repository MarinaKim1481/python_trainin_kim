import pytest
from fixture.application import Application

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    fixture.sessionHelper.login("admin", password="secret")
    def fin():
        fixture.sessionHelper.close_auth()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture