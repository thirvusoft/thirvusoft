// Copyright (c) 2022, ThirvuSoft Private Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('Requirement Sheet', {
	 refresh: function(frm){
		frm.set_value("date",frappe.datetime.nowdate())
	 },
	
});
