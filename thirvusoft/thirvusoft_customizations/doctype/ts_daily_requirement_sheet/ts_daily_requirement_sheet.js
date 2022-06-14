// Copyright (c) 2022, ThirvuSoft Private Limited and contributors
// For license information, please see license.txt
var ts_child_data
frappe.ui.form.on('TS Daily Requirement Sheet Details', {
	ts_assing_task:async function(frm,cdt,cdn){
		var ts_user=frappe.user.name
		var ts_data=locals[cdt][cdn]
		ts_child_data=ts_data
		var ts_value=0
		await frappe.call({
			method:"thirvusoft.thirvusoft_customizations.doctype.ts_daily_requirement_sheet.ts_daily_requirement_sheet.tech_lead_name_finder",
			args:{ts_user,ts_value},
			callback(ts_r){
				if(ts_r.message){
					if(ts_r.message==1){
						frappe.throw({
							title:"Message",
							message:"Not Permitted"
						})
					}
				}
			}
		}),
		frappe.call({
			method:"thirvusoft.thirvusoft_customizations.doctype.ts_daily_requirement_sheet.ts_daily_requirement_sheet.employee_role",
			args:{ts_user,ts_data},
			callback(ts_r){
				if(ts_r.message===1){
					frappe.throw({
						title:"Message",
						message:"Scurm Master Role Is Not Assigned"
					})
				}
				else{
					frappe.model.set_value(cdt,cdn, "ts_task_assigned_by", ts_r.message[0])
					frappe.model.set_value(cdt,cdn, "ts_tech_lead_name", ts_r.message[1])
					frm.save_or_update();
			frappe.show_alert({ message:__('Task Created'), indicator:'green' });
				}
			}
		})
	}
 })
 frappe.ui.form.on("TS Daily Requirement Sheet",{
	ts_add_requirement: function(frm,cdt,cdn) {
		var d = new frappe.ui.Dialog({
			size:"large",
			title: "Add Requirements",
			fields: [
				{label:'Subject',fieldname:'ts_subject',fieldtype:'Data',reqd:1},
				{fieldtype:'Column Break'},
				{label:'Project',fieldname:'ts_project',fieldtype:'Link',options: 'Project',reqd:1},
				{fieldtype:'Section Break'},
				{label:'Department',fieldname:'ts_department',fieldtype:'Link',options: 'Department',reqd:1},
				{fieldtype:'Column Break'},
				{label:'Assigned Team Member',fieldname:'ts_assigned_member',fieldtype:'Link',options:"Employee",reqd:1},
				{fieldtype:'Column Break'},
				{label:'Assigned CRM Member',fieldname:'ts_assigned_crm_member',fieldtype:'Link',options:"Employee",reqd:1,default:frappe.user.name,read_only:1},
				{fieldtype:'Section Break'},
				{label:'Expected Start Date',fieldname:'ts_expected_start_date',fieldtype:'Date',reqd:1},
				{fieldtype:'Column Break'},
				{label:'Expected Hours',fieldname:'ts_expected_hours',fieldtype:'Float',reqd:1},
				{fieldtype:'Section Break'},
				{label:'Freezing Date',fieldname:'ts_freezing_date',fieldtype: 'Date',reqd:1},
				{fieldtype:'Column Break'},
				{label:'Planned Commitment Date',fieldname:'ts_planned_commitment_date',fieldtype: 'Date',reqd:1},
				{fieldtype:'Column Break'},
				{label:'Priority',fieldname:'ts_priority',fieldtype: 'Select',options:["","Low","Medium","High","Urgent"],reqd:1},
				{fieldtype:'Section Break'},
				{label:'Requirement',fieldname:'ts_requriement',fieldtype:'Text Editor',reqd:1},
			],
			primary_action_label: "➕",
			primary_action:function(data){
				var child = cur_frm.add_child("ts_requirement");
				frappe.model.set_value(child.doctype, child.name, "ts_subject", data.ts_subject)
				frappe.model.set_value(child.doctype, child.name, "ts_project", data.ts_project)
				frappe.model.set_value(child.doctype, child.name, "ts_department", data.ts_department)
				frappe.model.set_value(child.doctype, child.name, "ts_assigned_member", data.ts_assigned_member)
				frappe.db.get_doc("Employee",data.ts_assigned_member).then(ts_employee=>{
					frappe.model.set_value(child.doctype, child.name, "ts_assigned_member_name", ts_employee.employee_name)
				})
				frappe.model.set_value(child.doctype, child.name, "ts_requriement", data.ts_requriement)
				frappe.model.set_value(child.doctype, child.name, "ts_expected_hours", data.ts_expected_hours)
				frappe.model.set_value(child.doctype, child.name, "ts_expected_start_date", data.ts_expected_start_date)
				frappe.model.set_value(child.doctype, child.name, "ts_freezing_date", data.ts_freezing_date)
				frappe.model.set_value(child.doctype, child.name, "ts_priority", data.ts_priority)
				frappe.model.set_value(child.doctype, child.name, "ts_planned_commitment_date", data.ts_planned_commitment_date)
				var ts_user=data.ts_assigned_crm_member
				var ts_value=1
				frappe.call({
					method:"thirvusoft.thirvusoft_customizations.doctype.ts_daily_requirement_sheet.ts_daily_requirement_sheet.tech_lead_name_finder",
					args:{ts_user,ts_value},
					callback(ts_r){
						if(ts_r.message){
							frappe.model.set_value(child.doctype, child.name,"ts_assigned_crm_member",ts_r.message)
						}
					}
				})
				frappe.db.get_doc("User",data.ts_assigned_crm_member).then(ts_employee=>{
					frappe.model.set_value(child.doctype, child.name, "ts_assigned_crm_name", ts_employee.full_name)
				})
				cur_frm.refresh_field("ts_requirement")
				d.hide()  
			}
		})
		d.show()
	},
	onload:function(frm,cdt,cdn){
		var ts_user=frappe.user.name
		var ts_value=1
		frappe.call({
			method:"thirvusoft.thirvusoft_customizations.doctype.ts_daily_requirement_sheet.ts_daily_requirement_sheet.tech_lead_name_finder",
			args:{ts_user,ts_value},
			callback(ts_r){

				if(ts_r.message)
				{
					frm.set_query("ts_project","ts_requirement", function() {
						return {
							filters: {'ts_assigned_crm' :ts_r.message}
						}
					})
				}
			}
		})
		frappe.call({
			method:"thirvusoft.thirvusoft_customizations.doctype.ts_daily_requirement_sheet.ts_daily_requirement_sheet.pending_requirement_finder",
			args:{ts_user},
			callback(ts_r){
				if(ts_r.message){
					var details=ts_r.message
					for(var i=0;i<details.length;i++){
						for(var j=0;j<details[i].length;j++){
							let row = frm.add_child("ts_pending_requirement");
							row.ts_subject = details[i][j]["ts_subject"]
							row.ts_project = details[i][j]["ts_project"]
							row.ts_department = details[i][j]["ts_department"]
							row.ts_assigned_member = details[i][j]["ts_assigned_member"]
							row.ts_assigned_member_name = details[i][j]["ts_assigned_member_name"]
							row.ts_expected_start_date = details[i][j]["ts_expected_start_date"]
							row.ts_expected_hours = details[i][j]["ts_expected_hours"]
							row.ts_freezing_date = details[i][j]["ts_freezing_date"]
							row.ts_planned_commitment_date = details[i][j]["ts_planned_commitment_date"]
							row.ts_priority = details[i][j]["ts_priority"]
							row.ts_requriement = details[i][j]["ts_requriement"]
							row.ts_assigned_crm_member = details[i][j]["ts_assigned_crm_member"]
							row.ts_assigned_crm_name = details[i][j]["ts_assigned_crm_name"]
							frm.refresh_field("ts_pending_requirement");
						}
					}
				}
			}
		})
	},
	validate:function(frm,cdt,cdn){
		var ts_data=locals[cdt][cdn]
		if(ts_data.ts_pending_requirement){
			var ts_pending_table=ts_data.ts_pending_requirement
			for(var i=0;i<ts_pending_table.length;i++){
				if(!ts_pending_table[i].new_requirement_added_by){
					frappe.throw({
						title:"Message",
						message:"Pending Requirement Not Added To New Requirement In Row : "+(i+1)
					})
				}
			}
		}
	}
})
frappe.ui.form.on("TS Pending Task Requirement Sheet",{
	ts_add_to_new_requirements:function(frm,cdt,cdn){
		var ts_data=locals[cdt][cdn]
		let row = frm.add_child("ts_requirement");
		row.ts_subject = ts_data.ts_subject
		row.ts_project = ts_data.ts_project
		row.ts_department = ts_data.ts_department
		row.ts_assigned_member = ts_data.ts_assigned_member
		row.ts_assigned_member_name = ts_data.ts_assigned_member_name
		row.ts_expected_start_date = ts_data.ts_expected_start_date
		row.ts_expected_hours = ts_data.ts_expected_hours
		row.ts_freezing_date = ts_data.ts_freezing_date
		row.ts_planned_commitment_date = ts_data.ts_planned_commitment_date
		row.ts_priority = ts_data.ts_priority
		row.ts_requriement = ts_data.ts_requriement
		row.ts_assigned_crm_member = ts_data.ts_assigned_crm_member
		row.ts_assigned_crm_name = ts_data.ts_assigned_crm_name
		row.ts_is_pending_requirement=1
		frm.refresh_field("ts_requirement");
		frappe.model.set_value(cdt,cdn,"new_requirement_added_by",ts_data.ts_assigned_crm_member)
		frappe.show_alert({ message:__('Added To New Requirements'), indicator:'green' });
	}
})