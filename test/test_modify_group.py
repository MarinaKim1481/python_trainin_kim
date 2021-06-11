from model.group import Group
from random import randrange

def test_edit_some_group(app):
    if app.groupHelper.count() == 0:
        app.groupHelper.add(Group(name="Test_count", header="Test_header", footer="Test_footer"))
    old_list = app.groupHelper.get_group_list()
    index = randrange(len(old_list))
    group = Group(name='New name')
    group.id = old_list[index].id
    app.groupHelper.edit_group_by_index(index, group)
    assert len(old_list) == app.groupHelper.count()
    new_list = app.groupHelper.get_group_list()
    old_list[index] = group
    assert(sorted(old_list, key=Group.id_or_max)) == (sorted(new_list, key=Group.id_or_max))

#def test_edit_first_group_header(app):
#    old_list = app.groupHelper.get_group_list()
#    app.groupHelper.edit_first_group_header(Group(header='New header'))
#    new_list = app.groupHelper.get_group_list()
#    assert len(old_list) == len(new_list)