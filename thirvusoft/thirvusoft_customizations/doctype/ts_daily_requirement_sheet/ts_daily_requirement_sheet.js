// Copyright (c) 2022, ThirvuSoft Private Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('TS Daily Requirement Sheet', {
	ts_add_requirement: function(frm,cdt,cdn) {
		var d = new frappe.ui.Dialog({
			title: "Add Requirements........",
			fields: [
				{label:'Project',fieldname:'ts_project',fieldtype:'Link',options: 'Project',reqd:1},
				{fieldtype:'Column Break'},
				{label:'Department',fieldname:'ts_department',fieldtype:'Link',options: 'Department',reqd:1},
				{fieldtype:'Column Break'},
				{label:'Assigend Member',fieldname:'ts_assigend_member',fieldtype:'Link',options:"User",reqd:1},
				{fieldtype:'Section Break'},
				{label:'Expected Hours',fieldname:'ts_expected_hours',fieldtype:'Float',reqd:1},
				{fieldtype:'Column Break'},
				{label:'Expected Start Date',fieldname:'ts_expected_start_date',fieldtype:'Date',reqd:1},
				{fieldtype:'Column Break'},
				{label:'Expected End Date',fieldname:'ts_expected_end_date',fieldtype:'Date',reqd:1},
				{fieldtype:'Section Break'},
				{label:'Required Nature Date',fieldname:'ts_required_nature_date',fieldtype: 'Date',reqd:1},
				{fieldtype:'Column Break'},
				{label:'Priority',fieldname:'ts_priority',fieldtype: 'Select',options:["","Low","Medium","High","Urgent"],reqd:1},
				{fieldtype:'Column Break'},
				{label:'Planned Commitment Date',fieldname:'ts_planned_commitment_date',fieldtype: 'Date',reqd:1},
				{fieldtype:'Section Break'},
				{label:'Requirement',fieldname:'ts_requriement',fieldtype:'Long Text',reqd:1},
			],
			primary_action_label: "➕",
			primary_action: function(data){
				var child = cur_frm.add_child("ts_requirement");
				frappe.model.set_value(child.doctype, child.name, "ts_project", data.ts_project)
				frappe.model.set_value(child.doctype, child.name, "ts_department", data.ts_department)
				frappe.model.set_value(child.doctype, child.name, "ts_assigend_member", data.ts_assigend_member)
				frappe.model.set_value(child.doctype, child.name, "ts_requriement", data.ts_requriement)
				frappe.model.set_value(child.doctype, child.name, "ts_expected_hours", data.ts_expected_hours)
				frappe.model.set_value(child.doctype, child.name, "ts_expected_start_date", data.ts_expected_start_date)
				frappe.model.set_value(child.doctype, child.name, "ts_expected_end_date", data.ts_expected_end_date)
				frappe.model.set_value(child.doctype, child.name, "ts_required_nature_date", data.ts_required_nature_date)
				frappe.model.set_value(child.doctype, child.name, "ts_priority", data.ts_priority)
				frappe.model.set_value(child.doctype, child.name, "ts_planned_commitment_date", data.ts_planned_commitment_date)
				cur_frm.refresh_field("ts_requirement")
				d.hide()   
			}
		})
		d.show()
	}
})