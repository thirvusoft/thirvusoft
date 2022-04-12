// Copyright (c) 2022, ThirvuSoft Private Limited and contributors
// For license information, please see license.txt
/* eslint-disable */
frappe.query_reports["Project Tracking"] = {
    "filters": [
        {
            "fieldname": "project",
            "label": __("Project"),
            "fieldtype": "Link",
            "options": "Project",
        },
        {
            "fieldname": "ci",
            "label": __("CI"),
            "fieldtype": "Link",
            "options": "User",
            "get_query": function(){
                return{
                    filters: {"role_profile_name": "CI"}
                }
            }
        },
        {
            "fieldname": "phase",
            "label": __("Phase"),
            "fieldtype": "Select",
			"options":["",1,2,3,4,5]
        },
        {
            "fieldname": "phase_status",
            "label": __("Phase Status"),
            "fieldtype": "Select",
            "options": ["","Open","Working","Hold","Completed","Cancelled"],
            "default": "",
        },
    ]
};









