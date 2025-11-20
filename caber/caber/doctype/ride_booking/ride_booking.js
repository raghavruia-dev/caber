// Copyright (c) 2025, Raghav Ruia and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
	refresh(frm) {

	},
	rate(frm) {
		frm.trigger("update_total_amount");
	},

	update_total_amount(frm) {
		let total_distance = 0;
		for (let item of frm.doc.items) {
			total_distance += item.distance;
		}

		const total_amount = total_distance * frm.doc.rate;

		frm.set_value("total_amount", total_amount);
		frm.set_value("total_distance_travelled", total_distance);
	}
});

frappe.ui.form.on("Ride Booking Item", {
	distance(frm) {
		frm.trigger("update_total_amount");
	},
	items_remove(frm) {
		frm.trigger("update_total_amount");
	}
});


// frappe.model.set_value(cdt, cdn, "source", "Source is updated")
// Dialog API