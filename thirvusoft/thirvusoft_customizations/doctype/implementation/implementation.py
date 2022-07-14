# Copyright (c) 2022, ThirvuSoft Private Limited and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Implementation(Document):
	def on_submit(self):
		for row in self.implementation_sheet:
			doc = frappe.get_doc("Project",row.project)
			for data in doc.estimation_details:
				if data.task_type=="Implementation" :
					data.total_hours_taken += row.hours_spend
				else:
					data.task_type = "Implementation"
					data.total_hours_taken = row.hours_spend
			doc.save()
	def on_cancel(self):
		for row in self.implementation_sheet:
			doc = frappe.get_doc("Project",row.project)
			for hours in doc.estimation_details:
				if hours.task_type=="Implementation" :
					hours.total_hours_taken -= row.hours_spend
			doc.save()


