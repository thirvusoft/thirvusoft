from datetime import datetime
import frappe
from frappe.utils.user import get_user_fullname
from frappe.utils.data import pretty_date
from frappe.utils.data import (add_days, today)
 
def lead_notification(doc = None):
    for_user = frappe.get_all("Has Role",pluck="parent",filters={"role":"Client Project Manager"})
    if(doc):
        leads = [doc]
        user = get_user_fullname(frappe.db.get_value('Lead', doc, 'lead_owner'))
        message = f"New Lead Created {doc}.\n{doc} is created by {user}"
    else:
        leads = frappe.get_all("Lead",{'call_connected':0,'status':"Lead", 'creation':["<",add_days(today(), -1)]},pluck="name")
        message = ""
        if(not len(for_user)):frappe.msgprint("<b>No one</b> is assigned with the role <b>Client Project Manager</b> (to send System Notification).")
    args={
        'leads':leads,
        'message':message,
        'for_user':for_user
    }
    if(len(leads)):
        frappe.enqueue(method = send_notification, **args, queue = "long")
    
def send_notification(leads,message,for_user):
    message1=""
    for i in leads:
        from_user = frappe.db.get_value("Lead", i, 'lead_owner')
        for user in for_user:
            if(message == ""):message1 = get_message_for_uncontacted_leads(from_user,i)
            notification = frappe.new_doc("Notification Log")
            notification.update({
                "subject" : message+message1,
                "email_content" : message+message1,
                "document_type" : "Lead",
                "document_name" : i,
                "for_user" : user,
                "from_user" : from_user,
                "type" : "Alert"
            })
            notification.insert(ignore_permissions=True)
    frappe.db.commit()
def get_message_for_uncontacted_leads(from_user, lead):
    username = get_user_fullname(from_user)
    creation = pretty_date(frappe.db.get_value("Lead",lead,"creation"))
    message = f"Stil Lead {lead} is not contacted.\n{lead} was created by {username} {creation}"
    return message

@frappe.whitelist()
def delete_notification_log(doc, name):
    frappe.flags.ignore_permissions = True
    notif = frappe.db.get_all("Notification Log", {'document_type':doc, 'document_name':name}, pluck='name')
    if(len(notif)):
        if(len(notif) == 1):condition = f"where name = '{notif[0]}'"
        else:condition=f"where name in {tuple(notif)}"
        frappe.db.sql(f'''
                      DELETE FROM `tabNotification Log` {condition};
                      ''')
        return True
    return False


def next_contact_notification():
    leads = frappe.get_all("Lead", filters={'next_contact_date':today(), 'call_connected':0}, pluck = "name")
    for_user = frappe.get_all("Has Role",pluck="parent",filters={"role":"Client Project Manager"})
    args={
        'leads':leads,
        'for_user':for_user 
    }
    if(len(leads)):
        frappe.enqueue(method = send_next_contact_notification, **args, queue = "long")
    
    
def send_next_contact_notification(leads, for_user):
    for lead in leads:
        from_user = frappe.get_value("Lead", lead, 'lead_owner')
        next_contact_by =  frappe.get_value("Lead", lead, 'contact_by')
        msg=''
        if(next_contact_by):
            msg+=next_contact_by
            for_user = [next_contact_by]
            from_user = frappe.get_value("Lead", lead, 'modified_by')
            msg+=" from_user" + from_user
        for user in for_user:
            username = get_user_fullname(user)
            notification = frappe.new_doc("Notification Log")
            notification.update({
                    "subject" : f"Its time to contact {lead}. As {username} schedule next contact date as today.",
                    "email_content" : f"Its time to contact {lead}. As {username} schedule next contact date as today.",
                    "document_type" : "Lead",
                    "document_name" : lead,
                    "for_user" : user,
                    "from_user" : from_user,
                    "type" : "Alert",
                    "read" : 0
                })
            notification.insert(ignore_permissions=True)
            frappe.db.commit()