from erpnext.hr.doctype.leave_application.leave_application import LeaveApplication
import frappe
class status_change(LeaveApplication):
    def on_submit(self):
        if(self.hr_manager_approved == 1):
            if self.status in ["Approved by HR Manager"]:
                self.status = "Approved"
                self.validate_back_dated_application()
                self.update_attendance()
            if self.status in ["Rejected by HR Manager","Rejected by Tech Lead"]:
                self.status = "Cancelled"
        else:
            frappe.throw("Needs Approval from HR Manager")