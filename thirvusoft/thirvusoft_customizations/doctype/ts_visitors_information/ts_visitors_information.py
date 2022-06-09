# Copyright (c) 2021, ThirvuSoft Private Limited and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
import re

class TSVisitorsInformation(Document):
	def validate(self):
		if(self.outtime != "00:00:00"):
			duration = datetime.strptime(self.outtime, '%H:%M:%S') - datetime.strptime(self.intime, '%H:%M:%S')
			self.duration = str(duration)
		else:
			pass
		pattern = re.compile("(0|91)?[6-9][0-9]{9}")
		if(pattern.match(self.contact)):
			pass
		else:
			frappe.throw("Enter a valid contact number")
		if(self.email != None):
			if re.match(r"^[a-z0-9\.\+_-]+@[a-z0-9\._-]+\.[a-z]*$", self.email):
				pass
			else:
				frappe.throw("Enter a valid Email ID")