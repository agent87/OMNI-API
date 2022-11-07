# fastapi routes

from fastapi import FastAPI, Body, Depends, Request, Response, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import datetime
import uvicorn
import os
import aiofiles

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/image')
async def postImage(file:UploadFile=File(...)):
    content = await file.read()
    
    # image to text functionalities

    # sms by pindo functionalities

    sms = ''

    return {'sms':sms, 'file':file.filename}

@app.post('/audio')
async def postAudio(file:UploadFile=File(...)):
    content = await file.read()

    # audio to text functionalities

    # sms by pindo functionalities

    sms = ''

    return {'sms':sms, 'file':file.filename}