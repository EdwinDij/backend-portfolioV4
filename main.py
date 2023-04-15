from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from email.mime.text import MIMEText
from dotenv import load_dotenv
from fastapi.responses import FileResponse

import smtplib
import os
import json

app = FastAPI()
load_dotenv()

password = os.getenv('MAIL_PASS')
email = os.getenv('MAIL')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello world from the server"}

@app.get("/api/data")
def get_data():
    with open('./data/data.json') as f:
        data = json.load(f)
        return data
    
@app.get("/api/data_paginated")
async def get_data_pagiated( page: int = 1, limit: int = 4):
    with open('./data/data.json') as f:
        data = json.load(f)
        start = (page - 1) * limit
        end = start + limit
        return data["project"][start:end]
    
@app.get("/api/data/{image_path:path}")
async def get_image(image_path: str):
    return FileResponse("images/" + image_path)

@app.post("/api/data")
async def post_new_data(request: Request):
    with open('./data/data.json') as f:
        data = json.load(f)
        
    form = await request.form()
    name = form.get('name')
    description = form.get('description')
    url_github = form.get('url_github')
    url_website = form.get('url_website')
    role = form.get('role')
    image = form.get('image')
    techno = form.get('techno')
    
    if not name or not description or not url_github  or not role or not techno:
        raise HTTPException(status_code=400, detail='Champs manquants')
    
    try :
        with open('./data/data.json', 'w') as f:
            techno = [t.strip() for t in techno.split(', ')]
            data['project'].append({
                "id": len(data['project']) + 1,
                "name": name,
                "description": description,
                "url_github": url_github,
                "url_website": url_website,
                "role": role,
                "image": image,
                "techno": [techno]
            })
            json.dump(data, f, indent=4)
            return JSONResponse(status_code=200, content={'message': 'Nouveau projet ajouté avec succès!', 'data': data['project'][-1]})
    except Exception as e:
        raise HTTPException(status_code=500, detail='Erreur lors de l\'ajout du projet: ' + str(e))

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
