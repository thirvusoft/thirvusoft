from erpnext.hr.doctype.leave_application.leave_application import LeaveApplication
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
import frappe


def compensation_customization():
    custom_fields = {
        "TS Compensation Request": [
            dict(fieldname='ts_section_break_4',
                fieldtype='Section Break',
                insert_after='leave_date',
            ),            
            dict(fieldname='compen_approver',
                label='compensation Opprover',
                fieldtype='Link',
                options='User',
                insert_after='ts_section_break_4',
            ),  
            dict(fieldname='ts_compen_approver_name',
                label='compensation Opprover Name',
                fieldtype='Data',
                insert_after='compen_approver',
            ),  
             dict(fieldname='ts_column_break',
                fieldtype='Column Break',
                insert_after='ts_compen_approver_name',
            ),
             dict(fieldname='ts_status',
                label='Status',
                fieldtype='Select',
                options='\nOpen\nApproved by Tech Lead\nRejected by Tech Lead\nApproved by HR Manager\nRejected by HR Manager',
                insert_after='ts_column_break',
            ),  
                        
        ],
     
    }
    create_custom_fields(custom_fields)

@frappe.whitelist()
def cm_approver(em_name):
    name= frappe.get_all("Employee",filters={'name':em_name}, fields=['compen_approver'],pluck='compen_approver')
    return name
    
@frappe.whitelist()
def cm_name(approver_name):
    name= frappe.get_all("User",filters={'email':approver_name}, fields=['full_name'],pluck='full_name')
    return name
    
    

