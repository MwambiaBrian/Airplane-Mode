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
        self.calculate_total_amount()

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
