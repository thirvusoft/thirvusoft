from __future__ import unicode_literals
import frappe
import unittest
from frappe.utils import random_string
from frappe.model.workflow import apply_workflow, WorkflowTransitionError, WorkflowPermissionError, get_common_transition_actions
from frappe.test_runner import make_test_records
from frappe.workflow.doctype.workflow.workflow import Workflow


def after_install():
	create_custom_role()
	create_custom_meeting()
	create_state()
	create_action()
	create_jobApplicant_workflow()
	create_project_tracking_workflow()
	create_task_workflow()
	create_leave_application_workflow()


def create_custom_role():
	existing_doc = frappe.db.get_value('Role', {'role_name': 'Receptionist'}, 'name')
	if not existing_doc:
		new_doc = frappe.new_doc('Role')
		new_doc.role_name = 'Receptionist'
		new_doc.save()



def create_custom_meeting():
    meetlist=["General","Scrum","Management","Wonder","Thirvu","Client","Session"]
    for row in meetlist:
        new_doc = frappe.new_doc('TS Meeting Type')
        new_doc.ts_meeting_type = row
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
		state = 'Applied', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Applied'
	))
	workflow.append('states', dict(
		state = 'Application Accepted', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Application Accepted'
	))
	workflow.append('states', dict(
		state = 'Application Rejected', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Application Rejected'
	))
	workflow.append('states', dict(
		state = 'Call for Interview', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Call for Interview'
	))
	workflow.append('states', dict(
		state = 'Invitation Accepted', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Invitation Accepted'
	))
	workflow.append('states', dict(
		state = 'Invitation Rejected', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Invitation Rejected'
	))
	workflow.append('states', dict(
		state = 'Initial Round', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Initial Round'
	))
	workflow.append('states', dict(
		state = 'Technical Round', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Technical Round'
	))
	workflow.append('states', dict(
		state = 'HR Round', allow_edit = 'Receptionist',update_field = 'status', update_value = 'HR Round'
	))
	workflow.append('states', dict(
		state = 'Document Verification', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Document Verification'
	))
	workflow.append('states', dict(
		state = 'Call Letter', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Call Letter'
	))
	workflow.append('states', dict(
		state = 'On Board', allow_edit = 'Receptionist',update_field = 'status', update_value = 'On Board'
	))
	workflow.append('states', dict(
		state = 'Rejected', allow_edit = 'Receptionist',update_field = 'status', update_value = 'Rejected'
	))
	workflow.append('transitions', dict(
		state = 'Draft', action='Applied', next_state = 'Applied',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.append('transitions', dict(
		state = 'Applied', action='Application Accepted', next_state = 'Application Accepted',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.append('transitions', dict(
		state = 'Applied', action='Reject', next_state = 'Draft',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.append('transitions', dict(
		state = 'Application Accepted', action='Call for Interview', next_state = 'Call for Interview',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.append('transitions', dict(
		state = 'Application Accepted', action='Reject', next_state = 'Draft',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.append('transitions', dict(
		state = 'Call for Interview', action='Invitation Accepted', next_state = 'Invitation Accepted',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.append('transitions', dict(
		state = 'Call for Interview', action='Reject', next_state = 'Invitation Rejected',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.append('transitions', dict(
		state = 'Invitation Accepted', action='Initial Round', next_state = 'Initial Round',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.append('transitions', dict(
		state = 'Invitation Accepted', action='Reject', next_state = 'Draft',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.append('transitions', dict(
		state = 'Initial Round', action='Technical Round', next_state = 'Technical Round',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.append('transitions', dict(
		state = 'Initial Round', action='Reject', next_state = 'Draft',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.append('transitions', dict(
		state = 'Technical Round', action='HR Round', next_state = 'HR Round',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.append('transitions', dict(
		state = 'Technical Round', action='Reject', next_state = 'Draft',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.append('transitions', dict(
		state = 'HR Round', action='Document Verification', next_state = 'Document Verification',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.append('transitions', dict(
		state = 'HR Round', action='Reject', next_state = 'Draft',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.append('transitions', dict(
		state = 'Document Verification', action='Call Letter', next_state = 'Call Letter',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.append('transitions', dict(
		state = 'Document Verification', action='Reject', next_state = 'Draft',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.append('transitions', dict(
		state = 'Call Letter', action='On Board', next_state = 'On Board',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.append('transitions', dict(
		state = 'Call Letter', action='Reject', next_state = 'Draft',
		allowed='Receptionist', allow_self_approval= 1
	))
	workflow.insert(ignore_permissions=True)

	return workflow


def create_state():
    list=["Pending Customer Requisition Form","Visit Scheduled","Lead Report Ready","Understanding Document In progress","Understanding Document Ready","Quotation","Paperwork Pending","Project Initiated","Development In Progress","Awaiting Implementation","Implementation in Progress","Support","Closed","On Hold","Cancelled","save","kavin","finest","Draft","Applied","Application Accepted","Application Rejected","Call for Interview","Invitation Accepted","Invitation Rejected","Initial Round","Technical Round","HR Round","Document Verification","Call Letter","On Board","Rejected","open","Scrum master verified","Completed","Approved by Tech Lead","Approved","Rejected","Cancelled"]
    for row in list:
        if not frappe.db.exists('Workflow State', row):
            new_doc = frappe.new_doc('Workflow State')
            new_doc.workflow_state_name = row
            new_doc.save()
def create_action():
    list=["on Hold","closed","Approve lead report","Reject visit scheduled","Approve understanding doc in process","Approve understanding doc ready","Reject understanding document","Approve quotation","paperwork pending","Reject Quotation","Project Initiated Approved","Development in process","Awaiting Implementation","Implementation in Process","Approved by Support","save and cancel","Reject lead report","Finest","cancel","Applied","Application Accepted","Reject","Call for Interview","Invitation Accepted","Initial Round","Technical Round","HR Round","Document Verification","Call Letter","On Board", "Task Approvel","Review","Reject","Approve"]
    for row in list:
        if not frappe.db.exists('Workflow Action Master', row):
            new_doc = frappe.new_doc('Workflow Action Master')
            new_doc.workflow_action_name = row
            new_doc.save()
 

def create_project_tracking_workflow():
    if frappe.db.exists('Workflow', 'workflow Project Tracking'):
        frappe.delete_doc('Workflow', 'workflow Project Tracking')
    if not frappe.db.exists('Role', 'COO'):
        frappe.get_doc(dict(doctype='Role',
            role_name='COO')).insert(ignore_if_duplicate=True)
    workflow = frappe.new_doc('Workflow')
    workflow.workflow_name = 'workflow Project Tracking'
    workflow.document_type = 'TS Project Tracking'
    workflow.workflow_state_field = 'workflow_state'
    workflow.is_active = 1
    workflow.send_email_alert = 0
    workflow.append('states', dict(
        state = 'Pending Customer Requisition Form', allow_edit = 'COO',
        update_field = 'status', update_value = 'Pending Customer Requisition Form'
    ))
    workflow.append('states', dict(
        state = 'Visit Scheduled', allow_edit = 'Projects Manager',
        update_field = 'status', update_value = 'Visit Scheduled'
    ))
    workflow.append('states', dict(
        state = 'Lead Report Ready', allow_edit = 'Projects User',
        update_field = 'status', update_value = 'Lead Report Ready'
    ))
    workflow.append('states', dict(
        state = 'Understanding Document In progress', allow_edit = 'Projects User',
        update_field = 'status', update_value = 'Understanding Document In progress'
    ))
    workflow.append('states', dict(
        state = 'Understanding Document Ready', allow_edit = 'Projects User',
        update_field = 'status', update_value = 'Understanding Document Ready'
    ))
    workflow.append('states', dict(
        state = 'Quotation', allow_edit = 'COO',
        update_field = 'status', update_value = 'Quotation'
    ))
    workflow.append('states', dict(
        state = 'Paperwork Pending', allow_edit = 'COO',
        update_field = 'status', update_value = 'Paperwork Pending'
    ))
    workflow.append('states', dict(
        state = 'Project Initiated', allow_edit = 'COO',
        update_field = 'status', update_value = 'Project Initiated'
    ))
    workflow.append('states', dict(
        state = 'Development In Progress', allow_edit = 'Projects Manager',
        update_field = 'status', update_value = 'Development In Progress'
    ))
    workflow.append('states', dict(
        state = 'Awaiting Implementation', allow_edit = 'Projects User',
        update_field = 'status', update_value = 'Awaiting Implementation'
    ))
    workflow.append('states', dict(
        state = 'Implementation in Progress', allow_edit = 'Projects User',
        update_field = 'status', update_value = 'Implementation in Progress'
    ))
    workflow.append('states', dict(
        state = 'Support', allow_edit = 'COO',
        update_field = 'status', update_value = 'Support'
    ))
    workflow.append('states', dict(
        state = 'Closed',docstate=1, allow_edit = 'Projects Manager',
        update_field = 'status', update_value = 'Closed'
    ))
    workflow.append('states', dict(
        state = 'On Hold', allow_edit = 'Projects Manager',
        update_field = 'status', update_value = 'On Hold'
    ))
    workflow.append('states', dict(
        state = 'Cancelled',docstate=2, allow_edit = 'Projects Manager',
        update_field = 'status', update_value = 'Cancelled'
    ))
    workflow.append('states', dict(
        state = 'save',docstate=1, allow_edit = 'Projects Manager',
    ))
    workflow.append('states', dict(
        state = 'draft', allow_edit = 'Projects User',
    ))
    workflow.append('states', dict(
        state = 'finest',docstate=1, allow_edit = 'Projects user',
        update_field = 'status', update_value = 'finest'
    ))
    workflow.append('transitions', dict(
        state = 'draft', action='on Hold', next_state = 'On Hold',
        allowed='Projects Manager', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'draft', action='closed', next_state = 'Closed',
        allowed='Projects Manager', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Pending Customer Requisition Form', action='Approve', next_state = 'Visit Scheduled',
        allowed='Projects Manager', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Visit Scheduled', action='Approve lead report', next_state = 'Lead Report Ready',
        allowed='Projects User', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Visit Scheduled', action='Reject visit scheduled', next_state = 'draft',
        allowed='Projects User', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Lead Report Ready', action='Approve understanding doc in process', next_state = 'Understanding Document In progress',
        allowed='Projects User', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Lead Report Ready', action='Approve understanding doc ready', next_state = 'Understanding Document Ready',
        allowed='Projects User', allow_self_approval= 1
    ))

    workflow.append('transitions', dict(
        state = 'Lead Report Ready', action='Reject lead report', next_state = 'draft',
        allowed='Projects User', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Understanding Document In progress', action='Approve understanding doc ready', next_state = 'Understanding Document Ready',
        allowed='Projects User', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Understanding Document In progress', action='Reject understanding document', next_state = 'draft',
        allowed='Projects User', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Understanding Document Ready', action='Approve quotation', next_state = 'Quotation',
        allowed='COO', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Understanding Document Ready', action='Reject understanding document', next_state = 'draft',
        allowed='COO', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Quotation', action='paperwork pending', next_state = 'Paperwork Pending',
        allowed='COO', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Quotation', action='Reject Quotation', next_state = 'draft',
        allowed='COO', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Quotation', action='Project Initiated Approved', next_state = 'Project Initiated',
        allowed='COO', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Paperwork Pending', action='Project Initiated Approved', next_state = 'Project Initiated',
        allowed='COO', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Paperwork Pending', action='Reject', next_state = 'draft',
        allowed='COO', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Project Initiated', action='Development in process', next_state = 'Development In Progress',
        allowed='Projects Manager', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Project Initiated', action='Reject', next_state = 'draft',
        allowed='Projects Manager', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Development In Progress', action='Awaiting Implementation', next_state = 'Awaiting Implementation',
        allowed='Projects User', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Awaiting Implementation', action='Implementation in Process', next_state = 'Implementation in Progress',
        allowed='Projects User', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Implementation in Progress', action='Approved by Support', next_state = 'Support',
        allowed='Projects User', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Implementation in Progress', action='Reject', next_state = 'draft',
        allowed='Projects User', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Support', action='Finest', next_state = 'finest',
        allowed='COO', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'finest', action='closed', next_state = 'Closed',
        allowed='Projects Manager', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'On Hold', action='Approve', next_state = 'draft',
        allowed='Projects Manager', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'draft', action='save and cancel', next_state = 'save',
        allowed='Projects Manager', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'On Hold', action='save and cancel', next_state = 'save',
        allowed='Projects Manager', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'save', action='cancel', next_state = 'Cancelled',
        allowed='Projects Manager', allow_self_approval= 1
    ))
    workflow.insert(ignore_permissions=True)
    return workflow

def create_task_workflow():
    if frappe.db.exists('Workflow', 'Task workflow'):
        frappe.delete_doc('Workflow', 'Task workflow')
    if not frappe.db.exists('Role', 'Scrum Master'):
        frappe.get_doc(dict(doctype='Role',
            role_name='Scrum Master')).insert(ignore_if_duplicate=True)
    if not frappe.db.exists('Role', 'Tech Lead'):
        frappe.get_doc(dict(doctype='Role',role_name='Tech Lead')).insert(ignore_if_duplicate=True)
    workflow = frappe.new_doc('Workflow')
    workflow.workflow_name = 'Task workflow'
    workflow.document_type = 'Task'
    workflow.workflow_state_field = 'workflow_state'
    workflow.is_active = 1
    workflow.send_email_alert = 0
    workflow.append('states', dict(
        state = 'Open', allow_edit = 'Scrum Master',
        update_field = 'status', update_value = 'Open'
    ))
    workflow.append('states', dict(
        state = 'Scrum master verified', allow_edit = 'Tech Lead',
        update_field = 'status', update_value = 'Pending Review'
    ))
    workflow.append('states', dict(
        state = 'Completed', allow_edit = 'Tech Lead',
        update_field = 'status', update_value = 'Completed'
    ))
    workflow.append('transitions', dict(
        state = 'Open', action='Task Approvel', next_state = 'Scrum master verified',
        allowed='Scrum Master', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Open', action='Reject', next_state = 'Open',
        allowed='Scrum Master', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Scrum master verified', action='Task Approvel', next_state = 'Completed',
        allowed='Tech Lead', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Scrum master verified', action='Reject', next_state = 'Open',
        allowed='Tech Lead', allow_self_approval= 1
    ))
    workflow.insert(ignore_permissions=True)
    return workflow
def create_leave_application_workflow():
    if frappe.db.exists('Workflow', 'Leave Application workflow'):
        frappe.delete_doc('Workflow', 'Leave Application workflow')
    if not frappe.db.exists('Role', 'COO'):
        frappe.get_doc(dict(doctype='Role',
            role_name='COO')).insert(ignore_if_duplicate=True)
    if not frappe.db.exists('Role', 'Tech Lead'):
        frappe.get_doc(dict(doctype='Role',role_name='Tech Lead')).insert(ignore_if_duplicate=True)
    workflow = frappe.new_doc('Workflow')
    workflow.workflow_name = 'Leave Application workflow'
    workflow.document_type = 'Leave Application'
    workflow.workflow_state_field = 'workflow_state'
    workflow.is_active = 1
    workflow.send_email_alert = 0
    workflow.append('states', dict(
        state = 'Open', allow_edit = 'Scrum Master',
        update_field = 'status', update_value = 'Open'
    ))
    workflow.append('states', dict(
        state = 'Approved by Tech Lead',doc_status=0, allow_edit = 'Tech Lead',
        update_field = 'status', update_value = 'Partially Approved'
    ))
    workflow.append('states', dict(
        state = 'Approved',doc_status=1, allow_edit = 'Tech Lead',
        update_field = 'status', update_value = 'Approved'
    ))
    workflow.append('states', dict(
        state = 'Rejected',doc_status=0, allow_edit = 'Tech Lead',
        update_field = 'status', update_value = 'Cancelled'
    ))
    workflow.append('states', dict(
        state = 'Cancelled',doc_status=2, allow_edit = 'Tech Lead',
        update_field = 'status', update_value = 'Cancelled'
    ))
    workflow.append('transitions', dict(
        state = 'Open', action='Review', next_state = 'Approved by Tech Lead',
        allowed='Tech Lead', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Open', action='Reject', next_state = 'Rejected',
        allowed='Tech Lead', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Approved by Tech Lead', action='Approve', next_state = 'Approved',
        allowed='COO', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Approved by Tech Lead', action='Reject', next_state = 'Rejected',
        allowed='COO', allow_self_approval= 1
    ))
    workflow.append('transitions', dict(
        state = 'Approved', action='Reject', next_state = 'Cancelled',
        allowed='COO', allow_self_approval= 1
    ))
    workflow.insert(ignore_permissions=True)
    return workflow
