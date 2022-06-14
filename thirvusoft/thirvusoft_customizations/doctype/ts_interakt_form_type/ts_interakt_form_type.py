# Copyright (c) 2022, ThirvuSoft Private Limited and contributors
# For license information, please see license.txt

from re import template
import frappe
import http.client
import json
from frappe.utils.password import get_decrypted_password
from frappe.model.document import Document
# from interakt.api import interaktsettings
class TSInteraktFormType(Document):
	pass

@frappe.whitelist()
def sendform(temp_name,data):
	api_key=frappe.db.get_single_value("Interakt Settings","api_key")
	api_endpoint=frappe.db.get_single_value("Interakt Settings","api_endpoint")
	temp_name=json.loads(temp_name)
	data=json.loads(data)
	frappe.errprint(temp_name)
	frappe.errprint(temp_name['name'])
	doc = frappe.get_doc({
	"doctype": "TS Interakt Form Type",
	"doctype_name": data['doctype'],
	"interakt_template": temp_name['name'],
	"dynamic_url": temp_name['url'],
	"api_key": api_key,
	"api_endpoint": api_endpoint,
	"contact_no": data['mobile_no']
	})
	doc.insert()
	conn = http.client.HTTPSConnection(doc.api_endpoint)
	payload = json.dumps({
  "countryCode": "+91",
  "phoneNumber": doc.contact_no,
  "callbackData": "some text here",
  "type": "Template",
  "template": {
    "name": doc.interakt_template,
    "languageCode": "en",
    "bodyValues": [
      "body_variable_value_1",
      "body_variable_value_2"
    ],
    "buttonValues": {
      "1": [
        doc.dynamic_url
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
	