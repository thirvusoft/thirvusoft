from __future__ import unicode_literals
import frappe

def after_install():
	create_custom_role()
	create_custom_meeting()


def create_custom_role():
	existing_doc = frappe.db.get_value('Role', {'role_name': 'Receptionist'}, 'name')
	if not existing_doc:
		new_doc = frappe.new_doc('Role')
		new_doc.role_name = 'Receptionist'
		new_doc.save()


def create_custom_meeting():
    meetlist=["General","Scrum","Management","Wonder","Thirvu","Client","Session"]
    for row in meetlist:
        new_doc = frappe.new_doc('TS Meeting Type')
        new_doc.ts_meeting_type = row
        new_doc.save()