import frappe


def connect_contact(self, action):
    if self.get("person_name"):
        lead = frappe.db.get_value(
            "Dynamic Link", {"link_doctype": "Lead", "link_name": self.get("name")}, "parent")
        if lead:
            contact = frappe.get_doc("Contact", lead)
        else:
            contact = frappe.new_doc("Contact")
        contact.update({
            'first_name': self.get("person_name"),
            'phone_nos': [{"phone": self.get("contact_details")}],
            'email_ids': [{"email_id": self.get("email")}],
            'designation': self.get("designation1"),
            'gender': self.get("gender1"),
        })
        contact.append(
            "links", {"link_doctype": "Lead", "link_name": self.name})

        contact.save(ignore_permissions=True)
