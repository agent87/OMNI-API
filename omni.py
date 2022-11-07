# fastapi routes

from fastapi import FastAPI, Body, Depends, Request, Response, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import datetime
import uvicorn
import os
import aiofiles

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
async def postImage(file:UploadFile=File(...)):
    if not file:
        raise HTTPException(status_code=404, detail='No File Uploaded')
    content = await file.read()

    # image to text functionalities

    # sms by pindo functionalities

    sms = ''

    return {'Success':True,'sms':sms, 'file':file.filename}

@app.post('/audio')
async def postAudio(file:UploadFile=File(...)):
    if not file:
        raise HTTPException(status_code=404, detail='No File Uploaded')
    content = await file.read()

    # audio to text functionalities

    # sms by pindo functionalities

    sms = ''

    return {'Success':True,'sms':sms, 'file':file.filename}

if __name__=='__main__':
    port = os.getenv('PORT',default=8000)
    app_str = 'app:app'
    uvicorn.run(app_str, host='0.0.0.0', port=int(port) or 8000, reload=True)