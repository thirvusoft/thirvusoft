// Copyright (c) 2022, ThirvuSoft Private Limited and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["TS Scrum Tool"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"width": "80"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"width": "80"
		},
		{
			"fieldname":"status",
			"label": __("Task Status"),
			"fieldtype": "Select",
			"options": ["","Open","Working","Pending Review","Overdue","Template","Completed","Cancelled"],
			"width": "100"
		},
		{
			"fieldname":"employee",
			"label": __("Employee"),
			"fieldtype": "Link",
			"options": "Employee",
			"width": "100"
		}

	]
};
