// Copyright (c) 2022, ThirvuSoft Private Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('Minutes of meeting', {
	onload: function(frm) {	
		frm.add_fetch("client","client_name","client_name");
		frm.add_fetch("client","client_contact_number","client_contact_number");
	 }
});

