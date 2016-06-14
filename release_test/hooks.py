# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "release_test"
app_title = "Release Test"
app_publisher = "Revant"
app_description = "Release Test"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "revant@revant.me"
app_license = "GPL v3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/release_test/css/release_test.css"
# app_include_js = "/assets/release_test/js/release_test.js"

# include js, css files in header of web template
# web_include_css = "/assets/release_test/css/release_test.css"
# web_include_js = "/assets/release_test/js/release_test.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "release_test.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "release_test.install.before_install"
# after_install = "release_test.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "release_test.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"release_test.tasks.all"
# 	],
# 	"daily": [
# 		"release_test.tasks.daily"
# 	],
# 	"hourly": [
# 		"release_test.tasks.hourly"
# 	],
# 	"weekly": [
# 		"release_test.tasks.weekly"
# 	]
# 	"monthly": [
# 		"release_test.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "release_test.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "release_test.event.get_events"
# }

