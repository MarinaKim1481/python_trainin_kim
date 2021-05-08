class groupHelper:

    def __init__(self, app):
        self.app = app

    def test_add_group(self, group):
        # Open group page
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        # Creation new
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        # Open group page
        wd.find_element_by_link_text("group page").click()