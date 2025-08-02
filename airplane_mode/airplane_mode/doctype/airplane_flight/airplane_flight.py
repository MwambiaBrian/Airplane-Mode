# Copyright (c) 2025, brian and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document

class AirplaneFlight(Document):
    def autoname(self):
        self.name = f"{self.source_airport_code}-{self.destination_airport_code}-{self.date_of_departure}"
    def validate(self):
        self.route = f"flights/{self.name.lower()}"

    def get_page_info(self):
        return {
        "title": self.name,
        "route": self.route,
        "published": self.is_published
    }

    def on_submit(self):
        self.status = "Completed"
