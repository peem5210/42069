from typing import Union

from utils.util_func import env
from services.lai.lai_util import LaiUtil


class LaiService:
    def __init__(self):
        self.conf = {'url': env('LAI_URL'), 'token': env('LAI_TOKEN')}
        self.util: LaiUtil = LaiUtil(self.conf)
        self.env = env('ENV')

    def send_msg(self, msg: str, force = True) -> dict[str, Union[str, int]]:
        if force or not self.env == 'local':
            res = self.util.send_msg_request(msg)
            return res
