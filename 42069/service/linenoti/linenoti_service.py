from typing import Union

from util.util_func import load_conf
from service.linenoti.linenoti_util import LineNotiUtil


class LineNotiService:
    def __init__(self):
        self.conf = load_conf(dir='configs/', name='linenoti.json')
        self.util = LineNotiUtil(self.conf)

    def send_msg(self, msg: str) -> dict[str, Union[str, int]]:
        res = self.util.send_msg_request(msg)
        return res
