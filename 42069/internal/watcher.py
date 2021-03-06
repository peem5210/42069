from services.gsheet.gsheet_service import GSheetService
from services.lai.lai_service import LaiService
from utils.util_func import load_env

load_env('./configs/google_sheet.env')
load_env("./configs/lai.env")


class Watcher:
    def __init__(self):
        self.gsheet_service = GSheetService()
        self.lai_service = LaiService()

    @property
    def init_state(self):
        return {
            'cell_loc': 'E56',
            'previous_cell': '',
            'sheet_name': 'ลำดับ 1701-1800',
        }

    def get_new_state(self, state):
        if state['sheet_name'] and state['cell_loc']:
            current_cell = self.gsheet_service.get_cell(state['sheet_name'], state['cell_loc'])
            if state['previous_cell'] != current_cell:
                self.lai_service.send_msg(f"previous: {state['previous_cell']}, current: {current_cell}")
                state['previous_cell'] = current_cell
        return state
