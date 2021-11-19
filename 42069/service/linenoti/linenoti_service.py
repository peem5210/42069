from typing import Union

from util.util_func import load_conf
from service.linenoti.linenoti_util import LineNotiUtil


class LineNotiService:
    def __init__(self):
        self.conf = load_conf(dir='configs/', name='linenoti.json')
        self.headers = {'content-type': 'application/x-www-form-urlencoded',
                        'Authorization': 'Bearer ' + self.conf['token']}
        self.util = LineNotiUtil(self.conf['url'], self.headers)

    def send_msg(self, msg: str) -> dict[str, Union[str, int]]:
        res = self.send_msg_request(msg)
        return res
