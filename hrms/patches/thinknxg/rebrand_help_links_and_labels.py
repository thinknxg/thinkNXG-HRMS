# Copyright (c) 2026, thinkNXG and contributors
# For license information, please see license.txt

"""Carry thinkNXG HR branding into existing sites.

The DocType, Report, Onboarding and Desktop Icon JSON files were rebranded
without bumping their `modified` timestamps (to keep upstream merges clean),
so `bench migrate` would not re-import them on sites that already have them.
This patch applies the same changes to the database. It only touches values
that still hold the original upstream text, so site-level edits are kept.
"""

import re

import frappe

OLD_DOCS = re.compile(r"https?://docs\.frappe\.io/hr(?:/[^\s\"'()\]<>]*)?")
NEW_DOCS = "https://docs.thinknxg.com/thinknxghr"
LIKE_OLD_DOCS = "%docs.frappe.io/hr%"
OLD_LOGO = "/assets/hrms/images/frappe-hr-logo.svg"
NEW_LOGO = "/assets/hrms/images/thinkNXG-logo.jpg"


def execute():
	update_field("DocType", "documentation", {"module": ("in", get_hrms_modules())})
	update_field("Report", "documentation_url", {"module": ("in", get_hrms_modules())})
	update_field("Onboarding Step", "description", {})

	if frappe.db.exists("Module Onboarding", "HR Onboarding"):
		if frappe.db.get_value("Module Onboarding", "HR Onboarding", "title") == "Get to know Frappe HR":
			frappe.db.set_value(
				"Module Onboarding",
				"HR Onboarding",
				"title",
				"Get to know thinkNXG HR",
				update_modified=False,
			)

	# set_app_logo() stored the upstream logo path on sites installed before the rebrand
	if frappe.db.get_single_value("Navbar Settings", "app_logo") == OLD_LOGO:
		frappe.db.set_single_value("Navbar Settings", "app_logo", NEW_LOGO)

	if frappe.db.table_exists("Desktop Icon") and frappe.db.has_column("Desktop Icon", "label"):
		frappe.db.set_value(
			"Desktop Icon",
			{"app": "hrms", "label": ("in", ["Frappe HR", "thinknxg HR"])},
			"label",
			"thinkNXG HR",
			update_modified=False,
		)


def get_hrms_modules():
	return frappe.get_all("Module Def", filters={"app_name": "hrms"}, pluck="name") or [""]


def update_field(doctype, fieldname, filters):
	if not frappe.db.has_column(doctype, fieldname):
		return

	filters = dict(filters)
	filters[fieldname] = ("like", LIKE_OLD_DOCS)
	for row in frappe.get_all(doctype, filters=filters, fields=["name", fieldname]):
		new_value = OLD_DOCS.sub(NEW_DOCS, row.get(fieldname) or "")
		if new_value != row.get(fieldname):
			frappe.db.set_value(doctype, row.name, fieldname, new_value, update_modified=False)
