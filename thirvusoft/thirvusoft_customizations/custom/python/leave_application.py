import frappe
from erpnext.hr.doctype.leave_application.leave_application import LeaveApplication

class status_change(LeaveApplication):
    def on_submit(self):
        if self.status in ["Open", "Cancelled"]:
            self.status = "Approved"
        self.validate_back_dated_application()
        self.update_attendance()