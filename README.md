### Airplane Mode

A hypothetical flight ticket system
#  Flight Ticket System – Frappe Learning App

Welcome to the **Flight Ticket System**, a learning-based project designed to help  understand how to model real-world business workflows using the **Frappe Framework** (the foundation of ERPNext). 

This app walks  through modeling a simple flight ticketing process while introducing powerful Frappe concepts along the way.

---

## What I Learnt

- How to create and configure **DocTypes**
- Custom field validation and controller logic
- Naming rules and dynamic document titles
- Document hooks (e.g., validation, before insert, on submit)
- Child Tables and linking documents
- Writing Python code to manage business logic

---

##  Features Modeled

- **Airline** and **Airplane** registration
- Booking an **Airplane Ticket** with flight details
- Automatic seat assignment (e.g., `89E`)
- Preventing duplicate add-ons
- Calculating ticket total from base flight price and add-ons
- Preventing ticket submission unless status is "Boarded"
- Auto-updating the related flight status on submission

---

##  DocTypes Included

- `Airline`
- `Airplane`
- `Airplane Ticket`
- `Flight Passenger`
- `Add-ons` (child table)

---

## Requirements

- [Frappe Framework](https://frappeframework.com) ≥ v14.x
- Python 3.10+
- Node.js & Redis (for background jobs and bench dev server)
- MariaDB / PostgreSQL (as per your Frappe setup)

---

## 📂 Installation

1. Clone this repository inside your Frappe bench's `apps` directory:

   ```bash
   cd ~/frappe-bench/apps
   git clone https://github.com/yourusername/flight-ticket-system.git


### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app airplane_mode
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/airplane_mode
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
