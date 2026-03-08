from typing import Literal


class PasswordManager:
    def __init__(self, password: str):
        pass

    def login(self, password: str):
        pass

    def lock(self):
        pass

    def add_login_entry(self, domain: str, username: str, password: str, alias: str = None):
        pass

    def show_login_entry(self, entry_alias: str):
        pass

    def remove_login_entry(self, entry_alias: str):
        pass

    def modify_login_entry(self, domain: str, entry_alias: str, new_username: str, new_password: str):
        pass

    def export(self, file_path: str, export_format: str = Literal["csv", "json"]):
        pass

    def import_from(self, file_path: str, import_format: Literal["csv", "json"]):
        pass
