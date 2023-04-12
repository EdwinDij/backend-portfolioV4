from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from email.mime.text import MIMEText
from dotenv import load_dotenv


import smtplib
import os
import json

app = FastAPI()
load_dotenv()
password = os.getenv('MAIL_PASS')
email = os.getenv('MAIL')

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/data")
def get_data():
    with open('./data/data.json') as f:
        data = json.load(f)
        return data
    
    

@app.post("/api/send-email")
async def send_email(request: Request):
    form = await request.form()
    name = form.get('name')
    email_sender = form.get('email')
    message = form.get('message')
    
    if not name or not email_sender or not message:
        raise HTTPException(status_code=400, detail='Champs manquants')
    
    
    recipient = email
    subject = f'Nouveau message de {name} depuis le portfolio!'
    body = f'Nom: {name} \nEmail: {email_sender} \nMessage: {message}'
    
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = email_sender
    message['To'] = recipient
    message['Importance'] = 'High'
    
    try: 
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email, password)
            smtp.sendmail(email_sender, recipient, message.as_string())
            return JSONResponse(status_code=200, content={'message': 'Message envoyé avec succès!'})
    except smtplib.SMTPException as e:
        raise HTTPException(status_code=500, detail='Erreur lors de l\'envoi du message: ' + str(e))

