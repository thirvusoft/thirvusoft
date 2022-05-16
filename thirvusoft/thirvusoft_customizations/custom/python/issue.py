import frappe
import erpnext
from frappe import _
def validate_phone(doc,action):
   phone_number = doc.phone_number
   if phone_number:
       if not phone_number.isdigit() or len(phone_number) != 10:
           frappe.throw(frappe._("{0} is not a valid Phone Number.").format(phone_number), frappe.InvalidPhoneNumberError) 