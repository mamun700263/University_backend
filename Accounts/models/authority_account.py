import uuid

from .base_account import Account

class AuthorityAccount(Account):
    """
    Authority account with a unique ID format.
    """

    def generate_unique_id(self):
        return f"AU-{uuid.uuid4().hex[:8].upper()}"
