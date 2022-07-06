// Copyright (c) 2022, ThirvuSoft Private Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('TS Customer Requirement Sheet', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on('TS Customer Requirement Sheet Details', {
	ts_requirements_add: function(frm,cdt,cdn){
	   frappe.model.set_value(cdt,cdn,"ts_date",frappe.datetime.nowdate())
	},
   
});
