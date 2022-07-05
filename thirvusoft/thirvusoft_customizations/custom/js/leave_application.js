frappe.ui.form.on("Leave Application",{
    onload:function(frm) {
        frappe.db.get_value('Employee', {'user_id':frappe.session.user}, 'designation', function(r) {
        var designation=r.designation
        frm.set_value("user_designation",designation)
        frm.refresh();
        })

    },
    validate:function(frm) {
            if(frm.doc.user_designation == "Tech Lead"){
                if(frm.doc.status == "Approved by HR Manager" || frm.doc.status == "Rejected by HR Manager"){
                    frappe.throw({
                        title:"Message",
                        message:"Not Permitted"
                    })
                }else if(frm.doc.status == "Approved by Tech Lead"){
                    frm.set_value("tech_lead_approved",1)
                }
               
            }
            if(frm.doc.user_designation == "HR Manager"){
                if(frm.doc.tech_lead_approved == 1){
                    if(frm.doc.status == "Approved by Tech Lead" || frm.doc.status == "Rejected by Tech Lead"){
                        frappe.throw({
                            title:"Message",
                            message:"Not Permitted"
                        })
                    }else if(frm.doc.status == "Approved by HR Manager"){
                        frm.set_value("hr_manager_approved",1)
                    }
                }else if(frm.doc.tech_lead_approved == 0){
                    frappe.throw({
                        title:"Message",
                        message:"Requires Tech Lead Approval"
                    })
                }
                
            }
    },
})