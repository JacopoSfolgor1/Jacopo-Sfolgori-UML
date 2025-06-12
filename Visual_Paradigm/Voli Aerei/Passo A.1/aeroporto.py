from typing import Any

class Aeroporto:

    _nome: str # mutabile, noto alla nascita
    _codice: str # <<immutable>>, noto alla nascita 
  
    def __init__(self, nome: str, codice: str) -> None:
        self.set_nome(nome)
        self._codice = codice 
      
    def nome(self) -> str:
        return self._nome

    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def codice(self) -> str:
        return frozenset(self._codice)
 
    def __hash__(self) -> int:
        return hash((self.nome(), self.codice()))

    def __eq__(self, other: Any) -> bool:
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return (self.nome(), self.codice()) == (other.nome(), other.codice())

    def __repr__(self) -> str:
        return f"Aeroporto(nome={self._nome})"
        