from typing import Union

from services.temp.capstone.capstone_util import CapStoneUtil


class CapStoneService:
    def __init__(self):
        self.util: CapStoneUtil = CapStoneUtil()

    def open_and_store_json(self, json) -> dict[str, Union[str, int]]:
        res = self.util.open_and_store_json(json)
        return res
