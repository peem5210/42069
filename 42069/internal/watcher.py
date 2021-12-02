from services.gsheet.gsheet_service import GSheetService
from services.lai.lai_service import LaiService
from utils.util_func import load_env


def init_state():
    return {
        'cell_loc': 'E56',
        'previous_cell': '',
        'sheet_name': 'ลำดับ 1701-1800',
        'count': 0
    }


class Watcher:
    def __init__(self):
        load_env('./configs/google_sheet.env')
        load_env("./configs/lai.env")
        self.gsheet_service = GSheetService()
        self.lai_service = LaiService()

    def get_new_state(self, state):
        state['count'] += 1
        if state['count'] % 7 == 0:  # % 7 = 7000 secs
            self.lai_service.send_msg(f"{state['previous_cell']}, health-check")
        if state['sheet_name'] and state['cell_loc']:
            current_cell = self.gsheet_service.get_cell(state['sheet_name'], state['cell_loc'])
            if state['previous_cell'] != current_cell:
                self.lai_service.send_msg(f"previous: {state['previous_cell']}, current: {current_cell}")
                state['previous_cell'] = current_cell
        return state
