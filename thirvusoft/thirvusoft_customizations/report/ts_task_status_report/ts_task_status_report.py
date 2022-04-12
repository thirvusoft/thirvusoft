# Copyright (c) 2022, Thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	from_date = filters.get("from_date")
	to_date = filters.get("to_date")
	project = filters.get("project")
	status = filters.get("status")
	conditions = ""
	if from_date or to_date or project or status:
		conditions = " where 1 = 1 "
		if from_date and to_date:
			conditions += " and task.exp_start_date between '{0}' and '{1}' ".format(from_date, to_date)
		if project:
			conditions += " and task.project = '{0}'".format(project)
		if status:
			conditions += " and phase.status = '{0}'".format(status)
	report_data = frappe.db.sql(""" select task.project,phase.phase,phase.status,phase.start_date,phase.end_date,sum(task.expected_time),sum(task.actual_time),count(task.project),
       									project.percent_complete,task._assign,task.assigned_tech_lead,phase.assigned_ci
								    from tabTask as task
								    left outer join  tabProject as project on
  										project.name = task.project 
									left outer join `tabTS Project Phase` as phase on
   										project.name = phase.parent and task.phase = phase.phase
									{0}
								    GROUP BY project.name,phase.phase """.format(conditions))
	data = [list(i) for i in report_data]
	columns= get_columns()
	user=[[frappe.get_all("User",fields=['username'],filters={'email':j})[0]['username'] for j in eval(i[9])] for i in data]
	for i in range(len(user)):data[i][9] = str(user[i])[1:-1:]
	tl_user=[frappe.get_all("User",fields=['username'],filters={'email':i[10]})[0]['username'] for i in data]
	for i in range(len(tl_user)):data[i][10] = str(tl_user[i])
	ci_user=[frappe.get_all("User",fields=['username'],filters={'email':i[11]})[0]['username'] for i in data]
	for i in range(len(ci_user)):data[i][11] = str(ci_user[i])
	return columns, data

def get_columns():
	columns = [
		_("Project") + ":Link/Project:130",
		_("Phase No") + ":Int:80",
		_("Status") + ":Data:100",
		_("Expected Start Date") + ":Date:150",
		_("Expected End Date") + ":Date:150",
		_("Total Expected Hrs") + ":Int:150",
		_("Total Actual Hrs") + ":Int:150",
		_("Total Tasks") + ":Int:100",
		_("Completion Percentage") + ":Percent:150",
		_("Assigned Peoples") + ":Data:250",
		_("Tech Lead") + ":Data:150",
		_("Client Intraction") + ":Data:150"
		
		]
	
	return columns