Details :<br>
Employee : {{doc.employee}} {{doc.employee_name}}<br>
Leave Type : {{doc.leave_type}}<br>
From Date : {{doc.from_date}}<br>
To Date : {{doc.to_date}}<br>
Reason for rejection :{{doc.reason_for_rejected}}<br>
<a href="{{frappe.utils.get_url_to_form(doc.doctype, doc.name)}}">{{doc.name}}</a>