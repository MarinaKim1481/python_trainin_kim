def test_edit_contact(app):
    app.sessionHelper.login("admin", password="secret")
    app.contactHelper.edit_first_contact()
    app.sessionHelper.close_auth()