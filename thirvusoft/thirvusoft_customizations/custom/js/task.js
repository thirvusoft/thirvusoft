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