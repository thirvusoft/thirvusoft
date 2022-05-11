// frappe.ui.form.on('Task', {
//     after_save:async function(frm) {
//             let assign_too = [];
//             if(frm.doc.assigned_ci){
//                 frappe.db.get_doc("Employee",frm.doc.assigned_ci).then(ts_employee=>{
//                     console.log(ts_employee.user_id)
//                     assign_too.push(ts_employee.user_id);
//                 })
//             }
//             if(frm.doc.assigned_team_member){
//                 frappe.db.get_doc("Employee",frm.doc.assigned_team_member).then(ts_employee=>{
//                     console.log(ts_employee.user_id)
//                     assign_too.push(ts_employee.user_id);
//                 })
//             }
//             if(frm.doc.assigned_tech_lead){
//                 frappe.db.get_doc("Employee",frm.doc.assigned_tech_lead).then(ts_employee=>{
//                     console.log(ts_employee.user_id)
//                     assign_too.push(ts_employee.user_id);
//                 })
//             }
//             if(assign_too){
//                 cur_frm.assign_to.add();
//                 cur_frm.assign_to.assign_to.dialog.set_values({assign_to:assign_too});
//                 setTimeout(() => {
//                     frm.assign_to.assign_to.dialog.primary_action();
//                 }, 3000);
//             }
//         },
// });

frappe.ui.form.on("Task",{
    validate:function(frm,cdt,cdn){
        var ts_data=locals[cdt][cdn]
        console.log(ts_data.status)
        if(ts_data.status=="PR Verified"){
            if(ts_data.ts_pr_review_member_email!=frappe.user.name){
                frappe.throw({
                    title:"Message",
                    message:"Not Permitted"
                })
            }
        }
        if((["PR Conflicts","PR Merged","PR Closed","Deployed To Production","Cancelled","Hold"]).includes(ts_data.status)){
            if(ts_data.ts_assigned_tech_lead_mail!=frappe.user.name){
                frappe.throw({
                    title:"Message",
                    message:"Not Permitted"
                })
            }
        }
        if((["Working","PR Opened","Development Testing Started","Development Testing Ended"]).includes(ts_data.status)){
            if(ts_data.ts_assigned_team_member_mail!=frappe.user.name){
                frappe.throw({
                    title:"Message",
                    message:"Not Permitted"
                })
            }
        }
        if((["CRM Verified","Client Satisfied"]).includes(ts_data.status)){
            if(ts_data.ts_assigned_crm_mail!=frappe.user.name){
                frappe.throw({
                    title:"Message",
                    message:"Not Permitted"
                })
            }
        }
        if(ts_data.status=="Completed"){
            var today = new Date();
            var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
            frappe.model.set_value(cdt,cdn,"completed_on",date)
            frappe.model.set_value(cdt,cdn,"completed_by",frappe.user.name)
        }
    }
})
frappe.ui.form.on('Task', {
          ts_create_pr: function(frm, cdt, cdn) {
                    window.open(frm.doc.ts_github_repo_link+'/compare/');
          }
});
