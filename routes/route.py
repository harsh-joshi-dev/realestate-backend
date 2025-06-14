from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from config.database import customer_collection, properties_collection
from models.customer import Customer
from models.property import Property
from schema.customer_schemas import list_customer_serial, individual_customer_serial
from schema.property_schemas import list_property_serial, individual_property_serial

router = APIRouter()

# ------------------------ Customer Routes ------------------------

@router.get("/customers", status_code=200)
async def get_customers():
    customers = list_customer_serial(customer_collection.find())
    return {"status": "success", "data": customers}


@router.post("/customers", status_code=201)
async def add_customer(customer: Customer):
    # Check for duplicate contact number
    if customer_collection.find_one({"contact_number": customer.contact_number}):
        raise HTTPException(status_code=400, detail="Customer with this contact number already exists.")

    result = customer_collection.insert_one(dict(customer))
    if result.inserted_id:
        return {"status": "success", "message": "Customer added successfully."}
    raise HTTPException(status_code=500, detail="Failed to add customer.")


@router.get("/customers/{id}", status_code=200)
async def get_customer(id: str):
    try:
        customer = customer_collection.find_one({"_id": ObjectId(id)})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format.")

    if customer:
        return {"status": "success", "data": individual_customer_serial(customer)}
    raise HTTPException(status_code=404, detail="Customer not found.")


@router.put("/customers/{id}")
async def update_customer(id: str, customer: Customer):
    result = customer_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(customer)}
    )
    if result:
        return {"status": "success", "message": "Customer updated successfully."}
    raise HTTPException(status_code=404, detail="Customer not found.")


@router.patch("/customers/assign/{id}")
async def assign_customer(id: str, data: dict):
    result = customer_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": data}
    )
    if result:
        return {"status": "success", "message": "Customer assigned successfully."}
    raise HTTPException(status_code=404, detail="Customer not found.")


@router.delete("/customers/{id}")
async def delete_customer(id: str):
    result = customer_collection.find_one_and_delete({"_id": ObjectId(id)})
    if result:
        return {"status": "success", "message": "Customer deleted successfully."}
    raise HTTPException(status_code=404, detail="Customer not found.")


# ------------------------ Property Routes ------------------------

@router.get("/properties", status_code=200)
async def get_properties():
    props = list_property_serial(properties_collection.find())
    return {"status": "success", "data": props}


@router.post("/properties", status_code=201)
async def add_property(property: Property):
    data = dict(property)

    # Add contractor details if old property
    if property.condition == "Old":
        if not data.get("contractor_details"):
            raise HTTPException(status_code=400, detail="Contractor details required for old properties.")

    result = properties_collection.insert_one(data)
    if result.inserted_id:
        return {"status": "success", "message": "Property added successfully."}
    raise HTTPException(status_code=500, detail="Failed to add property.")


@router.get("/properties/{id}", status_code=200)
async def get_property(id: str):
    try:
        prop = properties_collection.find_one({"_id": ObjectId(id)})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format.")

    if prop:
        return {"status": "success", "data": individual_property_serial(prop)}
    raise HTTPException(status_code=404, detail="Property not found.")


@router.put("/properties/{id}")
async def update_property(id: str, property: Property):
    result = properties_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(property)}
    )
    if result:
        return {"status": "success", "message": "Property updated successfully."}
    raise HTTPException(status_code=404, detail="Property not found.")


@router.patch("/properties/assign/{id}")
async def assign_property_to_customer(id: str, data: dict):
    result = properties_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": data}
    )
    if result:
        return {"status": "success", "message": "Property assigned to customer successfully."}
    raise HTTPException(status_code=404, detail="Property not found.")


@router.delete("/properties/{id}")
async def delete_property(id: str):
    result = properties_collection.find_one_and_delete({"_id": ObjectId(id)})
    if result:
        return {"status": "success", "message": "Property deleted successfully."}
    raise HTTPException(status_code=404, detail="Property not found.")
