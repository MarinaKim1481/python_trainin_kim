from selenium import webdriver
from fixture.sessionHelper import SessionHelper
from fixture.groupHelper import GroupHelper
from fixture.contactHelper import ContactHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.sessionHelper = SessionHelper(self)
        self.groupHelper = GroupHelper(self)
        self.contactHelper = ContactHelper(self)

    def open_homepage(self):
        # Open homepage
        wd = self.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_link_text("all e-mail")) > 0):
            wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False