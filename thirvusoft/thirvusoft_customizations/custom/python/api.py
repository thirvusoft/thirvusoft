# Whatsapp Integration

#Send Invoice

import http.client
import json
import frappe

@frappe.whitelist()
def send_report(project, file_url, file_name):
    customer=frappe.get_value('Project', project, 'customer')
    if(customer):
        contacts=frappe.get_all('Dynamic Link',{'link_name':customer},pluck='parent')
        cus_contact=frappe.get_all('Contact', {'name': ['in', contacts], 'is_primary_contact':1},pluck='mobile_no')
        if(not cus_contact):
            frappe.throw(f"No Primary mobile number for the customer {customer}")
        send_list=[]
        for mobile_no in cus_contact:
            if(mobile_no):
                conn = http.client.HTTPSConnection("api.interakt.ai")
                payload = json.dumps({
                "countryCode": "+91",
                "phoneNumber": mobile_no,
                "callbackData": "Thirvusoft",
                "type": "Template",
                "template": {
                "name": "test",
                "languageCode": "en",
                "headerValues": [ file_url ],
                "fileName": file_name or None,
                
                "bodyValues": [
                    "Thirvusoft"
                    ]
                    },
                })
                headers = {
                'Authorization': "Basic eHd0aHJaNUp6NjFvZF9qTFYwaml2YV9uSGdIbVR5ZFpad1JtYkREeng5czo=",
                'Content-Type': 'application/json',
                'Cookie': 'ApplicationGatewayAffinity=a8f6ae06c0b3046487ae2c0ab287e175; ApplicationGatewayAffinityCORS=a8f6ae06c0b3046487ae2c0ab287e175'
                    }
                conn.request("POST", "/v1/public/message/", payload, headers)
                res = conn.getresponse()
                data = res.read()
                send_list.append(mobile_no)
        frappe.msgprint("Message sent to "+", ".join(send_list) )
