import frappe
import re
from datetime import datetime
from frappe import utils



def validation(self, phone):

    email=r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}';
    if(re.match(email,self.email_id)):
        pass
    else:
        frappe.throw("Please Enter correct email id")

    if(self.phone_number == '+91 '):
        pho = r"^[+][0-9]{2,3}[ ][6-9]{1}[0-9]{9}$";
        if(re.match(pho,self.phone_number)):
            pass
        else:
            frappe.throw("Please enter the correct phone Number")
    elif(self.phone_number == None):
        pass
    else:
        pho = r"^[6-9]{1}[0-9]{9}$";
        if(re.match(pho,self.phone_number)):
            pass
        else:
            frappe.throw("Please enter the correct phone Number")
    
    if(self.mobile_number == '+91 '):
        pho = r"^[+][0-9]{2,3}[ ][6-9]{1}[0-9]{9}$";
        if(re.match(pho,self.mobile_number)):
            pass
        else:
            frappe.throw("Please enter the correct mobile Number")
    elif(self.mobile_number == None):
        pass
    else:
        pho = r"^[6-9]{1}[0-9]{9}$";
        if(re.match(pho,self.mobile_number)):
            pass
        else:
            frappe.throw("Please enter the correct mobile Number")

    self.applicant_name = self.applicant_name.capitalize()
    self.address = self.address.capitalize()
    self.city = self.city.capitalize()
    self.state = self.state.capitalize()
    self.describe_your_skills = self.describe_your_skills.capitalize()
    self.parentguardian_name = self.parentguardian_name.capitalize()
    self.parentguardian_occupation = self.parentguardian_occupation.capitalize()
    self.how_they_are_related_to_you = self.how_they_are_related_to_you.capitalize()
    self.referral_employee = self.referral_employee.capitalize()
    self.job_portal = self.job_portal.capitalize()
    self.referral_contact = self.referral_contact.capitalize()
    self.cover_letter = self.cover_letter.capitalize()
    self.n = self.n.capitalize()