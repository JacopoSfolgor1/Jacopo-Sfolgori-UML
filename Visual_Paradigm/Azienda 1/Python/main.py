from custom_types import *
from datetime import date
from impiegato import Impiegato
from dipartimento import Dipartimento
from progetto import Progetto


tel1: Telefono = Telefono("3334445566")
tel2: Telefono = Telefono("3337778899")
ind: Indirizzo = Indirizzo("Viale Cesare Pavese", "205b",
                           CAP("00144"))

alice: Impiegato = Impiegato("Alice", "Alessi",
                             date(year=1990, month=12, day=31),
                             RealGEZ(18000))
print(f"Ho creato l'impiegata {alice.nome()} {alice.cognome()}")

bob: Impiegato = Impiegato("Bob", "Burnham",
                             date(year=1997, month=10, day=11),
                             RealGEZ(19000))
print(f"Ho creato l'impiegato {bob.nome()} {bob.cognome()}")


dip1: Dipartimento = Dipartimento("Vendite", tel1, ind)

print(f"Ho creato il dipartimento {dip1}")


dip2: Dipartimento = Dipartimento("Acquisti", tel2, None)
print(f"Ho creato il dipartimento {dip2}")

t: frozenset[Telefono] = dip1.telefoni()

print("dip1.telefoni() = " + str(dip1.telefoni()))

dip1.add_telefono(Telefono("3481265413"))

print("dip1.telefoni() = " + str(dip1.telefoni()))


pegaso = Progetto("pegaso", 78000)
biagio = Impiegato("Biagio", "Boh", date(year=1990, month=12, day=31), RealGEZ(123))


#pegaso.add_impiegato(biagio, date.today())


print(pegaso.ultimo_impiegato_coinvolto())


print(pegaso.is_coinvolto(biagio))
print(pegaso.is_coinvolto(alice))

print(pegaso.impiegati())

try:
    pegaso.add_impiegato(biagio, "domani")
except KeyError as e:
    print(e)
    
try:
    pegaso.remove_impiegato(biagio)
except KeyError as e:
    print(e)

try:
    pegaso.remove_impiegato(alice)
except KeyError as e:
    print(e)

