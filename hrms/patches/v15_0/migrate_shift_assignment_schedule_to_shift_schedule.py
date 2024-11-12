import frappe


def execute():
	for shift_assignment_schedule in frappe.get_all("Shift Assignment Schedule", pluck="name"):
		shift_assignment_schedule = frappe.get_doc("Shift Assignment Schedule", shift_assignment_schedule)
		repeat_on_days = [d.day for d in shift_assignment_schedule.repeat_on_days]

		shift_schedules = frappe.get_all(
			"Shift Schedule",
			pluck="name",
			filters={
				"shift_type": shift_assignment_schedule.shift_type,
				"frequency": shift_assignment_schedule.frequency,
			},
		)

		shift_schedule_name = None
		for shift_schedule in shift_schedules:
			shift_schedule = frappe.get_doc("Shift Schedule", shift_schedule)
			shift_schedule_days = [d.day for d in shift_schedule.repeat_on_days]
			if sorted(repeat_on_days) == sorted(shift_schedule_days):
				shift_schedule_name = shift_schedule.name
				break

		if not shift_schedule_name:
			shift_schedule_name = (
				frappe.get_doc(
					{
						"doctype": "Shift Schedule",
						"shift_type": shift_assignment_schedule.shift_type,
						"frequency": shift_assignment_schedule.frequency,
						"repeat_on_days": [{"day": day} for day in repeat_on_days],
					}
				)
				.insert()
				.name
			)

		frappe.get_doc(
			{
				"doctype": "Shift Schedule Assignment",
				"shift_schedule": shift_schedule_name,
				"employee": shift_assignment_schedule.employee,
				"shift_status": shift_assignment_schedule.shift_status,
				"enabled": shift_assignment_schedule.enabled,
				"create_shifts_after": shift_assignment_schedule.create_shifts_after,
			}
		).insert()
