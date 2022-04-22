# Copyright (c) 2022, ThirvuSoft Private Limited and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
from typing import List
from webbrowser import get
from frappe import  _
import frappe

def execute(filters=None):
    data = get(filters)
    columns = get_columns(filters)
    return columns, data

def get(filters):
	final_list = []
	filter = {}
	if filters:
		if 'project' in (filters.keys()):
			filter['parent']= filters['project']
		if 'ci' in (filters.keys()):
			filter["assigned_ci"] = eval("['in',['"+str(filters['ci'])+"']]")
		if 'phase' in filters.keys():
			filter['phase'] = eval("[ 'in' ,['"+ str(filters['phase'])+"']]")
		if 'phase_status' in filters.keys():
			filter['status'] = eval("[ 'in' ,['"+ str(filters['phase_status'])+"']]")
		project_list = (frappe.get_all("TS Project Phase",fields =["parent"],filters = filter,pluck='parent'))
		project_list = list(set(project_list))
		if(len(project_list) == 0):
			frappe.throw("Mention the Phase Details in {0}".format(filters['project']))
		for project in project_list[::-1]:
			project_wise = frappe.get_doc("Project",project)
			if(len(project_wise.phases_)== 0):
				frappe.throw("Mention the Phase Details in {0}".format(project_wise.name))
			else:
				for tabphase in project_wise.phases_:
					final_dict = {}
					final_dict['project'] = project	
					final_dict['client'] = project_wise.customer
					final_dict['project_status'] = project_wise.status
					final_dict['phase'] = tabphase.phase
					final_dict['ci'] = tabphase.assigned_ci
					final_dict['start_date'] = tabphase.start_date
					final_dict['end_date'] = tabphase.end_date
					final_dict['phase_status'] = tabphase.status
					final_dict['total_issues_raised'] = project_wise.total_issues_raised
					hrs_list = []
					total_expected = 0
					total_actual = 0
					project_on_list = ["Development","Implementation","Full-flow Testing","Demo","Development Testing","Bug Fixing","Full-flow Checking"]
					for lis in project_on_list:
						task = frappe.get_all("Task",fields = ["expected_time","actual_time_taken_in_hours"],filters = {"project":project, "phase":tabphase.phase,"project_on": lis})
						expected = 0
						actual = 0
						for time in task:
							expected += time["expected_time"]
							actual += time["actual_time_taken_in_hours"]
						total_expected += expected
						total_actual += actual
						hrs_list.append(str(actual) + " / " + str(expected))
					final_dict['total_development_hours'] = hrs_list[0]
					final_dict['total_implementation_hours'] = hrs_list[1]
					final_dict['total_fullflow_testing_hours'] = hrs_list[2]
					final_dict['total_demo_hours'] = hrs_list[3]
					final_dict['total_development_testing_hours'] = hrs_list[4]
					final_dict['total_bug_fixing_hours'] = hrs_list[5]
					final_dict['total_fullflow_checking_hours'] = hrs_list[6]
					final_dict['total_expected_hours'] = total_expected
					final_dict['total_actual_hours'] = total_actual
					final_dict['total_exceeded_hours'] = total_actual - total_expected
					filt_keys = filters.keys()
					flag = True
					for i in filt_keys:
						if(final_dict[i] == filters[i]):
							pass
						else:
							flag = False
							break
					if flag == True:
						final_list.append(final_dict)
		return (final_list[::-1])
		
	else:
		project_list = frappe.get_list("Project",pluck='name')
		for project in project_list[::-1]:
			project_wise = frappe.get_doc("Project",project)
			if(len(project_wise.phases_)== 0):
				frappe.throw("Mention the Phase Details in {0}".format(project_wise.name))
			else:
				for tabphase in project_wise.phases_:
					final_dict = {}
					final_dict['project'] = project
					final_dict['client'] = project_wise.customer
					final_dict['project_status'] = project_wise.status
					final_dict['phase'] = tabphase.phase
					final_dict['ci'] = tabphase.assigned_ci
					final_dict['start_date'] = tabphase.start_date
					final_dict['end_date'] = tabphase.end_date
					final_dict['phase_status'] = tabphase.status
					final_dict['total_issues_raised'] = project_wise.total_issues_raised
					hrs_list = []
					total_expected = 0
					total_actual = 0
					project_on_list = ["Development","Implementation","Full-flow Testing","Demo","Development Testing","Bug Fixing","Full-flow Checking"]
					for lis in project_on_list:
						task = frappe.get_all("Task",fields = ["expected_time","actual_time_taken_in_hours"],filters = {"project":project, "phase":tabphase.phase,"project_on": lis})
						expected = 0
						actual = 0
						for time in task:
							expected += time["expected_time"]
							actual += time["actual_time_taken_in_hours"]
						total_expected += expected
						total_actual += actual
						hrs_list.append(str(actual) + " / " + str(expected))
					final_dict['total_development_hours'] = hrs_list[0]
					final_dict['total_implementation_hours'] = hrs_list[1]
					final_dict['total_fullflow_testing_hours'] = hrs_list[2]
					final_dict['total_demo_hours'] = hrs_list[3]
					final_dict['total_development_testing_hours'] = hrs_list[4]
					final_dict['total_bug_fixing_hours'] = hrs_list[5]
					final_dict['total_fullflow_checking_hours'] = hrs_list[6]
					final_dict['total_expected_hours'] = total_expected
					final_dict['total_actual_hours'] = total_actual
					final_dict['total_exceeded_hours'] = total_actual - total_expected
					final_list.append(final_dict)
	return (final_list)
			
def get_columns(filters):
	columns = [
		_("Project")+":Link/Project:100",
		_("Client")+":Data:150",
		_("Project Status")+":Data:150",
		_("Phase")+":Int:100",
		_("CI")+":Data:200",
		_("Start Date")+":Data:100",
		_("End Date")+":Date:100",
		_("Phase Status")+":Data:100",
		_("Total Issues Raised")+":Int:150",
		_("Total Development Hours")+":Data:200",
		_("Total Implementation Hours")+":Data:200",
		_("Total Fullflow Testing Hours")+":Data:200",
		_("Total Demo Hours")+":Data:200",
		_("Total Development Testing Hours")+":Data:200",
		_("Total Bug Fixing Hours")+":Data:200",
		_("Total Fullflow Checking Hours")+":Data:200",
		_("Total Expected Hours")+":Data:200",
		_("Total Actual Hours")+":Data:200",
		_("Total Exceeded Hours")+":Data:200",
	]
	return columns