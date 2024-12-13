import frappe
from frappe.utils import unique

from hrms.hr.doctype.shift_schedule.shift_schedule import get_or_insert_shift_schedule


def execute():
	frappe.reload_doc("HR", "doctype", "Shift Assignment")

	fields = ["shift_type", "frequency", "employee", "shift_status", "enabled", "create_shifts_after"]

	for doc_name in frappe.get_all("Shift Assignment Schedule", pluck="name"):
		doc = frappe.db.get_value("Shift Assignment Schedule", doc_name, fields, as_dict=True)
		repeat_on_days = unique(frappe.get_all("Assignment Rule Day", {"parent": doc_name}, pluck="day"))
		shift_schedule_name = get_or_insert_shift_schedule(doc.shift_type, doc.frequency, repeat_on_days)

		schedule_assignment = frappe.get_doc(
			{
				"doctype": "Shift Schedule Assignment",
				"shift_schedule": shift_schedule_name,
				"employee": doc.employee,
				"shift_status": doc.shift_status,
				"enabled": doc.enabled,
				"create_shifts_after": doc.create_shifts_after,
			}
		).insert()

		for d in frappe.get_all("Shift Assignment", filters={"schedule": doc_name}, pluck="name"):
			frappe.db.set_value("Shift Assignment", d, "shift_schedule_assignment", schedule_assignment.name)
