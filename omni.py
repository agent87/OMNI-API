# fastapi routes

from fastapi import FastAPI, Body, Depends, Request, Response, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import datetime
import uvicorn
import os
import aiofiles

from utils import stt, pindo, ocr

app = FastAPI(title='OMNI API')
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
async def postImage(phone:str,file:UploadFile=File(...)):
    if not file:
        raise HTTPException(status_code=404, detail='No File Uploaded')
    content = await file.read()

    # image to text functionalities

    # sms by pindo functionalities
    sms = ''
    sms_response = pindo.send_sms(phone, sms)

    return {'Success':True,'sms':sms, 'phone':phone, 'file':file.filename}

@app.post('/audio')
async def postAudio(phone:str,file:UploadFile=File(...)):
    if not file:
        raise HTTPException(status_code=404, detail='No File Uploaded')
    content = await file.read()

    # audio to text functionalities
    STT = stt.convert
    speech_converted = STT.to_text(content)

    # sms by pindo functionalities
    sms = speech_converted
    sms_response = pindo.send_sms(phone, sms)

    return {'Success':True, 'sms':sms, 'phone':phone, 'file':file.filename}

if __name__=='__main__':
    port = os.getenv('PORT',default=8000)
    app_str = 'omni:app'
    uvicorn.run(app_str, host='0.0.0.0', port=int(port) or 8000, reload=True)