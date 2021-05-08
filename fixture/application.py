from selenium import webdriver
from fixture.sessionHelper import sessionHelper
from fixture.groupHelper import groupHelper
from fixture.contactHelper import contactHelper



class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.sessionHelper = sessionHelper(self)
        self.groupHelper = groupHelper(self)
        self.contactHelper = contactHelper(self)

    def open_homepage(self):
        # Open homepage
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()
