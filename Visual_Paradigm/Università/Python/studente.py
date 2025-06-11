from custom_types import CodiceFiscale
from typing import Any
import datetime


class Studente: 

    _nome: str # noto alla nascita
    _cf: CodiceFiscale # noto alla nascita
    _nascita: datetime.date # noto alla nascita
    _n_matricola: str # immutabile, noto alla nascita

    def __init__(self, nome: str, cf: CodiceFiscale, nascita: datetime.date, n_matricola: str) -> None:
        self.set_nome(nome)
        self.set_cf(cf)
        self.set_nascita(nascita)
        self._n_matricola = n_matricola

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def cf(self) -> CodiceFiscale:
        return self._cf
    
    def set_cf(self, cf: CodiceFiscale) -> None:
        self._cf: CodiceFiscale = cf 
    
    def nascita(self) -> datetime.date:
        return self._nascita
    
    def set_nascita(self, n: datetime.date) -> None:
        self._nascita: datetime.date = n

    def n_matricola(self) -> str:
        return frozenset(self._n_matricola)
    
    def __hash__(self) -> int:
        return hash((self.nome(), self.cf(), self.nascita(), self.n_matricola()))
    
    def __eq__(self, other: Any) -> bool:
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return (self.nome(), self.cf(), self.nascita(), self.n_matricola()) == (other.nome(), other.cf(), other.nascita(), other.n_matricola())

    def __repr__(self) -> str:
        return f"Studente(nome={self._nome})"
        