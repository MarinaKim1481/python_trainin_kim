def test_edit_group(app):
    app.sessionHelper.login("admin", password="secret")
    app.groupHelper.edit_first_group()
    app.sessionHelper.close_auth()