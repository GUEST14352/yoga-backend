from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText
from fastapi.responses import JSONResponse

app = FastAPI()

class EmailRequest(BaseModel):
    name: str
    email: str
    message: str

@app.get("/")
def home():
    return {"message": "Yoga backend running ✅"}

@app.post("/send_email")
def send_email(data: EmailRequest):
    try:
        sender = "YOUR_GMAIL@gmail.com"
        app_password = "YOUR_APP_PASSWORD"
        recipient = "YOUR_GMAIL@gmail.com"

        subject = f"New Message from {data.name}"
        body = f"Name: {data.name}\nEmail: {data.email}\nMessage: {data.message}"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, app_password)
        server.send_message(msg)
        server.quit()

        return JSONResponse(content={"status": "success", "message": "Email sent successfully!"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
