frappe.ui.form.on("Project",{
    onload:function(frm,cdt,cdn){
    frm.set_query("ts_assigned_crm", function() {
        return {
            filters: {'designation' :"Customer Relationship Manager"}
        }
    })
    }
})