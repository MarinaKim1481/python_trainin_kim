from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.contactHelper.count() == 0:
        app.contactHelper.add(Contact(firstname="firstname_count", middlename="middlename", lastname="lastname", nickname="nickname",
                    photo_title="photo_title", company="company", address="address", home_phone="home_phone",
                    mobile_phone="mobile_phone", work_phone="work_phone", fax="fax", email="email", email2="email2",
                    email3="email3", homepage="homepage", bday="bday", bmonth="bmonth", byears="1990", aday="aday",
                    amonth="amonth", ayear="2010", address2="address2", phone2="phone2", notes="notes"))
    old_list = app.contactHelper.get_contact_list()
    index = randrange(len(old_list))
    app.contactHelper.delete_contact_by_index(index)
    assert len(old_list) - 1 == app.contactHelper.count()
    new_list = app.contactHelper.get_contact_list()
    old_list[index:index+1] = []
    assert old_list == new_list