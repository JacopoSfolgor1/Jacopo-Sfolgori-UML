from aeroporto import Aeroporto
from volo import Volo
from typing import Any

class partenza:
    # Associazione a responsabilità doppia
    class _link: 
        _aeroporto: Aeroporto 
        _volo: Volo

        def __init__(self, v: Volo, a: Aeroporto) -> None:
            self._volo: Volo = v 
            self._aeroporto: Aeroporto = a

        def volo(self) -> Volo:
            return self._volo
        
        def aeroporto(self) -> Aeroporto:
            return self._aeroporto
        
        def __hash__(self) -> int:
            return hash((self.volo(), self.aeroporto()))
        
        def __eq__(self, other: Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False
            
            return (self.volo(), self.aeroporto()) == (other.volo(), other.aeroporto())
        
