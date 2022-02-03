import frappe
def after_insert(self,event):
    project=frappe.get_doc({
        'doctype':'TS Project Tracking',
        'project_name':self.project_name,
        'project_need':self.project_need,
        'existing_software':self.existing_software,
        'customer_name':self.customer_name,
        'expected_closing':self.expected_closing
    })
    project.insert()
    frappe.db.commit()
    frappe.msgprint(f"{project.project_name} has been created.")

