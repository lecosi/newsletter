from .recipient import Recipient


class Newsletter:

    def __init__(self, recipients: list[Recipient]):
        self._recipients = recipients

