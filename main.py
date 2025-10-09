from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# --- FIX #1: Enable CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later, replace * with your actual frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Booking model ---
class Booking(BaseModel):
    name: str
    email: str
    phone: str
    className: str
    amount: int
    paymentId: str | None = None

# --- FIX #2: Root route ---
@app.get("/")
def root():
    return {"message": "Yoga backend running ✅"}

# --- Booking route ---
@app.post("/bookings")
def create_booking(booking: Booking):
    print("📥 Booking received:", booking.dict())
    return {"status": "success", "message": "Booking received successfully!"}

