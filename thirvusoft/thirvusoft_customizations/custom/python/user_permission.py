import frappe


def customer_permission(doc, event): 
    check=True
    if(event=="before_save"): 
        check_list=frappe.get_all("Customer", pluck='name')
        if(doc.name not in check_list): 
            check=False
    if(doc.user_id and check): 
        doc_list=frappe.get_all('User Permission', {'allow': "Customer", "user": doc.user_id}, pluck="name")
        if(doc_list): 
            user_per=frappe.get_doc("User Permission", doc_list[0])
            user_per.update({
                "for_value": doc.name
            })
            user_per.save()
        else: 
            doc1=frappe.new_doc('User Permission')
            doc1.update({
                'user': doc.user_id, 
                'allow': "Customer", 
                "for_value": doc.name, 
                "apply_to_all_doctypes": 1
            })
            doc1.insert()
        doc_list1=frappe.get_all('User Permission', {'allow': "Lead", "user": doc.user_id}, pluck="name")
        if(doc_list1): 
            pass
        else: 
            doc1=frappe.new_doc('User Permission')
            doc1.update({
                'user': doc.user_id, 
                'allow': "Lead", 
                "for_value": "", 
                "apply_to_all_doctypes": 1
            })
            doc1.insert(ignore_mandatory=True)

            
def lead_permission(doc, event): 
    check=True
    if(event=="before_save"): 
        check_list=frappe.get_all("Lead", pluck='name')
        if(doc.name not in check_list): 
            check=False
    if(doc.user_id and check): 
        doc_list=frappe.get_all('User Permission', {'allow': "Customer", "user": doc.user_id}, pluck="name")
        if(doc_list): 
            user_per=frappe.get_doc("User Permission", doc_list[0])
            user_per.update({
                "for_value": ""
            })
            user_per.flags.ignore_mandatory=True
            user_per.save()
        else: 
            doc1=frappe.new_doc('User Permission')
            doc1.update({
                'user': doc.user_id, 
                'allow': "Customer", 
                "for_value": "", 
                "apply_to_all_doctypes": 1
            })
            doc1.insert(ignore_mandatory=True)
        doc_list1=frappe.get_all('User Permission', {'allow': "Lead", "user": doc.user_id}, pluck="name")
        if(doc_list1): 
            user_per=frappe.get_doc("User Permission", doc_list1[0])
            user_per.update({
                "for_value": doc.name
            })
            user_per.save()
        else: 
            doc1=frappe.new_doc('User Permission')
            doc1.update({
                'user': doc.user_id, 
                'allow': "Lead", 
                "for_value": doc.name, 
                "apply_to_all_doctypes": 1
            })
            doc1.insert()
    frappe.db.commit()
