from model.group import Group

def test_add_group(app):
    app.sessionHelper.login(username="admin", password="secret")
    app.groupHelper.add(Group(name="Test", header="Test_header", footer="Test_footer"))
    app.sessionHelper.close_auth()

def test_add_empty_group(app):
    app.sessionHelper.login(username="admin", password="secret")
    app.groupHelper.add(Group(name="", header="", footer=""))
    app.sessionHelper.close_auth()
