import requests



class convert:
    url = "https://kws.mbaza.dev.cndp.org.rw/kinyarwanda/api/v1/stt/http"
    token  = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5LCJleHAiOjE2Njk4ODQ0NDEuNTUxNjA0fQ.Yp90vtm3v_1fY9RWfA8-kxKIwpw8o3T2IBil2QEMvX0"
    

    def to_text(audio):
        headers = {'Authorization': 'Bearer ' + convert.token}
        audio = [('audio', audio)]
        response = requests.post(convert.url, files=audio, headers=headers)
        return response.json()['message']
