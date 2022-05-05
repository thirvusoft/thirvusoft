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
			"options": ["","Pending Review","Hold","Completed","Cancelled"],
			"width": "100"
		},
		{
			"fieldname":"employee",
			"label": __("Employee"),
			"fieldtype": "Link",
			"options": "Employee",
			"width": "100"
		}

	],
	
	get_datatable_options(options) {
        return Object.assign(options, {
            checkboxColumn: true
        });
    },
	onload: function() {
		frappe.query_report.page.add_inner_button(__("Update Status"), function() {
				var d = new frappe.ui.Dialog({
					size:"large",
					title: "Action",
					fields: [
						{label:'Task Status',fieldname:'task_status',fieldtype:'Select',options: ["Hold","Open","Working","PR Opened","PR Merged","PR Conflicts","PR Closed","Deployed to Production","Development Testing Started","Development Testing Ended","CI Verified","Client Satisfied","Overdue","Completed","Cancelled"],reqd:1},
						{fieldtype:'Column Break'},
					],
					primary_action:function(data){
						var status = data.task_status
						change_status(status)
						d.hide()
						frappe.msgprint("Status Updated");
					}
					
						})
						d.show()	
		});
		
	}
};

var change_status = function(status){	
		let checked_rows_indexes = frappe.query_report.datatable.rowmanager.getCheckedRows();
		let checked_rows = checked_rows_indexes.map(i => frappe.query_report.data[i]);
			var task_list = []
			for(var i=0;i<checked_rows.length;i++)
				{
					task_list.push(checked_rows[i].task_id)
					
				}
				console.log(task_list)
				for(let i in task_list){
						frappe.call({
							method: "thirvusoft.thirvusoft_customizations.custom.python.reports.task_status",
							args: {
								name: task_list[i],
								value: status
							},
						});
				}	
}



