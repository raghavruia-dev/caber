// Copyright (c) 2025, Raghav Ruia and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
	refresh(frm) {
        
        let order_status = frm.doc.status;

        if (order_status == "New") {
            frm.add_custom_button("Accept", () => {
                frm.set_value("status", "Accepted");
                frm.save();
            }, "Actions");

            frm.add_custom_button("Reject", () => {
                frm.set_value("status", "Rejected");
                frm.save();
            }, "Actions")
        }

        if (order_status == "Rejected") {
            frm.add_custom_button("Accept", () => {
                frm.set_value("status", "Accepted");
                frm.save();
            }, "Actions");

        }

        if (order_status == "Accepted") {
            frm.add_custom_button("Reject", () => {
                frm.set_value("status", "Rejected");
                frm.save();
            }, "Actions")
        }


        // if (order_status !== "Accepted") {
        //     frm.add_custom_button("Accept", () => {
        //     frm.set_value("status", "Accepted");
        //     frm.save();
        //     }, "Actions");

        // frm.add_custom_button("Reject", () => {
        //     frm.set_value("status", "Rejected");
        //     frm.save();
        //     }, "Actions");
        // }
	}
});
