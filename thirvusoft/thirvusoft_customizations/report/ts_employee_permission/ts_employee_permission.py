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
			 "width":200
		},
		{
			"label":_("Reason"),
			 "fieldname":"reason",
			 "fieldtype":"Text",
			 "width":200
		},
		{
			"label":_("Absent Time"),
			 "fieldname":"hours",
			 "fieldtype":"Time"
		},
	]
	return columns
def get_conditions(filters):
	conditions ={}
	if(filters.date):
		conditions['date']=filters.date
	return conditions



def get_data(filters):
	data=[]
	conditions=get_conditions(filters)
	date=conditions['date']
	print(date)
	emp = frappe.get_doc("TS Employee Permission",date,order_by="employee")
	for i in emp.get("permission_details"):
		name=i.first_name
		if(i.middle_name!=None):name+=' '+i.middle_name
		if(i.last_name!=None):name+=' '+i.last_name
		print(name,i.hours)
		#row={'date':i.date, 'employee':i.permission_details.employee}
		row={'date':date, 'employee':i.employee, 'name':name, 'reason':i.reason, 'hours':i.hours}
		data.append(row)
	return data