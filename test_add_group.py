# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import Group
import unittest


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_add_group(self):
        wd = self.wd
        self.Open_HomePage(wd)
        self.Login(wd, username="admin", password="secret")
        self.Group_Actions(wd, Group(name="Test", header="Test_header", footer="Test_footer") )
        self.Close_Auth(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.Open_HomePage(wd)
        self.Login(wd, username="admin", password="secret")
        self.Group_Actions(wd, Group(name="", header="", footer="") )
        self.Close_Auth(wd)

    def Group_Actions(self, wd, group):
        # Open group page
        wd.find_element_by_xpath("//input[@value='Login']").click()
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
        wd.find_element_by_link_text("Logout").click()

    def Login(self, wd, username, password):
        # Login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)

    def Open_HomePage(self, wd):
        # Open homepage
        wd.get("http://localhost/addressbook/index.php")

    def Close_Auth(self, wd, username="admin", password="secret"):
        # Clear auth
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True


if __name__ == "__main__":
    unittest.main()
