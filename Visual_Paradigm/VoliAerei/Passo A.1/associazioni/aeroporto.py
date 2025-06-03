from volo import Volo
from città import Città
from arrivo import arrivo
from partenza import partenza
import weakref

class Aeroporto:

    _nome: str # mutabile, noto alla nascita
    _codice: str # <<immutable>>, noto alla nascita 
    _arrivi: dict[Volo, arrivo.link] # mutabile, non noto alla nascita
    _partenze: dict[Volo, partenza.link] # mutabile, non noto alla nascita

    def __init__(self, nome: str, codice: str) -> None:
        self.set_nome(nome)
        self._codice = codice 
        self._arrivi: dict[Volo, arrivo._link] = dict()
        self._partenze: dict[Volo, partenza._link] = dict()
        
    def nome(self) -> str:
        return self._nome

    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def codice(self) -> str:
        return frozenset(self._codice)
 
    def arrivi(self) ->frozenset[weakref[arrivo._link]]:
        return frozenset([weakref.ref(l) for l in self._arrivi.values()])
    
    def arrivo(self, v: Volo) -> weakref[arrivo._link]:
        return weakref.ref(self._arrivi[v])
    
    def partenze(self) -> frozenset[weakref[partenza._link]]:
        return frozenset([weakref.ref(l) for l in self._partenze.values()])
    
    def partenza(self, v: Volo) -> weakref[partenza._link]:
        return weakref.ref(self._partenze[v])
    
    def _add_link_arrivo(self, arr: arrivo._link) -> None:
        if arr.aeroporto() is not self:
            raise ValueError("link does not involve me")
        if arr.volo() in self._arrivi:
            raise KeyError(f"Duplicate link ({arr.volo()}, {self}) not allowed")
        self._arrivi[arr.volo()] = arr

    def _remove_link_arrivo(self, arr: weakref.ref[arrivo._link]) -> None:
        if arr().aeroporto() is not self:
            raise ValueError("link does not involve me")
        del self._arrivi[ arr.volo()]

    def _add_link_partenza(self, part: partenza._link) -> None:
        if part.aeroporto() is not self:
            raise ValueError("link does not involve me")
        if part.volo() in self._partenze:
            raise KeyError(f"Duplicate link ({part.volo()}, {self}) not allowed")
        self._partenze[part.volo()] = part

    def _remove_link_partenza(self, part: weakref.ref[partenza._link]) -> None:
        if part.aeroporto() is not self:
            raise ValueError("link does not involve me")
        del self._partenze[ part.volo()]

    def __repr__(self) -> str:
        return f"Aeroporto(nome={self._nome})"
        