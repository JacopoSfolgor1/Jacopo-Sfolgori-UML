from custom_types import CodiceFiscale
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

    def __repr__(self) -> str:
        return f"Studente(nome={self._nome})"
        