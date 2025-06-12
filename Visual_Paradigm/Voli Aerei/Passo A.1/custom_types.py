from typing import Self

class IntGZ(int):
    # Tipo di dato Intero > 0

    def __new__(cls, v: int | float | str | bool | Self) -> Self:
        # Invoco il metodo new della superclasse, che è 'integer'
        n: int = super().__new__(cls, v)

        if n > 0:
            return n

        raise ValueError(f"Il numero inserito {v} non è superiore a zero o intero!")
    

class IntGEZ(int):
    # Tipo di dato Intero >= 0

    def __new__(cls, v: int | float | str | bool | Self) -> Self:
        # Invoco il metodo new della superclasse, che è 'integer'
        n: int = super().__new__(cls, v)

        if n >= 0:
            return n

        raise ValueError(f"Il numero inserito {v} è inferiore a zero o non è intero!")
    

class IntG1900(int):
    # Tipo di dato Intero > 1900

    def __new__(cls, v: int | float | str | bool | Self) -> Self:
        # Invoco il metodo new della superclasse, che è 'integer'
        n: int = super().__new__(cls, v)

        if n > 1900:
            return n

        raise ValueError(f"Il numero inserito {v} non è superiore a '1900' o intero!")