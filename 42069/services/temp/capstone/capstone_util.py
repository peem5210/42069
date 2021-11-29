import json
import pathlib
import pandas as pd
from datetime import datetime
from services.lai.lai_service import LaiService


class CapStoneUtil:
    def __init__(self):
        self.lai_service = LaiService()

    def open_and_store_json(self, json_d):
        json_string = json.dumps(json_d)
        pathlib.Path('./data').mkdir(parents=True, exist_ok=True)
        pd.DataFrame.from_dict(json_d).to_csv(f"./data/{str(datetime.now())}.csv")
        return self.lai_service.send_msg(json_string)