from email.mime.text import MIMEText
from typing import Union
from urllib import request
from fastapi import FastAPI, Form
from dotenv import load_dotenv

import os
import smtplib

app = FastAPI()
load_dotenv()
password = os.getenv('MAIL_PASS')
email = os.getenv('MAIL')

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/send-email")