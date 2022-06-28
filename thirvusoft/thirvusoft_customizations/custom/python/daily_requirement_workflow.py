import frappe
def workflow_document_creation():
    create_state()
    create_action()
    create_Workflow_doc()

def create_Workflow_doc():
    if frappe.db.exists('Workflow', 'TS Daily Requirement Timing'):
        frappe.delete_doc('Workflow', 'TS Daily Requirement Timing')
    workflow = frappe.new_doc('Workflow')
    workflow.workflow_name = 'TS Daily Requirement Timing'
    workflow.document_type = 'TS Daily Requirement Sheet'
    workflow.workflow_state_field = 'workflow_state'
    workflow.is_active = 1
    workflow.send_email_alert = 1

    workflow.append('states', dict(
        state = 'Draft',doc_status=0, allow_edit = 'Product Manager'
    ))
    workflow.append('states', dict(
        state = 'Submitted',doc_status=1, allow_edit = 'Tech Lead'
    ))
    workflow.append('states', dict(
        state = 'Submitted',doc_status=1, allow_edit = 'Product Manager'
    ))
    workflow.append('states', dict(
        state = 'Rejected',doc_status=1, allow_edit = 'Tech Lead'
    ))

    workflow.append('transitions', dict(
        state = 'Draft', action='Submit', next_state = 'Submitted',
        allowed='Product Manager', allow_self_approval= 1,condition="doc.timing==0"
    ))
    workflow.append('transitions', dict(
        state = 'Draft', action='Submit', next_state = 'Submitted',
        allowed='Tech Lead', allow_self_approval= 1,condition="doc.timing==1"
    ))
    workflow.append('transitions', dict(
        state = 'Draft', action='Reject', next_state = 'Rejected',
        allowed='Tech Lead', allow_self_approval= 1,condition="doc.timing==1"
    ))

    workflow.insert(ignore_permissions=True)
    return workflow
def create_state():
    list=["Draft","Submitted","Rejected"]
    for row in list:
        if not frappe.db.exists('Workflow State', row):
            new_doc = frappe.new_doc('Workflow State')
            new_doc.workflow_state_name = row
            if(row=="Draft"):
                new_doc.style="Warning"
            if(row=="Submitted"):
                new_doc.style="Success"
            if(row=="Rejected"):
                new_doc.style="Danger"
            new_doc.save()
def create_action():
    list=["Reject", "Submit", "Draft"]
    for row in list:
        if not frappe.db.exists('Workflow Action Master', row):
            new_doc = frappe.new_doc('Workflow Action Master')
            new_doc.workflow_action_name = row
            new_doc.save()