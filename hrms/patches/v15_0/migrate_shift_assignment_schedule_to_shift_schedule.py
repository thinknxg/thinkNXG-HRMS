import frappe

from hrms.hr.doctype.shift_schedule.shift_schedule import get_or_insert_shift_schedule


def execute():
	frappe.reload_doc("HR", "doctype", "Shift Assignment")

	for doc in frappe.get_all("Shift Assignment Schedule", pluck="name"):
		doc = frappe.get_doc("Shift Assignment Schedule", doc)
		repeat_on_days = [d.day for d in doc.repeat_on_days]
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

		for d in frappe.get_all("Shift Assignment", filters={"schedule": doc.name}, pluck="name"):
			frappe.db.set_value("Shift Assignment", d, "shift_schedule_assignment", schedule_assignment.name)
