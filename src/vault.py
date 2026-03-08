class Vault:
    def __init__(self):
        self.entries = {}  # key = alias, value = VaultEntry


class VaultEntry:
    def __init__(self, username: str, hashed_password: str, alias: str):
        pass
