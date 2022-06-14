// Copyright (c) 2022, ThirvuSoft Private Limited and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Thirvu Report"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default" :frappe.datetime.get_today(),
			"reqd": 1
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default" :frappe.datetime.get_today(),
			"reqd": 1
		},
		{
            "fieldname": "project",
            "label": __("Project"),
            "fieldtype": "Link",
            "options": "Project",
            "reqd": 1
        },
		

	]
};
