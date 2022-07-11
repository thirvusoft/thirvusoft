from . import __version__ as app_version

app_name = "thirvusoft"
app_title = "ThirvuSoft Customizations"
app_publisher = "ThirvuSoft Private Limited"
app_description = "ThirvuSoft Customizations"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "vignesh@thirvusoft.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/thirvusoft/css/thirvusoft.css"
# app_include_js = "/assets/thirvusoft/js/thirvusoft.js"

# include js, css files in header of web template
# web_include_css = "/assets/thirvusoft/css/thirvusoft.css"
# web_include_js = "/assets/thirvusoft/js/thirvusoft.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "thirvusoft/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {	"Task" : "thirvusoft_customizations/custom/js/task.js",
				"Salary Slip" : "thirvusoft_customizations/custom/js/salaryslip_expense_details.js",
				"Project":"thirvusoft_customizations/custom/js/project.js",
				"Leave Application":"thirvusoft_customizations/custom/js/leave_application.js",
				"Lead":"thirvusoft_customizations/custom/js/lead.js"
			}
doctype_list_js = {"Interview" : "thirvusoft_customizations/custom/js/interview.js"}

# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "thirvusoft.install.before_install"
# after_install = "thirvusoft.install.after_install"
# after_install= {"thirvusoft.thirvusoft_customizations.custom.python.property_setter.property_creator"}
after_install = ["thirvusoft.thirvusoft_customizations.custom.python.install.after_install",
                 "thirvusoft.thirvusoft_customizations.custom.python.property_setter.property_creator_task",
                 "thirvusoft.thirvusoft_customizations.custom.python.property_setter.property_creator_issue",
                 "thirvusoft.thirvusoft_customizations.custom.python.daily_requirement_workflow.workflow_document_creation",
                 "thirvusoft.thirvusoft_customizations.utils.after_install.after_install"]
# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "thirvusoft.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

doc_events = {
    "Job Applicant": {
        "validate": "thirvusoft.thirvusoft_customizations.custom.python.Job_Application.validation",
    },
    "Issue": {
        "validate": "thirvusoft.thirvusoft_customizations.custom.python.issue.validate_phone"
    },
    "Customer": {
        'after_insert': "thirvusoft.thirvusoft_customizations.custom.python.user_permission.customer_permission",
        'before_save': "thirvusoft.thirvusoft_customizations.custom.python.user_permission.customer_permission"
    },
    "Lead": {
        'after_insert': 'thirvusoft.thirvusoft_customizations.custom.python.user_permission.lead_permission',
        'before_save': 'thirvusoft.thirvusoft_customizations.custom.python.user_permission.lead_permission',
        'validate': "thirvusoft.thirvusoft_customizations.custom.python.lead.connect_contact"
    }
}
# "Issue": {
# 	"validate": "thirvusoft.thirvusoft_customizations.custom.python.Job_Application.issues_raised",
# 	"after_insert": "thirvusoft.thirvusoft_customizations.custom.python.Job_Application.create_task",
# }
override_doctype_class = {
    "Salary Slip": "thirvusoft.thirvusoft_customizations.custom.python.salaryslip_expense_details.SalarySlip",
    "Leave Application": "thirvusoft.thirvusoft_customizations.custom.python.leave_application.status_change"
}

# Document Events
# ---------------
# Hook on document methods and events
# Scheduled Tasks
# ---------------

scheduler_events = {
	"cron": {
		"0 9,12,16 * * *": [
					"thirvusoft.thirvusoft_customizations.custom.python.lead_notification.lead_notification",
				],
	}
	# "daily": [
	# 	"thirvusoft.tasks.daily"
	# ],
	# "hourly": [
	# 	"thirvusoft.tasks.hourly"
	# ],
	# "weekly": [
	# 	"thirvusoft.tasks.weekly"
	# ]
	# "monthly": [
	# 	"thirvusoft.tasks.monthly"
	# ]
}

# Testing
# -------

# before_tests = "thirvusoft.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "thirvusoft.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "thirvusoft.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"thirvusoft.auth.validate"
# ]
