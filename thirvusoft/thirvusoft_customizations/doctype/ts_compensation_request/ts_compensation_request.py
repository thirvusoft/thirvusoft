# Copyright (c) 2022, ThirvuSoft Private Limited and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TSCompensationRequest(Document):
    
    def validate(self):
       leavelist = []
       leavelist = frappe.db.get_list("Attendance", filters={"employee":self.employee,"attendance_date":self.leave_date,"status":"Absent"}, fields=["name"])
       if leavelist == []:
           frappe.throw("check the leave date")
       else:
           pass
   
       compensationlist = []
       compensationlist  = frappe.db.get_list("Attendance", filters={"employee":self.employee,"attendance_date":self.compensation_date,"status":"Present"}, fields=["name"])
       if  compensationlist  == []:
           frappe.throw("check the compensation date")
       else:
           pass
    def on_submit(self):
        leavelist = []
        
        leavelist = frappe.db.get_list("Attendance", filters={"employee":self.employee,"attendance_date":self.leave_date,"status":"Absent"}, fields=["name"])
        compensationlist = []
        compensationlist  = frappe.db.get_list("Attendance", filters={"employee":self.employee,"attendance_date":self.compensation_date,"status":"Present"}, fields=["name"])
        frappe.db.set_value(
			"Attendance", compensationlist[0],"status", "Absent"
		),
        frappe.db.set_value(
			"Attendance", leavelist [0],"status", "Present"
		),
        frappe.db.set_value(
			"Attendance", leavelist [0],"compensation_day", self.name
		),
        frappe.db.set_value(
			"Attendance", leavelist [0],"compensation", 1
		)
	   
	
