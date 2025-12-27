# Sample Equipment Data
from equipment.models import Equipment, EquipmentCategory

# Create categories
categories = [
    ("HVAC", "Climate Control", "Building Management"),
    ("Electrical", "Power Systems", "Electrical Services"),
    ("Mechanical", "Machinery", "Industrial Equipment"),
    ("Plumbing", "Water Systems", "Facility Management"),
    ("Safety", "Safety Equipment", "Security & Safety"),
    ("IT", "Technology", "IT Department")
]

equipment_data = [
    {
        "asset_id": "HVAC-001",
        "name": "Central Air Conditioning Unit",
        "category": "HVAC",
        "company": "Climate Control Inc.",
        "serial_no": "ACU-2024-001",
        "technician": "John Smith",
        "maintenance_team": "HVAC Team",
        "maintenance_interval_days": 30,
        "status": "active",
        "description": "Main building air conditioning system, 50-ton capacity, serves floors 1-5"
    },
    {
        "asset_id": "ELEC-001",
        "name": "Main Electrical Panel",
        "category": "Electrical",
        "company": "Power Systems Ltd.",
        "serial_no": "EP-2024-001",
        "technician": "Mike Johnson",
        "maintenance_team": "Electrical Team",
        "maintenance_interval_days": 60,
        "status": "active",
        "description": "Primary electrical distribution panel, 400A service, controls building power"
    },
    {
        "asset_id": "MECH-001",
        "name": "Industrial Pump System",
        "category": "Mechanical",
        "company": "Industrial Machinery Co.",
        "serial_no": "IPS-2024-001",
        "technician": "Sarah Davis",
        "maintenance_team": "Mechanical Team",
        "maintenance_interval_days": 45,
        "status": "active",
        "description": "High-pressure water pump system, 500 GPM capacity, critical for production"
    },
    {
        "asset_id": "PLUMB-001",
        "name": "Water Treatment System",
        "category": "Plumbing",
        "company": "Aqua Solutions",
        "serial_no": "WTS-2024-001",
        "technician": "Tom Wilson",
        "maintenance_team": "Plumbing Team",
        "maintenance_interval_days": 90,
        "status": "active",
        "description": "Water filtration and treatment system, serves entire facility"
    },
    {
        "asset_id": "SAFE-001",
        "name": "Fire Suppression System",
        "category": "Safety",
        "company": "Safety First Inc.",
        "serial_no": "FSS-2024-001",
        "technician": "Lisa Anderson",
        "maintenance_team": "Safety Team",
        "maintenance_interval_days": 30,
        "status": "active",
        "description": "Automated fire suppression system, covers all building areas"
    },
    {
        "asset_id": "IT-001",
        "name": "Server Room Cooling",
        "category": "IT",
        "company": "Tech Solutions",
        "serial_no": "SRC-2024-001",
        "technician": "David Chen",
        "maintenance_team": "IT Team",
        "maintenance_interval_days": 15,
        "status": "active",
        "description": "Precision cooling system for server room, 24/7 operation"
    }
]

# Create categories and equipment
for cat_name, responsible, company in categories:
    category, created = EquipmentCategory.objects.get_or_create(
        name=cat_name,
        defaults={
            'responsible': responsible,
            'company': company
        }
    )
    print(f"Category '{cat_name}' created: {created}")

# Create equipment
for data in equipment_data:
    category = EquipmentCategory.objects.get(name=data['category'])
    equipment, created = Equipment.objects.get_or_create(
        asset_id=data['asset_id'],
        defaults={
            'name': data['name'],
            'category': category,
            'company': data['company'],
            'serial_no': data['serial_no'],
            'technician': data['technician'],
            'maintenance_team': data['maintenance_team'],
            'maintenance_interval_days': data['maintenance_interval_days'],
            'status': data['status'],
            'description': data['description']
        }
    )
    print(f"Equipment '{data['asset_id']}' created: {created}")

print("Sample equipment data loaded successfully!")
