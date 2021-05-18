import pytest
from fixture.application import Application

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    fixture.sessionHelper.login("admin", password="secret")
    request.addfinalizer(fixture.destroy)
    return fixture
    fixture.sessionHelper.close_auth("admin", "secret")