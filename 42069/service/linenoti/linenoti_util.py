import requests


class LineNotiUtil:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
    
    
    def send_msg_request(self, msg: str):
        response = requests.post(self.url, headers=self.headers, data={'message':msg})
        res = {
            'status': response.status_code,
            'msg': response.json
            }
        return res