// Copyright (c) 2016, ThirvuSoft Private Limited and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["TS Employee Permission"] = {
	"filters": [
		{
			fieldname:"start_date",
			label: __("Date"),
			fieldtype: "Date",
			reqd:1
		},
		{
			fieldname:"end_date",
			label: __("Date"),
			fieldtype: "Date",
			reqd:1
		},
		
	]
};
