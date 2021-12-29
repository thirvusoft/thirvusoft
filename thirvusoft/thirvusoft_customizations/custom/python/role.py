from __future__ import unicode_literals
import frappe

def create_custom_role():
	existing_doc = frappe.db.get_value('Role', {'role_name': 'Receptionist'}, 'name')
	if not existing_doc:
		new_doc = frappe.new_doc('Role')
		new_doc.role_name = 'Receptionist'
		new_doc.save()