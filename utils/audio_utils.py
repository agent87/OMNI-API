from utils import stt, pindo

def audio_processing(content, phone=None):
    try:
        STT = stt.convert
        speech_converted = STT.to_text(content)
        if speech_converted=='':
            speech_converted = 'Nta nteruro ibashije kumvamo.'
        success = True
    except Exception as e:
        speech_converted = 'Habaye ikibazo muri sisiteme'
        success = False
    sms = speech_converted
    if phone!=None:
        sms_response = pindo.send_sms(sms, phone)
    else:
        sms_response = pindo.send_sms(sms)
    
    return {'success':success, 'sms':sms, 'phone':phone}