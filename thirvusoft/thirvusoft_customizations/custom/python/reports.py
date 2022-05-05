from tracemalloc import take_snapshot
import frappe
import json

from frappe.utils.data import nowdate
@frappe.whitelist()
def task_status(name,value):
    task_doc= frappe.get_doc('Task',name)
    if (value == "Completed"):
        task_doc.update({
            'status':value,
            'completed_on':nowdate()
        })
        task_doc.save()
        frappe.db.commit()
    else:
        task_doc.update({
                'status':value
            })
        task_doc.save()
        frappe.db.commit()