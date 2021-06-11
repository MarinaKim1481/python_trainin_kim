from random import randrange
from model.group import Group

def test_delete_some_group(app):
    if app.groupHelper.count() == 0:
        app.groupHelper.add(Group(name="Test_count", header="Test_header", footer="Test_footer"))
    old_list = app.groupHelper.get_group_list()
    index = randrange(len(old_list))
    app.groupHelper.delete_group_by_index(index)
    assert len(old_list) - 1 == app.groupHelper.count()
    new_list = app.groupHelper.get_group_list()
    old_list[index:index+1] = []
    assert old_list == new_list