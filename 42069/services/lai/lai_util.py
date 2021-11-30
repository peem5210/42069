import requests


class LaiUtil:
    def __init__(self, config):
        self.headers = {'content-type': 'application/x-www-form-urlencoded',
                        'Authorization': 'Bearer ' + config['token']}
        self.url = config['url']

    def send_msg_request(self, msg: str):
        print("sending lai request..")
        response = requests.post(self.url, headers=self.headers, data={'message': msg}, timeout=2)
        print("send")
        res = {
            'status': response.status_code,
            'msg': response.json
        }
        return res
