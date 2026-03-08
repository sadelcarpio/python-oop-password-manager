from typing import Literal

from vault import VaultEntry


class PasswordManager:
    def __init__(self, username: str, password: str):
        pass

    def login(self, username: str, password: str):
        pass

    def lock(self):
        pass

    def add_login_entry(self, entry: VaultEntry):
        pass

    def show_login_entry(self, entry_alias: str):
        pass

    def remove_login_entry(self, entry_alias: str):
        pass

    def modify_login_entry(self, entry_alias: str, new_entry: VaultEntry):
        pass

    def export(self, export_format: str = Literal["csv", "json"]):
        pass

    def import_from(self, other_manager: "PasswordManager"):
        pass
