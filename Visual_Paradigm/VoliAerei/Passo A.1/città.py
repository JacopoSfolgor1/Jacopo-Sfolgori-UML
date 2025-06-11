from custom_types import IntGEZ
from typing import Any


class Città: 

    _nome: str # noto alla nascita
    _abitanti: IntGEZ # mutabile, noto alla nascita

    def __init__(self, nome: str, abitanti: IntGEZ) -> None:
        self.set_nome(nome)
        self.set_abitanti(abitanti)

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def abitanti(self) -> IntGEZ:
        return self._abitanti
    
    def set_abitanti(self, a: IntGEZ) -> None:
        self._abitanti = a

    def __hash__(self) -> int:
        return hash((self.nome(), self.abitanti()))
    
    def __eq__(self, other: Any) -> bool:
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return (self.nome(), self.abitanti()) == (other.nome(), other.abitanti())

    def __repr__(self) -> str:
        return f"Città(nome={self._nome})"