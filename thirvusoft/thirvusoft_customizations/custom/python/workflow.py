import frappe

def compensation_workflow():
    states=[]
    transition=[]
    ts_transitions=[['Draft', 'Draft'], ['Approve', 'Reject'], ['Approved by HR Manager', 'Rejected by HR Manager'], ['HR Manager', 'HR Manager']]
    ts_state=[['Draft', 'Rejected by HR Manager', 'Approved by HR Manager'],['0', '0', '1'], ['workflow_state', 'workflow_state', 'workflow_state'],['Draft', 'Rejected by HR Manager', 'Approved by HR Manager'], ['All', 'HR Manager', 'HR Manager']]
    for i in list(zip(*ts_state)):
        states.append({
            'state': i[0],
            'doc_status':i[1],
            'update_field':i[2],
            'update_value':i[3],
            'allow_edit':i[4]
        })
     
    for i in list(zip(*ts_transitions)):
        transition.append({
            'state':i[0],
            'action':i[1],
            'next_state':i[2],
            'allowed':i[3],

        })    
    doc = frappe.new_doc("Workflow")
    doc.update({
        'workflow_name':"Compensation Workflow",
        'document_type':"TS Compensation Request",
        'is_active':1, 
        'states':states,
        'transitions':transition,
    })   
    doc.insert(ignore_permissions=True)