from __future__ import unicode_literals
import frappe
def after_install():
    create_custom_role()
    create_custom_meeting_issues()
    create_state()
    create_action()
    create_jobApplicant_workflow()
def create_custom_role():
    existing_doc = frappe.db.get_value('Role', {'role_name': 'Receptionist'}, 'name')
    if not existing_doc:
        new_doc = frappe.new_doc('Role')
        new_doc.role_name = 'Receptionist'
        new_doc.save()
def create_custom_meeting_issues():
    meetlist=["General","Scrum","Management","Wonder","Thirvu","Client","Session"]
    for row in meetlist:
        new_doc = frappe.new_doc('TS Meeting Type')
        new_doc.ts_meeting_type = row
        new_doc.save()
    issuetypelist=["Internal Server Error","Server Down","404 Page Not Found","Unable to Connect","Print Format","CI Not-Reachable"]
    for row in issuetypelist:
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
    list=["Draft","Initial Data Validation","Selected For Telephoneic Interview","In-Person Interview","Rejected","Telephonic Interview","Selected For In-Person Interview","Follow Up","Written Test","Selected For HR Round","HR Round","Selected For Technical Round","Technical Round","Final Round","Selected For Employee"]
    for row in list:
        if not frappe.db.exists('Workflow State', row):
            new_doc = frappe.new_doc('Workflow State')
            new_doc.workflow_state_name = row
            new_doc.save()
def create_action():
    list=["Initial Data Validation","Selected For Telephoneic Interview","Reject","Selected For In-Person Interview","Follow Up","Written Test","Selected For HR Round","Selected For Technical Round","selected For Final Round","Selected For Employee","shortlisted"]
    for row in list:
        if not frappe.db.exists('Workflow Action Master', row):
            new_doc = frappe.new_doc('Workflow Action Master')
            new_doc.workflow_action_name = row
            new_doc.save()