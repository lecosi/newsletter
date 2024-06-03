from tempfile import TemporaryFile
from typing import Union


class Newsletter:

    def __init__(self, name: str, id: str, file: Union[TemporaryFile, None]):
        self._name = name
        self._id = id
        self._file = file

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def file(self) -> Union[TemporaryFile, None]:
        return self._file

