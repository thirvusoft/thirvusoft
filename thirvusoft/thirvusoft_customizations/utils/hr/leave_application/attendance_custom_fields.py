import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def attendance_custom_fields():
    custom_fields = {
        "Attendance": [
            dict(
                fieldname="compensation",
                fieldtype="Check",
                label="Is Compensation",
                insert_after="company",
                readonly=1,
               
            ),
           
            dict(fieldname='compensation_day', label='Compensation',
                 fieldtype='Link', options='TS Compensation Request', insert_after='compensation' ,readonly=1),
  
        ]
    }
    create_custom_fields(custom_fields)