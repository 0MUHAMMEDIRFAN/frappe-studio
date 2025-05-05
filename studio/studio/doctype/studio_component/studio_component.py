# Copyright (c) 2025, Frappe Technologies Pvt Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class StudioComponent(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		blocks: DF.JSON | None
		component_name: DF.Data | None
		studio_app: DF.Link | None
	# end: auto-generated types
 
	def autoname(self):
		if not self.name:
			self.name = f"component-{frappe.generate_hash(length=8)}"

	pass
