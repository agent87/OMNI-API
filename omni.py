# fastapi routes

from fastapi import FastAPI, Body, Depends, Form, Request, Response, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import datetime
import uvicorn
import os
import aiofiles

from utils import audio_utils, image_utils

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

templates = Jinja2Templates(directory='templates')
app.mount('/static',StaticFiles(directory='static'), name='static')

# @app.post('/image')
# async def postImage(phone:str,file:UploadFile=File(...)):
#     if not file:
#         raise HTTPException(status_code=404, detail='No File Uploaded')
#     content = await file.read()
#     response = image_utils.image_processing(content, phone)

#     return {'Success':response['success'], 'sms':response['sms'], 'phone':response['phone'], 'file':file.filename}

@app.get('/audio', response_class=HTMLResponse)
async def audio_get(request:Request):
    return templates.TemplateResponse('form.html',{'request':request})

@app.post('/audio', response_class=HTMLResponse)
async def audio_post(request:Request, file:UploadFile=File(...), phone:str=Form(...)):
    phone = phone
    if not file:
        raise HTTPException(status_code=404, detail='No File Uploaded')
    content = await file.read()

    response = audio_utils.audio_processing(content, phone)
    return templates.TemplateResponse('form.html',{'request':request,'response':response})


@app.post('/api/audio')
async def apiPostAudio(phone:str,file:UploadFile=File(...)):
    if not file:
        raise HTTPException(status_code=404, detail='No File Uploaded')
    content = await file.read()

    response = audio_utils.audio_processing(content, phone)

    return {'Success':response['success'], 'sms':response['sms'], 'phone':response['phone'], 'file':file.filename}

if __name__=='__main__':
    port = os.getenv('PORT',default=8000)
    app_str = 'omni:app'
    uvicorn.run(app_str, host='0.0.0.0', port=int(port) or 8000, reload=True)