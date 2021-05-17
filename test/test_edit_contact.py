def test_edit_contact(app):
    app.sessionHelper.login(username="admin", password="secret")
    app.contactHelper.test_edit_contact()
    app.sessionHelper.close_auth()