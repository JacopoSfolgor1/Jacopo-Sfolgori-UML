
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
 
    def __repr__(self) -> str:
        return f"Aeroporto(nome={self._nome})"
        