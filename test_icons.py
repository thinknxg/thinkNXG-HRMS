import frappe

def execute():
	icons = frappe.db.get_all("Desktop Icon", fields=["name", "label", "app", "link", "icon_type", "hidden", "standard"])
	for i in icons:
		print(i)
