from model.group import Group

def test_delete_first_group(app):
    if app.groupHelper.count() == 0:
        app.groupHelper.add(Group(name="Test_count", header="Test_header", footer="Test_footer"))
    app.groupHelper.delete_first_group()