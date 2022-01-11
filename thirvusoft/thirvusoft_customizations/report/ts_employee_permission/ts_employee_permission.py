# Copyright (c) 2013, ThirvuSoft Private Limited and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	filters = frappe._dict(filters or {})
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data
def get_columns(filters):
	columns = [
		{
			"label":_("Date"),
			 "fieldname":"date",
			 "fieldtype":"date"
		},
		{
			"label":_("Employee ID"),
			 "fieldname":"employee",
			 "fieldtype":"Link",
			 "options":"Employee"

		},
		{
			"label":_("Employee Name"),
			 "fieldname":"name",
			 "fieldtype":"Data",
			 "width":150
		},
		{
			"label":_("From Time"),
			 "fieldname":"start_time",
			 "fieldtype":"Time"
		},
		{
			"label":_("To Time"),
			 "fieldname":"end_time",
			 "fieldtype":"Time"
		},
		{
			"label":_("Absent Time"),
			 "fieldname":"hours",
			 "fieldtype":"Time"
		},
		{
			"label":_("Reason"),
			 "fieldname":"reason",
			 "fieldtype":"Text",
			 "width":200
		}
	]
	return columns
def get_data(filters):
	if(filters.start_date and filters.end_date):
		startdate=filters.start_date
		enddate=filters.end_date
	all_doc=frappe.get_all('TS Employee Permission')
	dates=[]
	for date in [date.name for date in all_doc]:
		if(date>=startdate and date<=enddate):	
			dates.append(date)
	data=[]
	for date in dates:
		doc=frappe.get_doc('TS Employee Permission',date)
		for emp in doc.permission_details:
			row={'date':doc.date,'employee':emp.employee,'name':emp.employee_name,'start_time':emp.start_time,'end_time':emp.end_time,'hours':emp.hours,'reason':emp.reason}
			data.append(row)


	return data
		