# Copyright (c) 2022, ThirvuSoft Private Limited and contributors
# For license information, please see license.txt


import frappe
from frappe import _
from frappe.utils import nowdate
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
			conditions += " and task.ts_assigned_team_member ='{0}' ".format(employee)
		if status:
			conditions += " and task.status = '{0}' ".format(status)
	report_data = frappe.db.sql("""select task.name,task.ts_assigned_team_member,emp.employee_name,task.exp_start_date,task.expected_time,task.ts_assigned_ci_name,actual_time,task.status
									from tabTask as task
									left outer join tabEmployee as emp on
  										  task.ts_assigned_team_member = emp.name
									{0}
								""".format(conditions))
	data = [list(i) for i in report_data]

	columns = get_columns()
	return columns, data

def get_columns():
	columns = [
		_("Task ID") + ":Link/Task:150",
		_("Employee") + ":Data:200",
		{
			"fieldname":"employee_name",
			"fieldtype": "Data",
			"hidden": 1,
			
		},
		_("Expected Start Date") + ":Data:180",
		_("Expected time") + ":data:130",
		_("Assigned PM") + ":Data:180",
		_("Actual Time") + ":data:100",
		_("Task Status") + ":Data:180",

		]
	
	return columns

@frappe.whitelist()
def task_status(task_name,task_status):
    task_doc= frappe.get_doc('Task',task_name)
    if (task_status == "Completed"):
        task_doc.update({
            'status':task_status,
            'completed_on':nowdate()
        })
        task_doc.save()
        frappe.db.commit()
    else:
        task_doc.update({
                'status':task_status
            })
        task_doc.save()
        frappe.db.commit()
		