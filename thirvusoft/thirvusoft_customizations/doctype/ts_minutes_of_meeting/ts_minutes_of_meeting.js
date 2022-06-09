// Copyright (c) 2022, ThirvuSoft Private Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('TS Minutes of Meeting', {
	project: function(frm, cdt, cdn) {
		let p= locals[cdt][cdn]	
		let l=frappe.db.get_value("Project", p.project, ["client_name","client_contact_number"]).then(function(f){
			frappe.model.set_value(cdt,cdn,'client',f.message.client_name)
			frappe.model.set_value(cdt,cdn, 'client_contact_number',f.message.client_contact_number)
		})
		
		// console.log(l)
		// 		frm.add_fetch("client","client_name","client_name");
		// frm.add_fetch("client","client_contact_number","client_contact_number");
	 }
});
