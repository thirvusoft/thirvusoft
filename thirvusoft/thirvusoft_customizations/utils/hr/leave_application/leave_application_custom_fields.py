import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
def leave_application_customization():
    leave_application_custom_fields()
    leave_application_property_setter()
def leave_application_custom_fields():
    custom_fields = {
        "Leave Application": [
            dict(
                fieldname="reason_for_rejected",
                fieldtype="Small Text",
                label="Reason For Rejected",
                insert_after="description",
                depends_on="eval: in_list(['Rejected by Tech Lead','Rejected by HR Manager'], doc.status)",
                mandatory_depends_on="eval: in_list(['Rejected by Tech Lead','Rejected by HR Manager'], doc.status)"
            ),
            dict(
                fieldname="tech_lead_approved",
                fieldtype="Check",
                label="Tech Lead Approved",
                insert_after="reason_for_rejected",
                hidden=1
                
            ),
            dict(
                fieldname="hr_manager_approved",
                fieldtype="Check",
                label="HR Manager Approved",
                insert_after="tech_lead_approved",
                hidden=1
                
            ),
            dict(
                fieldname="user_designation",
                fieldtype="Data",
                label="User Designation",
                insert_after="tech_lead_approved",
                hidden=1
                
            ),

        ]
    }
    create_custom_fields(custom_fields)
def leave_application_property_setter():
    leave_applicaion=frappe.get_doc({
        'doctype':'Property Setter',  
        'doctype_or_field': "DocField", 
        'doc_type': "Leave Application", 
        'property':"options", 
        "property_type":"Select", 
        'field_name':"status", 
        "value":"Open\nApproved by Tech Lead\nRejected by Tech Lead\nApproved by HR Manager\nRejected by HR Manager"     
    })       
    leave_applicaion.insert() 
    leave_applicaion.save(ignore_permissions=True)

    leave_applicaion=frappe.get_doc({
        'doctype':'Property Setter',  
        'doctype_or_field': "DocField", 
        'doc_type': "Leave Application", 
        'property':"hidden", 
        "property_type":"Check", 
        'field_name':"follow_via_email", 
        "value":"1"
    })       
    leave_applicaion.insert() 
    leave_applicaion.save(ignore_permissions=True)
    leave_applicaion=frappe.get_doc({
        'doctype':'Property Setter',  
        'doctype_or_field': "DocField", 
        'doc_type': "Leave Application", 
        'property':"default", 
        "property_type":"Check", 
        'field_name':"follow_via_email", 
        "value":"0"
    })       
    leave_applicaion.insert() 
    leave_applicaion.save(ignore_permissions=True) 
                    
