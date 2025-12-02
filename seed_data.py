from models import SessionLocal, Customer, FeeType
from datetime import date, timedelta
import random

def seed_database():
    session = SessionLocal()
    
    # 1. Seed Fee Types
    fee_types = [
        "Management Fee",
        "Placement Fee",
        "Renewal Fee",
        "Maintenance Markup",
        "Inspection Fee",
        "Late Fee",
        "Eviction Processing",
        "Utility Management"
    ]
    
    for fee_name in fee_types:
        existing = session.query(FeeType).filter_by(name=fee_name).first()
        if not existing:
            session.add(FeeType(name=fee_name))
    
    session.commit()
    
    # 2. Seed Customers
    # Check if we already have customers to avoid duplicates if run multiple times
    if session.query(Customer).count() > 5:
        print("Database already appears to be seeded.")
        session.close()
        return "Database already contains data."

    customers_data = [
        {
            "name": "Acme Properties LLC",
            "email": "accounts@acmeproperties.com",
            "property_address": "123 Main St, Springfield, IL 62704",
            "rate": 500.0,
            "cadence": "monthly",
            "fee_type": "Management Fee",
            "fee_2_type": "Maintenance Markup",
            "fee_2_rate": 50.0
        },
        {
            "name": "John & Jane Doe",
            "email": "jdoe@example.com",
            "property_address": "456 Oak Ave, Pleasantville, NY 10570",
            "rate": 1200.0,
            "cadence": "monthly",
            "fee_type": "Management Fee",
            "fee_2_type": None,
            "fee_2_rate": None
        },
        {
            "name": "Summit Holdings Inc.",
            "email": "billing@summitholdings.net",
            "property_address": "789 Pine Rd, Denver, CO 80203",
            "rate": 2500.0,
            "cadence": "quarterly",
            "fee_type": "Management Fee",
            "fee_2_type": "Inspection Fee",
            "fee_2_rate": 150.0,
            "fee_3_type": "Utility Management",
            "fee_3_rate": 75.0
        },
        {
            "name": "Sarah Smith",
            "email": "sarah.smith@testmail.com",
            "property_address": "321 Elm St, Austin, TX 78701",
            "rate": 350.0,
            "cadence": "monthly",
            "fee_type": "Placement Fee",
            "next_bill_date": date.today() + timedelta(days=5)
        },
        {
            "name": "Golden Gate Realty",
            "email": "finance@goldengate.com",
            "property_address": "555 Market St, San Francisco, CA 94105",
            "rate": 5000.0,
            "cadence": "monthly",
            "fee_type": "Management Fee",
            "fee_2_type": "Renewal Fee",
            "fee_2_rate": 250.0
        },
        {
            "name": "Robert Johnson",
            "email": "rjohnson@emailprovider.com",
            "property_address": "888 Broadway, Nashville, TN 37203",
            "rate": 800.0,
            "cadence": "monthly",
            "fee_type": "Management Fee"
        },
        {
            "name": "Lakeside Apartments",
            "email": "manager@lakesideapts.org",
            "property_address": "101 Lakeview Dr, Chicago, IL 60611",
            "rate": 3000.0,
            "cadence": "monthly",
            "fee_type": "Management Fee",
            "fee_2_type": "Maintenance Markup",
            "fee_2_rate": 200.0
        },
        {
            "name": "Highland Properties",
            "email": "contact@highlandprops.io",
            "property_address": "202 Highland Ave, Seattle, WA 98109",
            "rate": 1500.0,
            "cadence": "quarterly",
            "fee_type": "Management Fee"
        },
        {
            "name": "Emily Davis",
            "email": "emily.d@freemail.com",
            "property_address": "303 Cedar Ln, Miami, FL 33101",
            "rate": 450.0,
            "cadence": "monthly",
            "fee_type": "Management Fee",
            "fee_2_type": "Late Fee",
            "fee_2_rate": 25.0
        },
        {
            "name": "Urban Living LLC",
            "email": "payments@urbanliving.co",
            "property_address": "404 Urban Way, New York, NY 10001",
            "rate": 4000.0,
            "cadence": "monthly",
            "fee_type": "Management Fee",
            "fee_2_type": "Utility Management",
            "fee_2_rate": 100.0,
            "fee_3_type": "Inspection Fee",
            "fee_3_rate": 200.0
        },
        {
            "name": "Michael Wilson",
            "email": "mwilson@techmail.com",
            "property_address": "505 Tech Blvd, San Jose, CA 95113",
            "rate": 950.0,
            "cadence": "monthly",
            "fee_type": "Management Fee"
        },
        {
            "name": "Prestige Worldwide",
            "email": "investors@prestige.global",
            "property_address": "606 International Pkwy, Atlanta, GA 30303",
            "rate": 7500.0,
            "cadence": "yearly",
            "fee_type": "Management Fee",
            "fee_2_type": "Renewal Fee",
            "fee_2_rate": 500.0
        }
    ]

    for data in customers_data:
        # Split address into parts if needed, or just use raw string
        # Our model has property_city, property_state, property_zip
        # Let's parse the address string simply
        parts = data["property_address"].split(",")
        if len(parts) >= 3:
            addr = parts[0].strip()
            city = parts[1].strip()
            state_zip = parts[2].strip().split(" ")
            state = state_zip[0] if len(state_zip) > 0 else ""
            zip_code = state_zip[1] if len(state_zip) > 1 else ""
        else:
            addr = data["property_address"]
            city = ""
            state = ""
            zip_code = ""

        customer = Customer(
            name=data["name"],
            email=data["email"],
            property_address=addr,
            property_city=city,
            property_state=state,
            property_zip=zip_code,
            rate=data["rate"],
            cadence=data["cadence"],
            fee_type=data["fee_type"],
            fee_2_type=data.get("fee_2_type"),
            fee_2_rate=data.get("fee_2_rate"),
            fee_3_type=data.get("fee_3_type"),
            fee_3_rate=data.get("fee_3_rate"),
            next_bill_date=data.get("next_bill_date", date.today())
        )
        session.add(customer)

    session.commit()
    session.close()
    return "Database seeded successfully with 12 customers and fee types."
