from redundancja import Child
from konflikt_nazw import C
from abstrakcja import Abstract,Uchwyt

c= Child()

print("******************")
c = C()
c.hello()

print("******************")
print(C.__mro__)

print("******************")
# a = Abstract() #nie powinno się tworzyc obiektów klasy abstrakcyjnej
u = Uchwyt()

