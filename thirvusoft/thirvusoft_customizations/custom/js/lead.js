frappe.ui.form.on("Lead",{
    'delete_notif_log': function(frm){
        frappe.call({
            method: "thirvusoft.thirvusoft_customizations.custom.python.lead_notification.delete_notification_log",
            args:{doc:"Lead", name:frm.doc.name},
            callback(r){
                if(r.message){
                    frappe.msgprint("Notification Log related to this document <b>Deleted Successfully</b>.")
                }
                else{
                    frappe.msgprint("Notification Log not found for this document.")
                }
            }
        })
    }
})