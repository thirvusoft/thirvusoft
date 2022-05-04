# Copyright (c) 2022, ThirvuSoft Private Limited and contributors
# For license information, please see license.txt


import frappe
from frappe import _

def execute(filters=None):
	from_date = filters.get("from_date")
	to_date = filters.get("to_date")
	employee = filters.get("employee")
	status = filters.get("status")
	conditions = ""
	if from_date or to_date or employee or status:
		conditions = " where 1 = 1 "
		if from_date and to_date:
			conditions += " and task.exp_start_date between '{0}' and '{1}' ".format(from_date, to_date)
		if employee:
			conditions += " and task.assigned_team_member ='{0}' ".format(employee)
		if status:
			conditions += " and task.status = '{0}' ".format(status)
	report_data = frappe.db.sql("""select task.name,task.assigned_team_member,emp.employee_name,task.assigned_ci,task.status,task.ts_reason
									from tabTask as task
									left outer join tabEmployee as emp on
  										  task.assigned_team_member = emp.name
									{0}
								""".format(conditions))
	data = [list(i) for i in report_data]
	ci_name=[frappe.get_all("Employee",fields=['employee_name'],filters={'name':i[3]})[0]['employee_name'] for i in data]
	for i in range(len(ci_name)):data[i][3] = str(ci_name[i])
	columns = get_columns()
	return columns, data

def get_columns():
	columns = [
		_("Task ID") + ":Link/Task:180",
		_("Employee") + ":Data/Employee:180",
		_("Employee Name") + ":Data/Employee:180",
		_("CI") + ":Data/Employee:180",
		_("Task Status") + ":Data/Task:180",
		_("Reason") + ":Data:500",
		]
	
	return columns
		