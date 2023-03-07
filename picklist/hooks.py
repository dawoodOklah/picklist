from . import __version__ as app_version

app_name = "picklist"
app_title = "Picklist"
app_publisher = "mismail@anvilerp.com"
app_description = "Pick list"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "mismail@anvilerp.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/picklist/css/picklist.css"
app_include_css = "/assets/picklist/css/custom.css"
# app_include_js = "/assets/picklist/js/picklist.js"

# include js, css files in header of web template
# web_include_css = "/assets/picklist/css/picklist.css"
# web_include_js = "/assets/picklist/js/picklist.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "picklist/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
	"Pick List": "public/js/pick_list.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
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

# before_install = "picklist.install.before_install"
# after_install = "picklist.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "picklist.uninstall.before_uninstall"
# after_uninstall = "picklist.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "picklist.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }
doc_events = {
	"Pick List": {
		"on_submit": "picklist.api.update_so_status"
	},
	"Sales Order": {
		"validate": "picklist.api.check_barcodes"
	}
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"picklist.tasks.all"
#	],
#	"daily": [
#		"picklist.tasks.daily"
#	],
#	"hourly": [
#		"picklist.tasks.hourly"
#	],
#	"weekly": [
#		"picklist.tasks.weekly"
#	]
#	"monthly": [
#		"picklist.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "picklist.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "picklist.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "picklist.task.get_dashboard_data"
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
#	"picklist.auth.validate"
# ]



fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Pick List-sales_order_barcode",
                    "Pick List-sales_order",
                    "Pick List-total_pick_qty",
                    "Pick List-total_actual_qty",
                    "Pick List-qty",
                    "Pick List-item_barcode",
                    "Pick List-item",
                    "Pick List-order_status",
                    "Pick List-progress",

                    "Sales Order-doc_barcode",
                    "Sales Order Item-item_barcode",
                    "Sales Order Item-barcode"
                ]
            ]
        ]
    },
    {
        "dt": "Property Setter",
        "filters": [
            [
                "name",
                "in",
                [
                    "Sales Order-status-options"
                ]
            ]
        ]
    },
    {
        "dt": "Print Format",
        "filters": [
            [
                "name",
                "in",
                [
                    "Print Format With Barcode"
                ]
            ]
        ]
    }
]