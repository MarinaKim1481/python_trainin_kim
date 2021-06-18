import re
from random import randrange

def test_phones_on_home_page(app):
    index = random(app)
    contact_from_home_page = app.contactHelper.get_contact_list()[index]
    contact_from_edit_page = app.contactHelper.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_tels_from_home_page == merge_tels_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    index = random(app)
    contact_from_view_page = app.contactHelper.get_contact_from_view_page(index)
    contact_from_edit_page = app.contactHelper.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def test_emails_on_home_page(app):
    index = random(app)
    contact_from_home_page = app.contactHelper.get_contact_list()[index]
    contact_from_edit_page = app.contactHelper.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def test_adress_on_homepage(app):
    index = random(app)
    contact_from_home_page = app.contactHelper.get_contact_list()[index]
    contact_from_edit_page = app.contactHelper.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.address == contact_from_edit_page.address

def clear(s):
    return re.sub("[() -]", "", s)

def merge_tels_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x), filter(lambda x: x is not None,
                                                    [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x), filter(lambda x: x is not None,
                                                    [contact.email, contact.email2, contact.email3]))))

def random(app):
    contacts = app.contactHelper.get_contact_list()
    index = randrange(len(contacts))
    return index