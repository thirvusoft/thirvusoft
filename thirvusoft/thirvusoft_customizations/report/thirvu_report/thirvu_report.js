// Copyright (c) 2022, ThirvuSoft Private Limited and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Thirvu Report"] = {
	onload: function(query_report) {
        query_report.page.clear_menu();
        query_report.page.add_menu_item(__("Send This Report To Whatsapp"), () => {
            const filters = JSON.stringify(query_report.get_values());
            const query_string = frappe.utils.get_query_string(frappe.get_route_str());
            const query_params = frappe.utils.get_query_params(query_string);
            frappe.call({
                method: "path",
                freeze: true,
                args: {action:'send_single_report', filters: filters, prepared_report_name: query_params.prepared_report_name, report_name: 'Agent Outstanding'}
            }
        );
    }
        )
},
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
