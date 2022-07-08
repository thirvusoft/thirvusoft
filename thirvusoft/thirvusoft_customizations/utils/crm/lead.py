from readline import insert_text
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

        ]
    }

    create_custom_fields(lead_customize_field)

