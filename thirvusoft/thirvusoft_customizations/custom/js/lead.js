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
    },
    refresh: function(frm) {
        cur_frm.remove_custom_button("Opportunity","Create")
        frm.add_custom_button(__('Customer Requirement Sheet'), function(){
            let client_type = ""
            let lead = ""
            if(cur_frm.doc.status == "Lead")
            {
                client_type = cur_frm.doc.status
                lead = cur_frm.doc.name
            }
            frappe.run_serially([
            () => frappe.new_doc("TS Customer Requirement Sheet"),
            () => {if(client_type == "Lead"){
                cur_frm.set_value("client_type",client_type)
                cur_frm.set_value("lead",lead)
            }
            }
        ])
            
        }, __("Create"));
    },
    next_contact_date: function(frm){
        cur_frm.set_value("contact_date", frm.doc.next_contact_date)
        cur_frm.refresh()
    }
})