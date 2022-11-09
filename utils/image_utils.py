from utils import ocr, pindo
from PIL import Image

def image_processing(content, phone=None):
    img = Image.open(content)
    try:
        OCR = ocr.convert
        image_converted = OCR.to_text(img)
        if image_converted=='':
            image_converted = 'Nta nteruro ibashije kumvamo.'
        success = True
    except Exception as e:
        print(e)
        image_converted = 'Habaye ikibazo muri system'
        success = False
    sms = image_converted
    print(image_converted)
    # if phone!=None:
    #     sms_response = pindo.send_sms(sms, phone)
    # else:
    #     sms_response = pindo.send_sms(sms)
    
    return {'success':success, 'sms':sms, 'phone':phone}