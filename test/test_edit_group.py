def test_edit_group(app):
    app.sessionHelper.login(username="admin", password="secret")
    app.groupHelper.test_edit_group()
    app.sessionHelper.close_auth()