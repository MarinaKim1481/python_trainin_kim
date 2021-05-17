def delete_first_contact(app):
    app.sessionHelper.login(username="admin", password="secret")
    app.groupHelper.delete_first_contact()
    app.sessionHelper.close_auth()