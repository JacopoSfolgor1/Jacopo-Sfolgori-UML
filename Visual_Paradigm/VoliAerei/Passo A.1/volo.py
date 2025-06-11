from custom_types import IntGZ
from typing import Any


class Volo: 

    _codice: str # <<immutable>>, noto alla nascita
    _durata_min: IntGZ # mutabile, noto alla nascita

    def __init__(self, codice: str, durata_min: IntGZ) -> None:
        self._codice = codice
        self.set_durata_min(durata_min)

    def durata_min(self) -> IntGZ:
        return self._durata_min

    def set_durata_min(self, dm: IntGZ) -> None:
        self._durata_min = dm

    def codice(self) -> str:
        return frozenset(self._codice)
    
    def __hash__(self) -> int:
        return hash((self.codice(), self.durata_min()))

    def __eq__(self, other: Any) -> bool:
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return (self.codice(), self.durata_min()) == (other.codice(), other.durata_min())
                
    def __repr__(self) -> str:
       return f"Volo(codice={self._codice}, durata={self._durata_min})"
 