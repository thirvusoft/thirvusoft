import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def lead_customize_field():
     lead_customize_field = {
        "Lead": [
            dict(fieldname="section_break1",
                 label="Requirements",
                 fieldtype="Section Break",
                 collapsible=1,
                 insert_after='notes'
                 ),
            dict(fieldname="text_editor1",
                 label="Requirements",
                 fieldtype="Text Editor",
                 insert_after='section_break1'
                 ),
            dict(fieldname="your_requirement",
                 label="Your Requirement",
                 fieldtype="Select",
                 options="ERP\nMobile Application\nWebsites\nE-commerece websites",
                 insert_after="total_data_entry_staff"
                 ),
            dict(fieldname="call_log",
                 label="Call Log",
                 fieldtype="Table",
                 options="Ts Call Log",
                 insert_after="your_requirement",
                 ),
            dict(fieldname="section_break2",
                 label="Decison Maker Details",
                 fieldtype="Section Break",
                 collapsible=1,
                 insert_after="ends_on"
                 ),
            dict(fieldname="person_name",
                 label="Person Name",
                 fieldtype="Data",
                 insert_after="section_break2"
                 ),
            dict(fieldname="contact_details",
                 label="Whatsapp Number",
                 fieldtype="Data",
                 insert_after="person_name"
                 ),
            dict(fieldname="email",
                 label="Email",
                 fieldtype="Data",
                 insert_after="contact_details"
                 ),
            dict(fieldname="designation1",
                 label="Designation",
                 fieldtype="Data",
                 insert_after="email"
                 ),
            dict(fieldname="gender1",
                 label="Gender",
                 fieldtype="Link",
                 options="Gender",
                 insert_after="designation1"
                 ),
            dict(fieldname="gender1",
                 label="Gender",
                 fieldtype="Link",
                 options="Gender",
                 insert_after="designation1"
                 ),
            dict(fieldname="call_connected",
                 label="Lead call attended",
                 fieldtype="Check",
                 insert_after="organization_lead",
                 description="Enable this after first lead call. ",
                 in_list_view = 1,
                 in_standard_filter = 1
                 ),
            dict(fieldname="column_break_a",
                 fieldtype="Column Break",
                 insert_after="call_connected",
                 ),
            dict(fieldname="delete_notif_log",
                 label="Delete Notification",
                 fieldtype="Button",
                 insert_after="column_break_a",
                 description="Click to delete system notification of this document.",                 
                 ),

        ]
    }
     create_custom_fields(lead_customize_field)

