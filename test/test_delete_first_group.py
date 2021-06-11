from model.group import Group

def test_delete_first_group(app):
    if app.groupHelper.count() == 0:
        app.groupHelper.add(Group(name="Test_count", header="Test_header", footer="Test_footer"))
    old_list = app.groupHelper.get_group_list()
    app.groupHelper.delete_first_group()
    assert len(old_list) - 1 == app.groupHelper.count()
    new_list = app.groupHelper.get_group_list()
    old_list[0:1] = []
    assert old_list == new_list