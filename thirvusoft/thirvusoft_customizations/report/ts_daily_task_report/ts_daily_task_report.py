# Copyright (c) 2022, ThirvuSoft Private Limited and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters={}):
	columns, data = get_columns(filters), get_data(filters)
	return columns, data
	
def get_data(filters):
	filters['exp_start_date']=['<=', frappe.utils.nowdate()]
	filters['msg_sent']=0
	tasks=frappe.get_all('Task', filters,pluck='name')
	data=[]
	for task in tasks:
		doc=frappe.get_doc('Task', task)
		data.append({
			'task_desc': doc.subject,
			'task_nature': doc.task_nature,
			'status': doc.status,
			'time': doc.expected_time,
			'amount': doc.expected_time * (doc.per_hour_charge or 0)
		})
	return data
	
def get_columns(filters):
	columns=[
		{
			'label': _('Task Description'),
			'fieldtype': 'Data',
			'fieldname': 'task_desc'
		},
		{
			'label': _('Task Nature'),
			'fieldtype': 'Data',
			'fieldname': 'task_nature'
		},
		{
			'label': _('Status'),
			'fieldtype': 'Data',
			'fieldname': 'status'
		},
		{
			'label': _('Expected Time'),
			'fieldtype': 'Data',
			'fieldname': 'time'
		},
		{
			'label': _('Amount'),
			'fieldtype': 'Currency',
			'fieldname': 'amount'
		}
	]
	return columns
