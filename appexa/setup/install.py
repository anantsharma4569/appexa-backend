"""Runs when the app is installed on a site.

Frappe Cloud gives no bench CLI on shared plans, so the starter content cannot
be seeded by hand after an install. Seeding here means a fresh site comes up
with a working website instead of thirteen empty doctypes.

seed_all only inserts what is missing, so reinstalling or migrating an existing
site leaves edited records alone.
"""

import frappe

from appexa.setup.seed import seed_all


def after_install():
	try:
		seed_all()
	except Exception:
		# A failure here would roll back the whole install, which is a much
		# worse outcome than a site that starts empty and gets seeded later.
		frappe.log_error(title="Appexa: seeding the starter content failed")
		print("Appexa: could not seed the starter content; the app is installed regardless.")
