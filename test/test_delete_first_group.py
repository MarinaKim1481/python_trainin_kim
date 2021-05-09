def test_delete_first_group(app):
    app.sessionHelper.login(username="admin", password="secret")
    app.groupHelper.delete_first_group()
    app.sessionHelper.close_auth()