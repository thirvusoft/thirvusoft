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
