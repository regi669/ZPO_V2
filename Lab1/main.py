import os
from faker import Faker
import wikipedia

print(os.getcwd())
print(os.getpid())

os.rmdir('Lab1/test')
os.mkdir('Lab1/test')

faker = Faker()

print(faker.name())  # kom1
print(faker.name())  # kom2
print(faker.address())  # kom3
print(faker.address())  # kom4
print(faker.text())  # kom5

#wikipedia.set_lang('pl')

#print(wikipedia.summary('Python'))

#print(wikipedia.page('Mauritius').url)

#print(wikipedia.page('Galapagos').content)

def czy_przestepny(rok):
    if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
        return True
    else:
        return False

rok = 2021

if czy_przestepny(rok):
    dni_w_miesiacach = [31, 29, 31]
else:
    dni_w_miesiacach = [31, 28, 31]

suma_dni = sum(dni_w_miesiacach[:3])

print("Suma dni pierwszych trzech miesięcy w roku", rok, "wynosi:", suma_dni)


def suma_10_liczb_calkowitych():
    suma = 0
    for x in range(11):
        suma += x
    print(suma)


def iloczyn_10_liczb_calkowitych():
    suma = 1
    for x in range(1, 11):
        suma *= x
    print(suma)


suma_10_liczb_calkowitych()
iloczyn_10_liczb_calkowitych()

def zarobki(ilosc_lat, kwota):
    if ilosc_lat == 0:
        return
    kwota += 0.06 * kwota
    ilosc_lat -= 1
    print(str(ilosc_lat + 1) + '.Rok, Kwota: ' + str(round(kwota, 2)))
    zarobki(ilosc_lat, kwota)


zarobki(3, 1000)
