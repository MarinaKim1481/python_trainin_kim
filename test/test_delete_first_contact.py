def test_delete_first_contact(app):
    app.sessionHelper.login(username="admin", password="secret")
    app.contactHelper.test_delete_first_contact()
    app.sessionHelper.close_auth()