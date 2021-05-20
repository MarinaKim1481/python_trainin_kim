from model.group import Group

def test_add_group(app):
    app.groupHelper.add(Group(name="Test", header="Test_header", footer="Test_footer"))

def test_add_empty_group(app):
    app.groupHelper.add(Group(name="", header="", footer=""))