app_name = "caber"
app_title = "Caber"
app_publisher = "Raghav Ruia"
app_description = "manage your driver & vehicles for your cab business."
app_email = "raghavruia.dev@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "caber",
# 		"logo": "/assets/caber/logo.png",
# 		"title": "Caber",
# 		"route": "/caber",
# 		"has_permission": "caber.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/caber/css/caber.css"
# app_include_js = "/assets/caber/js/caber.js"

# include js, css files in header of web template
# web_include_css = "/assets/caber/css/caber.css"
# web_include_js = "/assets/caber/js/caber.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "caber/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "caber/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "home"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "caber.utils.jinja_methods",
# 	"filters": "caber.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "caber.install.before_install"
# after_install = "caber.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "caber.uninstall.before_uninstall"
# after_uninstall = "caber.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "caber.utils.before_app_install"
# after_app_install = "caber.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "caber.utils.before_app_uninstall"
# after_app_uninstall = "caber.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "caber.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Vehicle": "caber.api.get_query_conditions_for_vehicle",
# }
# 
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"ToDo": {
# 		"before_insert": "caber.api.throw_emoji"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#     "cron": {
#         "30 15 * * 3": [
#             "caber.api.send_payment_reminders"
#         ]
#     }
# }

# scheduler_events = {
# 	"all": [
# 		"caber.tasks.all"
# 	],
# 	# 12 AM at night
# 	"daily": [
# 		"caber.tasks.daily"
# 	],
# 	"hourly": [
# 		"caber.tasks.hourly"
# 	],
# 	"weekly": [
# 		"caber.tasks.weekly"
# 	],
# 	"weekly_long": [
# 		"caber.tasks.weekly"
# 	],
# 	"monthly": [
# 		"caber.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "caber.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "caber.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "caber.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["caber.utils.before_request"]
# after_request = ["caber.utils.after_request"]

# Job Events
# ----------
# before_job = ["caber.utils.before_job"]
# after_job = ["caber.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"caber.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

