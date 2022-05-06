import frappe
@frappe.whitelist()
def property_creator_task():
    ts_new_property_task=frappe.get_doc({
        'doctype':'Property Setter',
        'doctype_or_field': "DocField",
        'doc_type': "Task",
        'property':"options",
        "property_type":"Select",
        'field_name':"status",
        "value":"Hold\nOpen\nWorking\nPR Opened\nPR Merged\nPR Conflicts\nPR Closed\nDeployed to Production\nDevelopment Testing Started\nDevelopment Testing Ended\nCI Verified\nClient Satisfied\nOverdue\nCompleted\nCanceled"
    })
    ts_new_property_task.insert()
    ts_new_property_task.save()

def property_creator_issue():
    ts_new_property_issue=frappe.get_doc({
        'doctype':'Property Setter',
        'doctype_or_field': "DocField",
        'doc_type': "Issue",
        'property':"hidden",
        'field_name':"subject",
        "value":1
    })
    ts_new_property_issue.insert()
    ts_new_property_issue.save()