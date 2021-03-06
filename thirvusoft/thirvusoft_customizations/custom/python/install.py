from __future__ import unicode_literals
from thirvusoft.thirvusoft_customizations.utils.hr.leave_application.leave_application_custom_fields import leave_application_customization
from thirvusoft.thirvusoft_customizations.utils.hr.leave_application.attendance_custom_fields import attendance_custom_fields
import frappe
def after_install():
    create_custom_role()
    create_custom_meeting_issues()
    create_issue_type()
    create_state()
    create_action()
    create_jobApplicant_workflow()
    create_leave_application_workflow()
    create_compensation_request_workflow()
    leave_application_customization()
    attendance_custom_fields()
   

def create_custom_role():
    existing_doc = frappe.db.get_value('Role', {'role_name': 'Receptionist'}, 'name')
    if not existing_doc:
        new_doc = frappe.new_doc('Role')
        new_doc.role_name = 'Receptionist'
        new_doc.save()
    existing_doc = frappe.db.get_value('Role', {'role_name': 'Product Manager'}, 'name')
    if not existing_doc:
        new_doc = frappe.new_doc('Role')
        new_doc.role_name = 'Product Manager'
        new_doc.save()
def create_custom_meeting_issues():
    meetlist=["General","Scrum","Management","Wonder","Thirvu","Client","Session"]
    for row in meetlist:
        if not frappe.db.exists('TS Meeting Type', row):
            new_doc = frappe.new_doc('TS Meeting Type')
            new_doc.ts_meeting_type = row
            new_doc.save()
def create_issue_type():
    issue_type_list=["Internal Server Error","Server Down","404 Page Not Found","Unable to Connect","Print Format","CI Not-Reachable"]
    for row in issue_type_list:
        if not frappe.db.exists('Issue Type', row):
            new_doc = frappe.new_doc('Issue Type')
            new_doc.__newname = row
            new_doc.save()
def create_jobApplicant_workflow():
    if frappe.db.exists('Workflow', 'Job Applicant workflow'):
        frappe.delete_doc('Workflow', 'Job Applicant workflow')
    if not frappe.db.exists('Role', 'Receptionist'):
        frappe.get_doc(dict(doctype='Role',
            role_name='Receptionist')).insert(ignore_if_duplicate=True)
    workflow = frappe.new_doc('Workflow')
    workflow.workflow_name = 'Job Applicant workflow'
    workflow.document_type = 'Job Applicant'
    workflow.workflow_state_field = 'workflow_state'
    workflow.is_active = 1
    workflow.send_email_alert = 1
    workflow.append('states', dict(
        state = 'Draft', allow_edit = 'Receptionist',update_field = 'status', update_value = 'open'
    ))
    workflow.append('states', dict(
        state = 'Initial Data Validation', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Initial Data Validation'
    ))
    workflow.append('states', dict(
        state = 'Selected For Telephoneic Interview', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Selected For Telephoneic Interview'
    ))
    workflow.append('states', dict(
        state = 'Rejected', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Rejected'
    ))
    workflow.append('states', dict(
        state = 'Telephonic Interview', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Telephonic Interview'
    ))
    workflow.append('states', dict(
        state = 'Selected For In-Person Interview', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Selected For In-Person Interview'
    ))
    workflow.append('states', dict(
        state = 'In-Person Interview', allow_edit = 'Receptionist',update_field = 'status', update_value = 'In-Person Interview'
    ))
    workflow.append('states', dict(
        state = 'Follow Up', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Follow Up'
    ))
    workflow.append('states', dict(
        state = 'Written Test', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Written Test'
    ))
    workflow.append('states', dict(
        state = 'Selected For HR Round', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Selected For HR Round'
    ))
    workflow.append('states', dict(
        state = 'HR Round', allow_edit = 'Receptionist',update_field = 'status', update_value = 'HR Round'
    ))
    workflow.append('states', dict(
        state = 'Selected For Technical Round', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Selected For technical Round'
    ))
    workflow.append('states', dict(
        state = 'Technical Round', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Technical Round'
    ))
    workflow.append('states', dict(
        state = 'Final Round', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Final Round'
    ))
    workflow.append('states', dict(
        state = 'Selected For Employee', allow_edit = 'Receptionist',update_field = 'status', update_value = 'shortlisted'
    ))
    workflow.append('transitions', dict(
        state = 'Draft', action='Initial Data Validation', next_state = 'Initial Data Validation',
        allowed='Receptionist', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Initial Data Validation', action='Selected For Telephoneic Interview', next_state = 'Telephonic Interview',
        allowed='Receptionist', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Initial Data Validation', action='Reject', next_state = 'Rejected',
        allowed='Receptionist', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Telephonic Interview', action='Selected For In-Person Interview', next_state = 'In-Person Interview',
        allowed='Receptionist', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'In-Person Interview', action='Follow Up', next_state = 'Follow Up',
        allowed='Receptionist', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Telephonic Interview', action='Reject', next_state = 'Rejected',
        allowed='Receptionist', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Follow Up', action='Selected For In-Person Interview', next_state = 'In-Person Interview',
        allowed='Receptionist', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Follow Up', action='Reject', next_state = 'Rejected',
        allowed='Receptionist', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'In-Person Interview', action='Written Test', next_state = 'Written Test',
        allowed='Receptionist', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'In-Person Interview', action='Reject', next_state = 'Rejected',
        allowed='Receptionist', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Written Test', action='Selected For HR Round', next_state = 'HR Round',
        allowed='Receptionist', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Written Test', action='Reject', next_state = 'Rejected',
        allowed='Receptionist', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'HR Round', action='Selected For Technical Round', next_state = 'Technical Round',
        allowed='Receptionist', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'HR Round', action='Reject', next_state = 'Rejected',
        allowed='Receptionist', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Technical Round', action='selected For Final Round', next_state = 'Final Round',
        allowed='Receptionist', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Technical Round', action='Reject', next_state = 'Rejected',
        allowed='Receptionist', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Final Round', action='shortlisted', next_state = 'Selected For Employee',
        allowed='Receptionist', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Final Round', action='Reject', next_state = 'Rejected',
        allowed='Receptionist', allow_self_approval= 1
    ))
    workflow.insert(ignore_permissions=True)
    return workflow
