from typing import Union

from utils.util_func import load_conf, load_env, env
from services.lai.lai_util import LaiUtil


class LaiService:
    def __init__(self):
        self.conf = {}
        try:
            self.conf: dict[str, Union[str, int]] = load_conf(dir='./42069/configs/', name='linenoti.json')
        except Exception:
            load_env('./configs/', name='lai')
            self.conf['url'] = env('LAI_URL')
            self.conf['token'] = env('LAI_TOKEN')
        self.util: LaiUtil = LaiUtil(self.conf)

    def send_msg(self, msg: str) -> dict[str, Union[str, int]]:
        res = self.util.send_msg_request(msg)
        return res
