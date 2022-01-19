import frappe
from future import unicode_literals

def create_custom_meeting():
    meetlist=["General","Scrum","Management","Wonder","Thirvu","Client","Session"]
    for row in meetlist:
        new_doc = frappe.new_doc('TS Meeting Type')
        new_doc.ts_meeting_type = row
        new_doc.save()


