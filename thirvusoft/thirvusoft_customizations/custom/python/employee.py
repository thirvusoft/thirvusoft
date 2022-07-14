from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
import frappe


def employee_customization():
    custom_fields = {
        "Employee": [
            dict(fieldname='compen_approver',
                label='compensation Opprover',
                fieldtype='Link',
                options='User',
                insert_after='shift_request_approver',
            ),            
        ],
     
    }
    create_custom_fields(custom_fields)

