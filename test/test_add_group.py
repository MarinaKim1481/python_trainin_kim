from model.group import Group

def test_add_group(app):
    old_list = app.groupHelper.get_group_list()
    group = Group(name="Test", header="Test_header", footer="Test_footer")
    app.groupHelper.add(group)
    assert len(old_list) + 1 == app.groupHelper.count()
    new_list = app.groupHelper.get_group_list()
    old_list.append(group)
    assert(sorted(old_list, key=Group.id_or_max)) == (sorted(new_list, key=Group.id_or_max))

def test_add_empty_group(app):
    old_list = app.groupHelper.get_group_list()
    group = Group(name="", header="", footer="")
    app.groupHelper.add(group)
    assert len(old_list) + 1 == app.groupHelper.count()
    new_list = app.groupHelper.get_group_list()
    old_list.append(group)
    assert(sorted(old_list, key=Group.id_or_max)) == (sorted(new_list, key=Group.id_or_max))