def test_delete_first_contact(app):
    app.sessionHelper.login(username="admin", password="secret")
    app.contactHelper.delete_first_contact()
    app.sessionHelper.close_auth()