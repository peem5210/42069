from typing import Union

from services.temp.capstone.capstone_util import CapStoneUtil


class CapStoneService:
    def __init__(self):
        self.util: CapStoneUtil = CapStoneUtil()

    def open_and_store_json(self, json, name='') -> dict[str, Union[str, int]]:
        res = self.util.open_and_store_json(json, name=name)
        return res

    def read_all(self) -> dict[str, Union[str, int, list[dict]]]:
        res = self.util.read_all()
        return res

    def clear(self):
        return self.util.clear()