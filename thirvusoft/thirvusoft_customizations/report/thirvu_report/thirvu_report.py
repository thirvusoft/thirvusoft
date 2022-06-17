# Copyright (c) 2022, ThirvuSoft Private Limited and contributors
# For license information, please see license.txt

import re
import frappe
import json
from frappe.utils.pdf import get_pdf
from thirvusoft.thirvusoft_customizations.custom.python.api import send_report
from frappe import _
from frappe.utils.file_manager import save_file


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
def get_thirvu_report_html(filters=None):
	filters=json.loads(filters)
	data = get_data(filters)
	html_path='thirvusoft/thirvusoft_customizations/report/thirvu_report/thirvu_report.html'
	html = frappe.render_template(html_path, {'filters':filters, 'data':data, 'doc':{}})
	
	pdf= get_pdf(html, {"orientation": 'Landscape'})
	file=save_file('Thirvu_Report.pdf',pdf,'Report', 'Thirvu Report', is_private=0)
	url=frappe.utils.get_url() + file.file_url
	send_report(filters['project'],url,file.file_name)