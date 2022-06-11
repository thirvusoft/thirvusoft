// Copyright (c) 2022, ThirvuSoft Private Limited and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["TS Daily Task Report"] = {
	"filters": [
		{
			'label': 'Project',
			'fieldtype': 'Link',
			'fieldname':'project',
			'options': 'Project',
			'reqd': 1
		}
	]
};
