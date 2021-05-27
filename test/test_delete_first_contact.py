from model.contact import Contact

def test_delete_first_contact(app):
    if app.contactHelper.count() == 0:
        app.contactHelper.add(Contact(firstname="firstname_count", middlename="middlename", lastname="lastname", nickname="nickname",
                    photo_title="photo_title", company="company", address="address", home_phone="home_phone",
                    mobile_phone="mobile_phone", work_phone="work_phone", fax="fax", email="email", email2="email2",
                    email3="email3", homepage="homepage", bday="bday", bmonth="bmonth", byears="1990", aday="aday",
                    amonth="amonth", ayear="2010", address2="address2", phone2="phone2", notes="notes"))
    app.contactHelper.delete_first_contact()