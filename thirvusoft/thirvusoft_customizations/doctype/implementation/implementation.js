// Copyright (c) 2022, ThirvuSoft Private Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('Implementation', {
	refresh: function(frm) {
		frm.set_value("date",frappe.datetime.nowdate())

	}
});
frappe.ui.form.on('Implementation Sheet',{
    hours_spend:function(frm,cdt,cdn){
        var row = locals[cdt][cdn];
		var hours = row.hours_spend;
		var total_hrs = frm.doc.total_hours? frm.doc.total_hours:0;
		frm.set_value("total_hours",hours+total_hrs);
	
    },
	implementation_sheet_remove:function(frm,cdt,cdn)
	{
		var total_hour=0;
		for(var i=0;i<cur_frm.doc.implementation_sheet.length;i++)
		{
			total_hour+=cur_frm.doc.implementation_sheet[i].hours_spend?cur_frm.doc.implementation_sheet[i].hours_spend:0;

			
		}
		frm.set_value("total_hours",total_hour);
	}
})

