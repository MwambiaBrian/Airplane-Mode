# Copyright (c) 2025, brian and contributors
# For license information, please see license.txt
import random
import string
import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):
    def before_insert(self):
        # Generate a seat number in the format: <random-integer><random-letter A-E>
        number = random.randint(1, 99)
        letter = random.choice(['A', 'B', 'C', 'D', 'E'])
        self.seat = f"{number}{letter}"
    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("Cannot submit ticket unless the passenger has boarded.")
            
   
    def validate(self):
        self.remove_duplicate_add_ons()
        self.calculate_total_amount()        # Get the flight document
        flight = frappe.get_doc("Airplane Flight", self.flight)

        # Get the airplane document linked to the flight
        airplane = frappe.get_doc("Airplane", flight.airplane)
        capacity = airplane.capacity or 0

        # Count existing tickets for this flight (excluding the current one in case of update)
        booked_tickets = frappe.db.count(
            "Airplane Ticket",
            {
                "flight": self.flight,
                "docstatus": ("!=", 2),  # Exclude cancelled tickets
                "name": ("!=", self.name)  # Exclude this ticket if it's being updated
            }
        )

        if booked_tickets >= capacity:
            frappe.throw(_("This flight is fully booked. No more tickets can be issued."))

    def remove_duplicate_add_ons(self):
        seen = set()
        unique_add_ons = []

        for addon in self.add_ons:
            if addon.add_on not in seen:
                seen.add(addon.add_on)
                unique_add_ons.append(addon)

        # Clear and replace with unique entries
        self.add_ons = []
        for addon in unique_add_ons:
            self.append("add_ons", {
                "add_on": addon.add_on,
                "amount": addon.amount
            })

    def calculate_total_amount(self):
        total_addons = sum(addon.amount or 0 for addon in self.add_ons)
        self.total_amount = (self.flight_price or 0) + total_addons
