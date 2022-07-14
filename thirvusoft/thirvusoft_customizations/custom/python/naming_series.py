import frappe


def employee_naming_series():
    print("Creating Naming series for employee")
    naming_series = frappe.get_doc({

        'doctype': 'Property Setter',
        'doctype_or_field': "DocField",
        'doc_type': "Employee",
        'property': "options",
        'property_type': "Data",
        'field_name': "naming_series",
        "value": "HR-EMP-.YY.-\nHR-INT-.YY.-"
    })
    naming_series.save()
