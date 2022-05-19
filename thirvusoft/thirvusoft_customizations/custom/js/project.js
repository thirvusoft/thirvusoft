frappe.ui.form.on("Project",{
    setup:function(frm,cdt,cdn){
        var ts_filter=["Product Manager","Tech Lead"]
    frm.set_query("ts_assigned_crm", function() {
        return {
            filters: {'designation': ["in", ts_filter]}
        }
    })
    }
})