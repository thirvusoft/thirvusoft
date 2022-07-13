frappe.ui.form.on("TS Compensation Request",{
    employee:function(){
        console.log("jbnbbbbbbbbbbbb")
        frappe.call({
            method:"thirvusoft.thirvusoft_customizations.custom.python.compensation.cm_approver",
            args:{
                'em_name':cur_frm.doc.employee,
            },
            callback: function(r){
                frappe.msgprint(__(" {0} - User Assigned for {1} Subtype",[cur_frm.doc.user ,  r.message]));
            }
        })
    }
})