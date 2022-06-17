# Copyright (c) 2022, ThirvuSoft Private Limited and contributors
# For license information, please see license.txt

import re
import frappe
import json
from frappe.utils.pdf import get_pdf
from frappe.www.printview import get_print_style
from frappe.utils import today
from frappe.desk.query_report import get_prepared_report_result, get_report_doc

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
			"fieldname": "name",
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
			"fieldname": "type",
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
			"fieldname": "actual_time",
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
	result = frappe.db.get_list("Task", filters={"project": filters["project"], 
	"act_start_date": ["between", (filters['from_date'], filters['to_date'])],
	},fields=["name","subject","type","status","actual_time","resource_count"])
	
	return result

def create_temp_file(doc):
	report_name_mapping = {'Agent Late Payment': 'Late', 'Agent Outstanding': 'Total'}
	report_name = report_name_mapping[doc.report_name]
	customer_group = json.loads(doc.filters)['customer_group']
	file_name = f'{customer_group}-{report_name}.pdf'
	# todo: don't use the same file if found... an one week old file got sent and created a lot of confusions...
	file_exist = frappe.db.get_value('File',{'file_name':file_name},'name')
	content = get_content(doc)
	if not file_exist and content:
		_file = frappe.get_doc({
			"doctype": "File",
			"file_name": file_name,
			"content": content})
		_file.save(ignore_permissions=True)
		file_exist = _file.name
	return file_exist

def get_content(doc):
	if doc.report_name == 'Agent Late Payment':
		orientation = 'Portrait'
		html =  get_thirvu_report_html(late_payment_filters=doc.filters, prepared_report_name=doc.name)

	return get_pdf(html, {"orientation": orientation})


@frappe.whitelist()
def get_thirvu_report_html(customer_group=None, late_payment_filters=None, prepared_report_name=''):

	user = frappe.session.user
	if not late_payment_filters:
		default_company = frappe.defaults.get_user_default("Company")
		late_payment_filters = {'company': default_company,
		'report_date': today(),
		'ageing_based_on': 'Posting Date',
		'range1': 30,
		'range2': 60,
		'range3': 90,
		'range4': 120,
		'customer_group': customer_group}
	if isinstance(late_payment_filters, str):
		late_payment_filters = eval(late_payment_filters)

	report = get_report_doc('Thirvu Report')
	data = get_prepared_report_result(report, late_payment_filters, prepared_report_name, user)
	prepared_report_doc = data['doc']

	base_template_path = "frappe/www/printview.html"
	template_path = "essdee/essdee/report/agent_late_payment/agent_late_payment.html"
	
	print(data)
	ee
	if 'result' in data:
		data = data['result']
		data.pop()
		html = frappe.render_template(template_path, \
				{"filters": late_payment_filters, "data": data, "doc": prepared_report_doc})
		html = frappe.render_template(base_template_path, {"body": html, \
				"css": get_print_style(), "title": "Statement For " + late_payment_filters['customer_group']})

		return html