def create_state():
    list=["Open","Approved by Tech Lead","Rejected by Tech Lead","Approved by HR Manager","Rejected by HR Manager","Approved","Draft","Initial Data Validation","Selected For Telephoneic Interview","In-Person Interview","Rejected","Telephonic Interview","Selected For In-Person Interview","Follow Up","Written Test","Selected For HR Round","HR Round","Selected For Technical Round","Technical Round","Final Round","Selected For Employee"]
    for row in list:
        if not frappe.db.exists('Workflow State', row):
            new_doc = frappe.new_doc('Workflow State')
            new_doc.workflow_state_name = row
            if(row=="Open"):
                new_doc.style="Primary"
            if(row=="Approved by Tech Lead"):
                new_doc.style="Warning"
            if(row=="Rejected by Tech Lead"):
                new_doc.style="Danger"
            if(row=="Rejected by HR Manager"):
                new_doc.style="Danger"
            if(row=="Approved by HR Manager"):
                new_doc.style="Success"
            new_doc.save()
def create_action():
    list=["Initial Data Validation","Approve","Reject","Selected For Telephoneic Interview","Reject","Selected For In-Person Interview","Follow Up","Written Test","Selected For HR Round","Selected For Technical Round","selected For Final Round","Selected For Employee","shortlisted"]
    for row in list:
        if not frappe.db.exists('Workflow Action Master', row):
            new_doc = frappe.new_doc('Workflow Action Master')
            new_doc.workflow_action_name = row
            new_doc.save()
def create_leave_application_workflow():
    if frappe.db.exists('Workflow', 'Leave Application Flow'):
        frappe.delete_doc('Workflow', 'Leave Application Flow')
    workflow = frappe.new_doc('Workflow')
    workflow.workflow_name = 'Leave Application Flow'
    workflow.document_type = 'Leave Application'
    workflow.workflow_state_field = 'workflow_state'
    workflow.is_active = 0
    workflow.send_email_alert = 1
    workflow.append('states', dict(
        state = 'Open', allow_edit = 'All',
    ))
    workflow.append('states', dict(
        state = 'Approved by Tech Lead', allow_edit = 'Tech Lead'
    ))
    workflow.append('states', dict(
        state = 'Rejected by Tech Lead', allow_edit = 'Tech Lead'
    ))
    workflow.append('states', dict(
        state = 'Approved by HR Manager', allow_edit = 'HR Manager', 	doc_status = 1
    ))
    workflow.append('states', dict(
        state = 'Rejected by HR Manager', allow_edit = 'HR Manager'
    ))
    
    workflow.append('transitions', dict(
        state = 'Open', action='Approve', next_state = 'Approved by Tech Lead',
        allowed='Tech Lead', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Open', action='Reject', next_state = 'Rejected by Tech Lead',
        allowed='Tech Lead', allow_self_approval= 1,
    ))
    workflow.append('transitions', dict(
        state = 'Approved by Tech Lead', action='Approve', next_state = 'Approved by HR Manager',
        allowed='HR Manager', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Approved by Tech Lead', action='Reject', next_state = 'Rejected by HR Manager',
        allowed='HR Manager', allow_self_approval= 1,
    ))
   
    workflow.insert(ignore_permissions=True)
    return workflow

def create_compensation_request_workflow():
    if frappe.db.exists('Workflow', 'TS Compensation Request workflow'):
        frappe.delete_doc('Workflow', 'TS Compensation Request workflow')
    if not frappe.db.exists('Role', 'HR Manager'):
        frappe.get_doc(dict(doctype='Role',
            role_name='HR Manager')).insert(ignore_if_duplicate=True)
    workflow = frappe.new_doc('Workflow')
    workflow.workflow_name = 'TS Compensation Request workflow'
    workflow.document_type = 'TS Compensation Request'
    workflow.workflow_state_field = 'workflow_state'
    workflow.is_active = 1
    workflow.send_email_alert = 1
    workflow.append('states', dict(
    state = 'Draft', allow_edit = 'HR Manager', 
    ))
   
    workflow.append('states', dict(
    state = 'Approved', allow_edit = 'HR Manager'  ,doc_status = 1
    ))
    workflow.append('states', dict(
    state = 'Rejected', allow_edit = 'HR Manager'
    ))


    workflow.append('transitions', dict(
    state = 'Draft', action='Approve', next_state = 'Approved',
    allowed='HR Manager', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
    state = 'Draft', action='Reject', next_state = 'Rejected',
    allowed='HR Manager', allow_self_approval= 1
    ))


    workflow.insert(ignore_permissions=True)
    return workflow
