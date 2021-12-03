from services.gsheet.gsheet_connector import GSheetConnector
from services.gsheet.gsheet_service import get_service_account


class DotoSchema:
    ID = 'A'
    COM = 'E'
    LAST = 'Z'


class DotoService:
    def __init__(self):
        self.gsheet_connector = GSheetConnector(get_service_account(), "1ff2kdL-N93OJAKDMh9NP9QJXXgoJY6Rv7ogF2Jpgd1U")
        self.todo_sh = self.gsheet_connector.get_sheet('todo')

    def get_todos(self):
        return self.gsheet_connector.to_df(self.todo_sh.get_all_values()).to_dict(orient='records')

    def add_todo(self, todo, desc, priority):
        id = self.gsheet_connector.get_next_avail_row('todo')
        return self.todo_sh.append_row((id, todo, desc, priority))

    def complete_todo(self, id):
        self.todo_sh.update(f'{DotoSchema.COM}{id}', "Yes")
        return self.todo_sh.get(f'{DotoSchema.ID}{id}:{DotoSchema.LAST}{id}')

