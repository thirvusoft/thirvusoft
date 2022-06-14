# Copyright (c) 2022, ThirvuSoft Private Limited and contributors
# For license information, please see license.txt

# import frappe

from ast import Return
from frappe.utils import data
from frappe import _


def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	columns = [
		{
			"label": _("Task"),
			"fieldtype": "Link",
			"fieldname": "task",
			"options": "Task",
			"width": 300
		},
		{
			"label": _("Subject"),
			"fieldtype": "Data",
			"fieldname": "subject",
			"width": 300
		},
		{
			"label": _("Task Type"),
			"fieldtype": "Link",
			"fieldname": "task_type",
			"options": "Task Type",
			"width": 150
		},
		{
			"label": _("Status"),
			"fieldtype": "Data",
			"fieldname": "status",
			"width": 150
		},
		{
			"label": _("Hours Taken"),
			"fieldtype": "Float",
			"fieldname": "hours_taken",
			"width": 150
		},
		{
			"label": _("Resource Count"),
			"fieldtype": "Data",
			"fieldname": "resource_count",
			"width": 150
		},
	]

	return columns

def get_data(filters):
	return [{
		'task' : 'TASK-2022-01245',
		'subject' : 'Forgot Password',
		'task_type' : 'Medium',
		'status' : 'Completed',
		'hours_taken' : 5,
		'resource_count' : 2
	}]