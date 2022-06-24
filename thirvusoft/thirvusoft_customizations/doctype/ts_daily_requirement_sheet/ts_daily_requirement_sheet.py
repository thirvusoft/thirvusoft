# Copyright (c) 2022, ThirvuSoft Private Limited and contributors
# For license information, please see license.txt
 
from datetime import datetime

from frappe.model.document import Document
from frappe.desk.form import assign_to
from frappe.desk.form.assign_to import notify_assignment
 
import frappe
class TSDailyRequirementSheet(Document):
   def validate(doc):
        doc.deadline_time = frappe.db.get_single_value("Thirvusoft Settings", "deadline_time")
        finaltime = str(doc.deadline_time)
        time=':'.join([('0'*(2-len(t)))+t for t in finaltime.split(':')])
        now =datetime.now()
        current_time=now.strftime("%H:%M:%S")
        if current_time > time:
            doc.timing=1
            print(current_time, time)
        else:
            doc.timing=0

@frappe.whitelist()
def tech_lead_name_finder(ts_user,ts_value):
    ts_employee_user=frappe.get_doc("User",ts_user)
    if(ts_employee_user):
        ts_employee_user_id=frappe.db.get_values("Employee",filters={"user_id":ts_user},fieldname=["name",'employee_name'])
        try:
            ts_employee_user_id=ts_employee_user_id[0]
            if(ts_value=="0"):
                if(ts_employee_user.role_profile_name=="Tech Lead"):
                    return ts_employee_user_id[0],ts_employee_user_id[1]
                else:
                    return 1
            else:
                return ts_employee_user_id[0]
        except:
            pass

 
 
