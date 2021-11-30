import json
import gspread
import pandas as pd
import os

TMP_SERVICE_ACCOUNT_PATH = './google_cloud_storage_service_account.json'


class GSheetConnector:
    def __init__(self, service_account, sheets_id):

        try:
            with open(TMP_SERVICE_ACCOUNT_PATH, 'w') as service_account_file:
                json.dump(service_account, service_account_file)
            service_account_path = TMP_SERVICE_ACCOUNT_PATH
            self.gc = gspread.service_account(filename=service_account_path)
            self.sh = self.gc.open_by_key(sheets_id)
            self.sheet_list = self.get_sheet_list()
        finally:
            if os.path.isfile(TMP_SERVICE_ACCOUNT_PATH):
                print(service_account)
                pass
                # os.remove(TMP_SERVICE_ACCOUNT_PATH)

    def upsert_sheet_by_df(self, sheet_name, df):
        self.sh.worksheet(sheet_name).update([df.columns.values.tolist()] + df.values.tolist())

    def clear_sheet(self, sheet_name):
        self.sh.worksheet(sheet_name).clear()

    def get_sheet(self, name):
        return self.sh.worksheet(name)

    def get_sheet_values(self, name):
        return self.sh.worksheet(name).get_all_values()

    def get_sheet_list(self):
        return [x.title for x in self.sh.worksheets()]

    def get_all_sheet_value(self):
        d = dict()
        for x in self.sheet_list: d[x] = self.get_sheet_values(x)
        return d

    def get_next_avail_row(self, name):
        str_list = list(filter(None, self.sh.worksheet(name).col_values(1)))
        return str(len(str_list) + 1)

    def save_all_sheet(self, orient='records', path=''):
        for x in self.sheet_list:
            if (x != 'description'):
                df = self.to_df(self.get_sheet_values(x))
                df.to_json(path + x + '.json', orient=orient)

    def to_df(self, sheet):
        data = sheet
        headers = data.pop(0)
        headers = [i for i in headers if i]
        data = [i[:len(headers)] for i in data]
        df = pd.DataFrame(data, columns=headers)
        return df
