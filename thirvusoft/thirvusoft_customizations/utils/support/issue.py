from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter
def issue_customization():
    issue_custom_fields()
    issue_property_setter()

def issue_custom_fields():
    pass

def issue_property_setter():pass
    # make_property_setter("Issue", "service_level_section", "hidden", 1, "Section Break")
    # make_property_setter("Issue", "naming_series", "hidden", 1, "Select")
    # make_property_setter("Issue", "priority", "reqd", 1, "Link")