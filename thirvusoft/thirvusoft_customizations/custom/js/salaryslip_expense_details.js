frappe.ui.form.on('Salary Slip', {
    ts_fetch_expense: function(frm,cdt,cdn) {
        let k = 0;
        frappe.call({
            method:"thirvusoft.thirvusoft_customizations.custom.python.salaryslip_expense_details.salaryslip",
            args:{doc:frm.doc},
            callback(res){
                frm.set_value("ts_reimbursement_",[])
                var total = 0;
                for(let i of res.message)
                {
                    for (const [key, value] of Object.entries(i)) {
                        let p=locals[cdt][cdn]
                            cur_frm.add_child("ts_reimbursement_")
                            frappe.model.set_value(p.ts_reimbursement_[k].doctype,p.ts_reimbursement_[k].name,"ts_expense_claim_type",key)
                            frappe.model.set_value(p.ts_reimbursement_[k].doctype,p.ts_reimbursement_[k].name,"ts_total_expense_claim",value)
                            
                            cur_frm.refresh_field('ts_reimbursement_')
                            k+=1;
                            total+=value;
                        cur_frm.refresh_field('ts_reimbursement_')
                        frm.refresh()
                    }
                }
                frm.set_value("ts_total_reimbursement",total)
                frm.refresh()
            }
        }) 
    },
});
