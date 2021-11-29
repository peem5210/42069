import os
import io
import json
import shutil
import pathlib
import pandas as pd
from datetime import datetime
from starlette.responses import StreamingResponse
from services.lai.lai_service import LaiService


class CapStoneUtil:
    def __init__(self):
        self.lai_service = LaiService()
        self.dir = './data'

    def open_and_store_json(self, json_d, name=''):
        json_string = json.dumps(json_d)
        pathlib.Path(self.dir).mkdir(parents=True, exist_ok=True)
        pd.DataFrame.from_dict(json_d).to_csv(os.path.join(self.dir, f"{name}--{str(datetime.now())}.csv"))
        return self.lai_service.send_msg(json_string)

    def read_all(self):
        df = pd.DataFrame()
        for f in os.listdir(self.dir):
            try:
                df = df.append(pd.read_csv(os.path.join(self.dir, f)))
            except Exception:
                continue
        s_buf = io.StringIO()
        df.reset_index(drop=True).to_csv(s_buf)
        s_buf.seek(0)
        return StreamingResponse(s_buf)

    def list_all(self):
        return os.listdir(self.dir)

    def clear(self):
        shutil.rmtree(self.dir)
        pathlib.Path(self.dir).mkdir(parents=True, exist_ok=True)
        return "ok"

