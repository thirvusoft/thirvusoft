import frappe


def connect_contact(self, action):
    contact = frappe.get_doc({
        'doctype': 'Contact',
        'first_name': self.person_name,
        'phone_nos': [{"phone": self.contact_details}],
        '': "Issue",
        'property': "hidden",
        'field_name': "subject",
        "value": 1
    })
    contact.insert()
    contact.save()
