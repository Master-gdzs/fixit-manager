from fastapi import APIRouter

from app.schemas.customer import Customer, CustomerCreate

router = APIRouter(prefix="/customers", tags=["Customers"])

customers = [
    {
        "id": 1,
        "first_name": "Иван",
        "last_name": "Петров",
        "phone": "+380501112233",
    },
    {
        "id": 2,
        "first_name": "Сергей",
        "last_name": "Иванов",
        "phone": "+380671234567",
    },
]

@router.get("/", response_model=list[Customer])
def get_customers():
    return customers


@router.post("/", response_model=Customer)
def create_customer(customer: CustomerCreate):
    new_customer = {
        "id": len(customers) + 1,
        "first_name": customer.first_name,
        "last_name": customer.last_name,
        "phone": customer.phone,
    }

    customers.append(new_customer)

    return new_customer
