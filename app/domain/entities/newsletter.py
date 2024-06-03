
class Newsletter:

    def __init__(self, name: str, id: str):
        self._name = name
        self._id = id

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

