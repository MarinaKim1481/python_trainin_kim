from model.group import Group

def test_edit_group(app):
    if app.groupHelper.count() == 0:
        app.groupHelper.add(Group(name="Test_count", header="Test_header", footer="Test_footer"))
    app.groupHelper.edit_first_group()