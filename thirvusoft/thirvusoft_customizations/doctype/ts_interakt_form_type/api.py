import http
import json
import frappe
from frappe.utils.password import get_decrypted_password


@frappe.whitelist()
def interaktsettings(api_endpoint,api_key,contact,template,url):
    conn = http.client.HTTPSConnection(api_endpoint)
    payload = json.dumps({
  "countryCode": "+91",
  "phoneNumber": contact,
  "callbackData": "some text here",
  "type": "Template",
  "template": {
    "name": template,
    "languageCode": "en",
    "bodyValues": [
      "body_variable_value_1",
      "body_variable_value_2"
    ],
    "buttonValues": {
      "1": [
        url
      ]
    }
  }
})
    headers = {  
  'Authorization': get_decrypted_password(doctype="Interakt Settings", name="Interakt Settings", fieldname="api_key",),
  'Content-Type': 'application/json'
}
    conn.request("POST", "/v1/public/message/", payload, headers)
    res = conn.getresponse()
    data = res.read()

def send_invoice(cus, name, doctype):

  link=frappe.get_value(doctype, name, 'print_link') or None
  if(link):
    link=frappe.utils.get_url()+link
    mb=frappe.get_doc("Contact",cus+'-'+cus)
    conn = http.client.HTTPSConnection("api.interakt.ai")
    payload = json.dumps({
    "countryCode": "+91",
    "phoneNumber": 9585350886,
    "callbackData": "some text here",
    "type": "Template",
    "template": {
      "name": "test",
      "languageCode": "en",
      "headerValues": [ "https://abouttmc.com/wp-content/uploads/2015/06/Beginners_guide_to_erp_v2.pdf" ],
      "fileName": "file.pdf",
      "bodyValues": [
        "Mani"
      ]
    }
  })
    headers = {
    'Authorization': "Basic eHd0aHJaNUp6NjFvZF9qTFYwaml2YV9uSGdIbVR5ZFpad1JtYkREeng5czo=",
    'Content-Type': 'application/json',
    'Cookie': 'ApplicationGatewayAffinity=a8f6ae06c0b3046487ae2c0ab287e175; ApplicationGatewayAffinityCORS=a8f6ae06c0b3046487ae2c0ab287e175'
  }
    conn.request("POST", "/v1/public/message/", payload, headers)
    res = conn.getresponse()
    data = res.read()