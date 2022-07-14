import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def employee_customization():
    emp_custom_fields()

def emp_custom_fields():
    custom_fields = {
        "Employee": [
            dict(
                fieldname="abbr",
                fieldtype="Data",
                label="Abbreviation",
                insert_after="naming_series",
                hidden=1
            )
        ]
        }
    create_custom_fields(custom_fields)
