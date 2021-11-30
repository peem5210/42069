from services.gsheet.gsheet_service import GSheetService
from services.lai.lai_service import LaiService
from utils.util_func import load_env


def init_state():
    return {
        'cell_loc': 'E56',
        'previous_cell': '',
        'sheet_name': 'ลำดับ 1701-1800',
    }


class Watcher:
    def __init__(self):
        load_env(path='./configs/google_sheet.env')
        load_env("./configs/lai.env")
        self.gsheet_service = GSheetService()
        self.lai_service = LaiService()

    def check_cell(self, state):
        if state['sheet_name'] and state['cell_loc']:
            current_cell = self.gsheet_service.get_cell(state['sheet_name'], state['cell_loc'])
            if state['cell_loc'] and state['previous_cell'] != current_cell:
                state['previous_cell'] = current_cell
                self.lai_service.send_msg(str(state['previous_cell']))
        return state
