from model.group import Group

def test_edit_first_group_name(app):
    old_list = app.groupHelper.get_group_list()
    group = Group(name='New name')
    group.id = old_list[0].id
    app.groupHelper.edit_first_group_name(group)
    new_list = app.groupHelper.get_group_list()
    assert len(old_list) == len(new_list)
    old_list[0] = group
    assert(sorted(old_list, key=Group.id_or_max)) == (sorted(new_list, key=Group.id_or_max))

#def test_edit_first_group_header(app):
#    old_list = app.groupHelper.get_group_list()
#    app.groupHelper.edit_first_group_header(Group(header='New header'))
#    new_list = app.groupHelper.get_group_list()
#    assert len(old_list) == len(new_list)