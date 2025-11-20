# Copyright (c) 2025, Raghav Ruia and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(self): 
		if not self.rate:
			self.rate = frappe.db.get_single_value("Caber Settings", "standard_rate")
			frappe.msgprint("No rate specified. Using standard rate from Caber Settings.")

		totalDistanceTravelled = 0

		# add all the distance (from the line items)
		for item in self.items:
			totalDistanceTravelled += item.distance

		self.total_distance_travelled = totalDistanceTravelled
		self.total_amount = self.rate * totalDistanceTravelled
