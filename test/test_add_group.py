from model.group import Group

def test_add_group(app):
    old_list = app.groupHelper.get_group_list()
    app.groupHelper.add(Group(name="Test", header="Test_header", footer="Test_footer"))
    new_list = app.groupHelper.get_group_list()
    assert len(old_list) + 1 == len(new_list)

def test_add_empty_group(app):
    app.groupHelper.add(Group(name="", header="", footer=""))