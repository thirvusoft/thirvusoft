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
			'label':_('Name')
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
			'fieldtype':'Data',
			'label':_('Total Time')
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
	emp=frappe.get_all('TS Hourly Details')
	if(filters.start_date and filters.end_date):
		a=filters.start_date
		b=filters.end_date
		data=[]
		for i in emp:
			z=frappe.get_doc('TS Hourly Details',i.name)		
			if(str(z.date)>=a and str(z.date)<=b):	
				row={'employee_id':z.employee_id, 'date':z.date, 'name':z.employee_name, 
				'start_time':z.start_time, 'end_time':z.end_time, 'reason':z.reason, 'hours':z.hours}
				data.append(row)
		return data

