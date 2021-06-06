from model.contact import Contact

def test_edit_contact(app):
    if app.contactHelper.count() == 0:
        app.contactHelper.add(Contact(firstname="firstname_count", middlename="middlename", lastname="lastname", nickname="nickname",
                    photo_title="photo_title", company="company", address="address", home_phone="home_phone",
                    mobile_phone="mobile_phone", work_phone="work_phone", fax="fax", email="email", email2="email2",
                    email3="email3", homepage="homepage", bday="bday", bmonth="bmonth", byears="1990", aday="aday",
                    amonth="amonth", ayear="2010", address2="address2", phone2="phone2", notes="notes"))
    old_list = app.contactHelper.get_contact_list()
    contact = Contact(firstname="Second")
    contact.id = old_list[1].id
    app.contactHelper.edit_first_contact(сontact)
    new_list = app.contactHelper.get_contact_list()
    assert len(old_list) == len(new_list)
    old_list[1] = contact
    assert(sorted(old_list, key=Contact.id_or_max)) == (sorted(new_list, key=Contact.id_or_max))