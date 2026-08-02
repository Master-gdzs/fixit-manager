from fastapi import APIRouter

from app.schemas.customer import Customer

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.get("/", response_model=list[Customer])
def get_customers():
    return [
        Customer(
            id=1,
            first_name= "Иван",
            last_name= "Петров",
            phone= "+380501112233",
        ),
        Customer(
            id=2,
            first_name= "Сергей",
            last_name= "Иванов",
            phone= "+380671234567",
        ),
    ]