from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Booking(BaseModel):
    name: str
    email: str
    phone: str
    className: str
    amount: int
    paymentId: str | None = None

@app.post("/bookings")
def create_booking(booking: Booking):
    # Here: save to DB / send email
    return {"status": "success", "message": "Booking received!"}
