import frappe
import random
import string

def execute():
    tickets = frappe.get_all("Airplane Ticket", fields=["name", "passenger"])
    for ticket in tickets:
         # Generate a seat number in the format: <random-integer><random-letter A-E>
        number = random.randint(1, 99)
        letter = random.choice(['A', 'B', 'C', 'D', 'E'])
        seat = f"{number}{letter}"

        frappe.db.set_value("Airplane Ticket", ticket.name, "seat", seat)
