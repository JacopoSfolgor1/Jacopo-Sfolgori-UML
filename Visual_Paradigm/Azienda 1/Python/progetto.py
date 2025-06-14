from custom_types import RealGEZ
from impiegato import Impiegato
from datetime import date

class Progetto:
    _nome: str 
    _budget: RealGEZ 
    _impiegati: dict[Impiegato: date] 

    def __init__(self, nome: str, budget: RealGEZ) -> None:
        self.set_nome(nome)
        self.set_budget(budget)
        self._impiegati: dict[Impiegato: date] = {}

    def nome(self) -> str:
        return self._nome

    def set_nome(self, n: str) -> None:
        self._nome: str = n 

    def budget(self) -> RealGEZ:
        return self._budget
    
    def set_budget(self, b: RealGEZ) -> None:
        self._budget: RealGEZ = b

    def impiegati(self) -> frozenset[tuple[Impiegato, str]]:
       return frozenset((imp, data.strftime(f"data inizio: {'%d/%m/%Y'}")) for imp, data in self._impiegati.items())

    def add_impiegato(self, imp: Impiegato, data_inizio: date) -> None:
        if type(data_inizio) == date and imp not in self._impiegati:
            self._impiegati[imp] = data_inizio
            # self._impiegati.update({imp: data_inizio}) usato maggiormente per più oggetti da aggiungere in una volta
            print(f"Ho aggiunto l'impiegato: {imp} in data: {data_inizio}")
        else:
            raise KeyError(f"Impiegato: {imp} già presente o data di inizio invalida")

    def remove_impiegato(self, imp: Impiegato) -> None:
        if imp in self._impiegati:
            self._impiegati.pop(imp)
            print(f"Ho rimosso l'impiegato: {imp}")
        else:
            raise KeyError(f"Impiegato: {imp} non trovato")
        
    def is_coinvolto(self, imp: Impiegato) -> bool:
        if imp in self._impiegati:
            return True
        return False
    
    def ultimo_impiegato_coinvolto(self) -> Impiegato:
        if self.impiegati():
            imp: Impiegato = max(self._impiegati.items(), key = lambda t: t[1])[0]
            return f"Ultimo impiegato coinvolto:\n {imp}"
        

