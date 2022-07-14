frappe.ui.form.on('Employee', {
	employment_type: function (frm) {
        var abbreviation = cur_frm.doc.employment_type.slice(0,3)
		cur_frm.set_value('abbr',abbreviation.toUpperCase())
	},
    before_save:function(frm){
        if(!cur_frm.doc.employment_type){
            cur_frm.set_value('abbr','EMP')
        }
    }
})