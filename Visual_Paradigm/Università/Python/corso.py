from custom_types import IntGEZ
from typing import Any

class Corso: 

    _nome: str # noto alla nascita
    _n_ore_lezione: IntGEZ # noto alla nascita
    _codice: str # immutabile, noto alla nascita

    def __init__(self, nome: str, n_ore_lezione: IntGEZ, codice: str) -> None:
        self.set_nome(nome)
        self.set_n_ore_lezione(n_ore_lezione)
        self._codice = codice

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def n_ore_lezione(self) -> IntGEZ:
        return self._n_ore_lezione
    
    def set_n_ore_lezione(self, nol: IntGEZ) -> None:
        self._n_ore_lezione: IntGEZ = nol 

    def codice(self) -> str:
        return frozenset(self._codice)
    
    def __hash__(self) -> int:
        return hash((self.nome(), self.n_ore_lezione(), self.codice()))
    
    def __eq__(self, other: Any) -> bool:
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return (self.nome(), self.n_ore_lezione(), self.codice()) == (other.nome(), other.n_ore_lezione(), other.codice())

    def __repr__(self) -> str:
        return f"Corso(nome={self._nome})"
        