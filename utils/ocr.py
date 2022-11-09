import requests
import os

class convert:
    url = "https://freeocrapi.com/api"


    def to_text(image):
        file = {'file':image}
        response = requests.post(convert.url, files=file)
        return response.text