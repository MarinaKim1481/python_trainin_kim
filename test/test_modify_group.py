from model.group import Group

def test_edit_first_group_name(app):
    app.groupHelper.edit_first_group_name(Group(name='New name'))

def test_edit_first_group_header(app):
    app.groupHelper.edit_first_group_header(Group(header='New header'))