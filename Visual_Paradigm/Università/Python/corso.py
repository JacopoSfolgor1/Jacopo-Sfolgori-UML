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

    def __repr__(self) -> str:
        return f"Corso(nome={self._nome})"
        