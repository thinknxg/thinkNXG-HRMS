import click

from hrms.setup import after_install as setup


def after_install():
	try:
		print("Setting up thinkNXG HR...")
		setup()

		click.secho("Thank you for installing thinkNXG HR!", fg="green")

	except Exception as e:
		SUPPORT_URL = "https://thinknxg.com/thinkdesk"
		click.secho(
			"Installation for thinkNXG HR app failed due to an error."
			" Please try re-installing the app or"
			f" contact thinkNXG Support at {SUPPORT_URL} if not resolved.",
			fg="bright_red",
		)
		raise e
