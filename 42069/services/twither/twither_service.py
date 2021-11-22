from typing import Union

from utils.util_func import load_conf
from services.twither.twither_util import TwitherUtil


class TwitherService:
    def __init__(self):
        try:
            self.conf: dict[str, Union[str, int]] = {}
            self.util: TwitherUtil = TwitherUtil(self.conf)
        except Exception as e:
            print(f"error: {str(e)}")

    def do_something(self, something: str) -> dict[str, Union[str, int]]:
        res = {}
        return res
