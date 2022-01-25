#import frappe
#from frappe import _
#def val(self,latitude):
#    a=frappe.get_list("Customer", fields = ['latitude', 'longitude'])
#    b=frappe.get_list("Attendance",fields = ['latitude', 'longitude'])
#    frappe.throw(a)
#    if(b[0] == b[1]):
#        frappe.throw("corrct")
from erpnext.hr.doctype.attendance.attendance import Attendance
import frappe
from frappe import _
#from frappe.model.document import Document
#from frappe.utils import cstr, formatdate, get_datetime, getdate, nowdate

#from erpnext.hr.utils import validate_active_employee


class location(Attendance):
	def validate(self):
		self.validate_location()

	def validate_location(self):
        a=frappe.get_list("Customer", fields = ['latitude', 'longitude'])
        