from frappe.utils import getdate
from datetime import timedelta
@frappe.whitelist()
def employee_role(ts_user,ts_data):
    ts_data=eval(ts_data)
    ts_employee_user_id=frappe.get_doc("User",ts_user)
    if ts_employee_user_id:
        if(ts_employee_user_id.role_profile_name=="Tech Lead"):
            ts_user_details=frappe.db.get_values("User",filters={"role_profile_name":"Scrum Master"},fieldname=["name"])
            if ts_user_details:
                ts_employee_user_id_name=frappe.db.get_values("Employee",filters={"user_id":ts_user},fieldname=["name"])
                ts_employee_user_id_name=ts_employee_user_id_name[0]
                ts_user_details=ts_user_details[0]
                ts_scrum_user_details=frappe.db.get_values("Employee",filters={"user_id":ts_user_details[0]},fieldname=["name","employee_name"])
                ts_scrum_user_details=ts_scrum_user_details[0]
                ts_expected_start_date=getdate(ts_data["ts_expected_start_date"])
                ts_expected_end_date=ts_expected_start_date+timedelta(days=7)
                ts_new_task=frappe.get_doc({
                    "doctype":"Task",
                    "subject":ts_data["ts_subject"],
                    "project":ts_data["ts_project"],
                    "status":"Open",
                    "priority":ts_data["ts_priority"],
                    "assigned_tech_lead_id":ts_employee_user_id_name[0],
                    "assigned_product_manager_id":ts_data["ts_assigned_crm_member"],
                    "assigned_team_member_id":ts_data["ts_assigned_member"],
                    "ts_assigned_tech_lead_name":ts_employee_user_id.full_name,
                    "ts_assigned_ci_name":ts_data["ts_assigned_crm_name"],
                    "ts_assigned_team_member":ts_data["ts_assigned_member_name"],
                    "scrum_master_id":ts_scrum_user_details[0],
                    "ts_scurm_master_name":ts_scrum_user_details[1],
                    "ts_scurm_master_mail":ts_user_details[0],
                    "ts_assigned_team_member_mail":frappe.db.get_value('Employee', ts_data["ts_assigned_member"], 'user_id'),
                    "ts_assigned_crm_mail":frappe.db.get_value('Employee', ts_data["ts_assigned_crm_member"], 'user_id'),
                    "ts_sassigned_tech_lead_mail":frappe.db.get_value('Employee', ts_employee_user_id_name[0], 'user_id'),
                    "exp_start_date":ts_data["ts_expected_start_date"],
                    "exp_end_date":ts_expected_end_date,
                    "expected_time":ts_data["ts_expected_hours"],
                    "description":ts_data["ts_requriement"],
                    "department":ts_data["ts_department"],
                })
                ts_new_task.insert()
                ts_new_task.save()
                employee = frappe.get_doc("Employee",ts_new_task.assigned_product_manager_id)
                ci_email = employee.user_id
                

                employee1= frappe.get_doc("Employee",ts_new_task.assigned_tech_lead_id)
                tech_email = employee1.user_id
                
                
                employee2= frappe.get_doc("Employee",ts_new_task.assigned_team_member_id)
                team_email = employee2.user_id
                
                doc=frappe.new_doc("ToDo")
                doc.update({
                    "owner" : team_email,
                    "description" :  ts_data["ts_subject"],
                    "reference_type" : "Task",
                    "reference_name" : ts_new_task.name,
                    "role" : "All",
                    "assigned_by" : tech_email,
                    
                })
                doc.insert(ignore_permissions=True)
                notify_assignment(doc.assigned_by, doc.owner, doc.reference_type, doc.reference_name, action='ASSIGN',
				description=doc.description)


                doc1=frappe.new_doc("ToDo")
                doc1.update({
                    "owner" : tech_email,
                    "description" : ts_data["ts_subject"],
                    "reference_type" : "Task",
                    "reference_name" : ts_new_task.name,
                    "role" : "All",
                    "assigned_by" : tech_email,
                    
                })
                doc1.insert(ignore_permissions=True)
                notify_assignment(doc1.assigned_by, doc1.owner, doc1.reference_type, doc1.reference_name, action='ASSIGN',
				description=doc1.description)

                doc2=frappe.new_doc("ToDo")
                doc2.update({
                    "owner" :  ci_email,
                    "description" : ts_data["ts_subject"],
                    "reference_type" : "Task",
                    "reference_name" : ts_new_task.name,
                    "role" : "All",
                    "assigned_by" : tech_email,
                    
                })
                doc2.insert(ignore_permissions=True)
                notify_assignment(doc2.assigned_by, doc2.owner, doc2.reference_type, doc2.reference_name, action='ASSIGN',
				description=doc2.description)
                return ts_employee_user_id_name[0],ts_employee_user_id.full_name
            else:
                return 1

        

@frappe.whitelist()
def pending_requirement_finder(ts_user):
    pending_requirement=[]
    try:
        ts_last_doc=frappe.get_last_doc("TS Daily Requirement Sheet",{"owner":ts_user,"docstatus":1})
        if ts_last_doc:
            for requirement in ts_last_doc.__dict__["ts_requirement"]:
                if requirement:
                    if not requirement.__dict__["ts_task_assigned_by"]:
                        details=requirement.__dict__
                        pending_requirement.append([{"ts_subject":details["ts_subject"],
                                "ts_project":details["ts_project"],
                                "ts_department":details["ts_department"],
                                "ts_assigned_member":details["ts_assigned_member"],
                                "ts_assigned_member_name":details["ts_assigned_member_name"],
                                "ts_expected_start_date":details["ts_expected_start_date"],
                                "ts_expected_hours":details["ts_expected_hours"],
                                "ts_freezing_date":details["ts_freezing_date"],
                                "ts_planned_commitment_date":details["ts_planned_commitment_date"],
                                "ts_priority":details["ts_priority"],
                                "ts_requriement":details["ts_requriement"],
                                "ts_assigned_crm_member":details["ts_assigned_crm_member"],
                                "ts_assigned_crm_name":details["ts_assigned_crm_name"]}])
                        return pending_requirement
    except:
        pass
