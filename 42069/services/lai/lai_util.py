import requests


class LaiUtil:
    def __init__(self, config):
        self.headers = {'content-type': 'application/x-www-form-urlencoded',
                        'Authorization': 'Bearer ' + config['token']}
        self.url = config['url']

    def send_msg_request(self, msg: str):
        response = requests.post(self.url, headers=self.headers, data={'message': msg}, timeout=10)
        res = {
            'status': response.status_code,
            'msg': response.json
        }
        return res
