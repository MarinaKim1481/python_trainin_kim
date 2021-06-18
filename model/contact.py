from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, photo_title=None, company=None, address=None, home_phone=None, mobile_phone=None, work_phone=None, fax=None, email=None, email2=None, email3=None, all_emails_from_home_page=None, homepage=None, bday=None, bmonth=None, byears=None, aday=None, amonth=None, ayear=None, address2=None, phone2=None, notes=None, all_tels_from_home_page=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo_title = photo_title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byears = byears
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.all_tels_from_home_page = all_tels_from_home_page
        self.id = id

    def __repr__(self):
        return "%s, %s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize