from custom_types import IntG1900

class Compagnia: 

    _nome: str # noto alla nascita
    _anno: IntG1900 # <<immutable>>, noto alla nascita

    def __init__(self, nome: str, anno: IntG1900) -> None:
        self.set_nome(nome)
        self._anno = anno

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def anno(self) -> IntG1900:
        return frozenset(self._anno)

    def __repr__(self) -> str:
        return f"Compagnia(nome={self._nome})"
        