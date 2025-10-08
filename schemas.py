from pydantic import BaseModel

class BookingCreate(BaseModel):
    name: str
    email: str
    phone: str
    class_type: str
    amount: float
