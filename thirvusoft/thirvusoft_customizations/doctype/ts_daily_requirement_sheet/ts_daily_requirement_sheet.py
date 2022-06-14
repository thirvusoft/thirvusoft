# Copyright (c) 2022, ThirvuSoft Private Limited and contributors
# For license information, please see license.txt
 
from datetime import datetime

from frappe.model.document import Document
from frappe.desk.form import assign_to
  
import frappe
class TSDailyRequirementSheet(Document):
   def validate(doc):
        doc.deadline_time = frappe.get_value("TS Time","8d2b6eb21d", "deadline_time")
        finaltime = str(doc.deadline_time)
        time=':'.join([('0'*(2-len(t)))+t for t in finaltime.split(':')])
        now =datetime.now()
        current_time=now.strftime("%H:%M:%S")
        if current_time > time:
            doc.timing=1
        else:
            doc.timing=0

@frappe.whitelist()
def tech_lead_name_finder(ts_user,ts_value):
    ts_employee_user=frappe.db.get_values("Employee",filters={"user_id":ts_user},fieldname=["name",'employee_name',"designation"])
    if(ts_employee_user):
        ts_employee_user=ts_employee_user[0]
        ts_employee_user_id=ts_employee_user[0]
        ts_employee_user_name=ts_employee_user[1]
        ts_employee_user_name_designation=ts_employee_user[2]
        if(ts_value=="0"):
            if(ts_employee_user_name_designation=="Tech Lead"):
                return ts_employee_user_id,ts_employee_user_name
            else:
                return 1
        else:
            return ts_employee_user_id

 
 
from frappe.utils import getdate
from datetime import timedelta
@frappe.whitelist()
def employee_role(ts_user,ts_data):
   ts_data=eval(ts_data)
   ts_employee_user_id=frappe.db.get_values("Employee",filters={"user_id":ts_user},fieldname=["name",'employee_name',"designation"])
   if ts_employee_user_id:
        ts_employee_user_id=ts_employee_user_id[0]
        if(ts_employee_user_id[2]=="Tech Lead"):
            ts_user_details=frappe.db.get_values("User",filters={"role_profile_name":"Scurm Master"},fieldname=["name"])
            if ts_user_details:
                ts_user_details=ts_user_details[0]
                ts_scurm_user_details=frappe.db.get_values("Employee",filters={"user_id":ts_user_details[0]},fieldname=["name","employee_name"])
                ts_scurm_user_details=ts_scurm_user_details[0]
                ts_expected_start_date=getdate(ts_data["ts_expected_start_date"])
                ts_expected_end_date=ts_expected_start_date+timedelta(days=7)
                ts_new_task=frappe.get_doc({
                    "doctype":"Task",
                    "subject":ts_data["ts_subject"],
                    "project":ts_data["ts_project"],
                    "status":"Open",
                    "priority":ts_data["ts_priority"],
                    "assigned_tech_lead":ts_employee_user_id[0],
                    "assigned_ci":ts_data["ts_assigned_crm_member"],
                    "assigned_team_member":ts_data["ts_assigned_member"],
                    "ts_assigned_tech_lead_name":ts_employee_user_id[1],
                    "ts_assigned_ci_name":ts_data["ts_assigned_crm_name"],
                    "ts_assigned_team_member":ts_data["ts_assigned_member_name"],
                    "ts_scurm_master_id":ts_scurm_user_details[0],
                    "ts_scurm_master_name":ts_scurm_user_details[1],
                    "ts_scurm_master_mail":ts_user_details[0],
                    "exp_start_date":ts_data["ts_expected_start_date"],
                    "exp_end_date":ts_expected_end_date,
                    "expected_time":ts_data["ts_expected_hours"],
                    "description":ts_data["ts_requriement"],
                    "department":ts_data["ts_department"],
                })
                ts_new_task.insert()
                ts_new_task.save()
                employee = frappe.get_doc("Employee",ts_new_task.assigned_ci)
                ci_email = employee.user_id
                

                employee1= frappe.get_doc("Employee",ts_new_task.assigned_tech_lead)
                tech_email = employee1.user_id
                
                
                employee2= frappe.get_doc("Employee",ts_new_task.assigned_team_member)
                team_email = employee2.user_id
                
                doc=frappe.new_doc("ToDo")
                doc.update({
                    "owner" : team_email,
                    "description" :  team_email,
                    "reference_type" : "Task",
                    "reference_name" : ts_new_task.name,
                    "role" : "All",
                    "assigned_by" : tech_email,
                    
                })
                doc.insert(ignore_permissions=True)


                doc1=frappe.new_doc("ToDo")
                doc1.update({
                    "owner" : tech_email,
                    "description" : tech_email,
                    "reference_type" : "Task",
                    "reference_name" : ts_new_task.name,
                    "role" : "All",
                    "assigned_by" : tech_email,
                    
                })
                doc1.insert(ignore_permissions=True)
                

                doc2=frappe.new_doc("ToDo")
                doc2.update({
                    "owner" :  ci_email,
                    "description" : ci_email,
                    "reference_type" : "Task",
                    "reference_name" : ts_new_task.name,
                    "role" : "All",
                    "assigned_by" : tech_email,
                    
                })
                doc2.insert(ignore_permissions=True)
                return ts_employee_user_id[0],ts_employee_user_id[1]
            else:
              return 1

@frappe.whitelist()
def pending_requirement_finder(ts_user):
    pending_requirement=[]
    ts_last_doc=frappe.get_last_doc("TS Daily Requirement Sheet",{"owner":ts_user})
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
