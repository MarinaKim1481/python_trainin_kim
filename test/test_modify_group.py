from model.group import Group

def test_edit_first_group_name(app):
    old_list = app.groupHelper.get_group_list()
    app.groupHelper.edit_first_group_name(Group(name='New name'))
    new_list = app.groupHelper.get_group_list()
    assert len(old_list) == len(new_list)

def test_edit_first_group_header(app):
    old_list = app.groupHelper.get_group_list()
    app.groupHelper.edit_first_group_header(Group(header='New header'))
    new_list = app.groupHelper.get_group_list()
    assert len(old_list) == len(new_list)