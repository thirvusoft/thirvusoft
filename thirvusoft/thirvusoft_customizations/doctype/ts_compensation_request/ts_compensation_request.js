frappe.ui.form.on("TS Compensation Request",{
    employee:function(frm){
        frappe.call({
            method:"thirvusoft.thirvusoft_customizations.custom.python.compensation.cm_approver",
            args:{
                'em_name':cur_frm.doc.employee,
            },
            callback: function(r){
				var approver=r.message[0]
                frm.set_value("compen_approver",approver)
            }
        })
    },
	compen_approver:function(frm){
        frappe.call({
            method:"thirvusoft.thirvusoft_customizations.custom.python.compensation.cm_name",
            args:{
                'approver_name':cur_frm.doc.compen_approver,
            },
            callback: function(r){
				var approver=r.message[0]
				console.log(approver)
                frm.set_value("ts_compen_approver_name",approver)
            }
        })
    }
})