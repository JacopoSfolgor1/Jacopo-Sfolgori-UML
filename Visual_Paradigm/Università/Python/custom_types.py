from typing import Self
import re
    

class IntGEZ(int):
    # Tipo di dato Intero >= 0

    def __new__(cls, v: int | float | str | bool | Self) -> Self:
        # Invoco il metodo new della superclasse, che è 'integer'
        n: int = super().__new__(cls, v)

        if n >= 0:
            return n

        raise ValueError(f"Il numero inserito {v} è inferiore a zero o non è intero!")
    

class IntGE1088(int):
    # Tipo di dato Intero >= 1088

    def __new__(cls, v: int | float | str | bool | Self) -> Self:
        # Invoco il metodo new della superclasse, che è 'integer'
        n: int = super().__new__(cls, v)

        if n >= 1088:
            return n

        raise ValueError(f"Il numero inserito {v} non è superiore a '1088' o intero!")
    

class CodiceFiscale(str):
    
    def __new__(cls, cf: str):
        if not re.fullmatch(r"[A-Z]{6}\d{2}[A-Z]\d{2}[A-L]\d{3}[A-Z0-9]", cf):
            raise ValueError(f"Codice fiscale non valido: '{cf}'")
        return str.__new__(cls, cf)