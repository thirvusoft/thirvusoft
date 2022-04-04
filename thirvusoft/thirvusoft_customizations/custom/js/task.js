frappe.ui.form.on('Task', {
    after_save: function(frm) {
            let assign_too = [];
            if(frm.doc.assigned_ci){
                assign_too.push(frm.doc.assigned_ci);
            }
            if(frm.doc.assigned_team_member){
                assign_too.push(frm.doc.assigned_team_member);
            }
            if(frm.doc.assigned_tech_lead){
                assign_too.push(frm.doc.assigned_tech_lead);
            }
            if(assign_too.length!=0){
                cur_frm.assign_to.add();
                cur_frm.assign_to.assign_to.dialog.set_values({assign_to:assign_too});
                setTimeout(() => {
                    frm.assign_to.assign_to.dialog.primary_action();
                }, 100);
            }
        },
});