from __future__ import unicode_literals

import frappe
import unittest
from frappe.utils import random_string
from frappe.model.workflow import apply_workflow, WorkflowTransitionError, WorkflowPermissionError, get_common_transition_actions
from frappe.test_runner import make_test_records
from frappe.workflow.doctype.workflow.workflow import Workflow


def create_workflow():
	if frappe.db.exists('Workflow', 'Job Applicant'):
		frappe.delete_doc('Workflow', 'Job Applicant')

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
		state = 'Draft', allow_edit = 'All'
	))
	workflow.append('states', dict(
		state = 'Applied', allow_edit = 'Receptionist',
	))
	workflow.append('states', dict(
		state = 'Application Accepted', allow_edit = 'Receptionist'
	))
	workflow.append('states', dict(
		state = 'Application Rejected', allow_edit = 'Receptionist',
	))
	workflow.append('states', dict(
		state = 'Call for Interview', allow_edit = 'Receptionist'
	))
	workflow.append('states', dict(
		state = 'Invitation Accepted', allow_edit = 'Receptionist'
	))
	workflow.append('states', dict(
		state = 'Invitation Rejected', allow_edit = 'Receptionist'
	))
	workflow.append('states', dict(
		state = 'Initial Round', allow_edit = 'Receptionist',
	))
	workflow.append('states', dict(
		state = 'Technical Round', allow_edit = 'Receptionist'
	))
	workflow.append('states', dict(
		state = 'HR Round', allow_edit = 'Receptionist',
	))
	workflow.append('states', dict(
		state = 'Document Verification', allow_edit = 'Receptionist'
	))
	workflow.append('states', dict(
		state = 'Call Letter', allow_edit = 'Receptionist'
	))
	workflow.append('states', dict(
		state = 'On Board', allow_edit = 'Receptionist'
	))
	workflow.append('states', dict(
		state = 'Rejected', allow_edit = 'Receptionist'
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