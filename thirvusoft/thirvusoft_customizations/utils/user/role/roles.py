import frappe
def create_role():
    role = frappe.new_doc("Role")
    if(not frappe.db.exists("Role", "Client Project Manager")):
        role.update({
            "role_name":"Client Project Manager",
            "disabled":0,
            "is_custom":0,
            "desk_access":1,
            "two_factor_auth":0,
            "search_bar":1,
            "notifications":1,
            "list_sidebar":1,
            "bulk_actions":1,
            "view_switcher":1,
            "form_sidebar":1,
            "timeline":1,
            "dashboard":1,      
        })
        role.insert(ignore_permissions=True)
    return