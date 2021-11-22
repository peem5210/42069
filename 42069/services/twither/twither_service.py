from typing import Union

from utils.util_func import load_conf
from services.twither.twither_util import TwitherUtil


class TwitherService:
    def __init__(self):
        self.conf: dict[str, Union[str, int]] = load_conf(dir='configs/', name='linenot.json')
        self.util: TwitherUtil = TwitherUtil(self.conf)

    def do_something(self, something: str) -> dict[str, Union[str, int]]:
        res = {}
        return res
