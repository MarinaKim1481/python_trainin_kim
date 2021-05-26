class GroupHelper:

    def __init__(self, app):
        self.app = app

    def add(self, group):
        # Open group page
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        # Creation new
        wd.find_element_by_name("new").click()
        self.fill_group_from(group)
        wd.find_element_by_name("submit").click()
        # Open group page
        wd.find_element_by_link_text("group page").click()

    def fill_group_from(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        wd.find_element_by_link_text("group page").click()

    def edit_first_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_first_group()
        # Open modification form
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("New")
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("group page").click()

    def edit_first_group_name(self, new_group_data):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_first_group()
        # Open modification form
        wd.find_element_by_name("edit").click()
        self.fill_group_from(new_group_data)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("group page").click()

    def edit_first_group_header(self, new_group_data):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_first_group()
        # Open modification form
        wd.find_element_by_name("edit").click()
        self.fill_group_from(new_group_data)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("group page").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        return len(wd.find_elements_by_name("selected[]"))
