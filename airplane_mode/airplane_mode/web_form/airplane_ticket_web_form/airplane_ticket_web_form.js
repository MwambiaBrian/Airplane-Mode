frappe.web_form.after_load = () => {
	console.log("✅ Script loaded");

	const flight = frappe.utils.get_url_arg("flight");

	if (flight) {
		console.log("🌐 URL param 'flight':", flight);

		frappe.web_form.set_value("flight", flight);

		frappe.call({
			method: "frappe.client.get",
			args: {
				doctype: "Airplane Flight", // not "Airplane Ticket" here!
				name: flight,
			},
			callback: function (r) {
				if (r.message) {
					console.log("💰 Price fetched:", r.message.price);
					frappe.web_form.set_value("flight_price", r.message.price || 1000);
				}
			},
		});
	}
};
