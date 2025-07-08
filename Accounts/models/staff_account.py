import uuid
from .base_account import Account

class StaffAccount(Account):
    """
    Staff account with a unique ID format.
    """

    def generate_unique_id(self):
        return f"OF-{uuid.uuid4().hex[:8].upper()}"
