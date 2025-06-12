from custom_types import CodiceFiscale
import datetime


class Professore: 

    _nome: str # noto alla nascita
    _cf: CodiceFiscale # noto alla nascita
    _nascita: datetime.date # noto alla nascita

    def __init__(self, nome: str, cf: CodiceFiscale, nascita: datetime.date) -> None:
        self.set_nome(nome)
        self.set_cf(cf)
        self.set_nascita(nascita)

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

    def __repr__(self) -> str:
        return f"Professore(nome={self._nome})"
        