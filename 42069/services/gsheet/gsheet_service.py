from utils.util_func import env
from services.gsheet.gsheet_connector import GSheetConnector


def get_service_account():
    service_account_keys = [
        "type",
        "project_id",
        "private_key_id",
        "private_key",
        "client_email",
        "client_id",
        "auth_uri",
        "token_uri",
        "auth_provider_x509_cert_url",
        "client_x509_cert_url",
    ]

    service_account = {}
    for key in service_account_keys:
        service_account[key] = env(key.upper())
    return service_account


class GSheetService:
    def __init__(self):
        self.connector: GSheetConnector = GSheetConnector(get_service_account(),
                                                          "1hqADqovYx7n6N7cWPIZ7gg7RFf46yji3gYrJL2GqoBI")

    def sheet_list(self):
        return self.connector.sheet_list

    def get_cell(self, sheet_name, cell):
        return self.connector.get_sheet(sheet_name).acell(cell).value
