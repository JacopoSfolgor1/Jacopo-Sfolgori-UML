from typing import Any

class Nazione: 

    _nome: str # noto alla nascita

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def __hash__(self) -> int:
        return hash(self.nome())

    def __eq__(self, other: Any) -> bool:
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return (self.nome()) == (other.nome())

    def __repr__(self) -> str:
        return f"Nazione(nome={self._nome})"