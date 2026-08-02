from pydantic import BaseModel

class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    phone: str


class Customer(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone: str