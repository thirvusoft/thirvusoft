# Copyright (c) 2013, ThirvuSoft Private Limited and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from datetime import datetime
def execute(filters=None):
	filters=frappe._dict(filters or {})
	columns, data = get_columns(), get_data(filters)
	return columns, data
def get_columns():
	columns=[
		{
			'fieldname':'employee_id',
			'fieldtype':'Data',
			'label':_('Employee ID')
		},
		{
			'fieldname':'date',
			'fieldtype':'Date',
			'label':_('Date')
		},
		{
			'fieldname':'name',
			'fieldtype':'Data',
			'label':_('Name'),
			'width':150
		},
		{
			'fieldname':'start_time',
			'fieldtype':'Time',
			'label':_('Start Time')
		},
		{
			'fieldname':'end_time',
			'fieldtype':'Time',
			'label':_('End Time')
		},
		{
			'fieldname':'hours',
			'fieldtype':'Time',
			'label':_('Absent Hours'),
			'width':'150'
		},
		{
			'fieldname':'reason',
			'fieldtype':'data',
			'label':_('reason'),
			'width':'150'
		}
	]
	return columns



def get_data(filters):
	emp=frappe.get_all('TS Permission Details')
	if(filters.start_date and filters.end_date):
		startdate=filters.start_date
		enddate=filters.end_date
		data=[]
		for i in emp:
			doc=frappe.get_doc('TS Permission Details',i.name)		
			if(str(doc.date)>=startdate and str(doc.date)<=enddate and doc.docstatus==1):	
				row={'employee_id':doc.employee_id, 'date':doc.date, 'name':doc.employee_name, 
				'start_time':doc.start_time, 'end_time':doc.end_time, 'reason':doc.reason, 'hours':doc.hours}
				data.append(row)
		return data

