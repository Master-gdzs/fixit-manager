from fastapi import APIRouter

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.get("/")
def get_customers():
    return [
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