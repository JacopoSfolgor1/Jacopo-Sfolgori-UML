
class Facoltà:

    _nome: str # noto alla nascita
    _tipo_facoltà: str # noto alla nascita

    def __init__(self, nome: str, tipo_facoltà: str) -> None:
        self.set_nome(nome)
        self.set_tipo_facoltà(tipo_facoltà)

    def nome(self) -> str:
        return self._nome
        
    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def tipo_facoltà(self) -> str:
        return self._tipo_facoltà
    
    def set_tipo_facoltà(self, tf: str) -> None:
        self._tipo_facoltà: str = tf

    def __repr__(self) -> str:
        return f"Facoltà(nome={self._nome})"