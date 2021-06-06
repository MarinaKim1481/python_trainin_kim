from model.group import Group

def test_edit_group(app):
    if app.groupHelper.count() == 0:
        app.groupHelper.add(Group(name="Test_count", header="Test_header", footer="Test_footer"))
    old_list = app.groupHelper.get_group_list()
    app.groupHelper.edit_first_group()
    new_list = app.groupHelper.get_group_list()
    assert len(old_list) == len(new_list)