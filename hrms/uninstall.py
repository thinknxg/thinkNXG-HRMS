import click

from hrms.setup import before_uninstall as remove_custom_fields


def before_uninstall():
	try:
		print("Removing customizations created by the thinkNXG HR app...")
		remove_custom_fields()

	except Exception as e:
		SUPPORT_URL = "https://thinknxg.com/thinkdesk"
		click.secho(
			"Removing Customizations for thinkNXG HR failed due to an error."
			" Please try again or"
			f" contact thinkNXG Support at {SUPPORT_URL} if not resolved.",
			fg="bright_red",
		)
		raise e

	click.secho("thinkNXG HR app customizations have been removed successfully...", fg="green")
