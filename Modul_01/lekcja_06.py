# value1 = input("Podaj liczbę 1: ")
# value2 = input("Podaj liczbę 2: ")
# result = value1 + value2
# print(result)
#input standardowo jest stringiem dlatego następuje konkatenacja znaków
#######################################################################
# print("Artur Gołata " * 30)
#pomnożenie stringa i wyświetlenie na ekranie 30 razy Artur ...
#######################################################################
# height = int(input("Podaj swoją wagę: "))
# weight = float(input("Podaj swój wzrost: "))
# bmi = (height / (weight)**2)
# print(f"Twoje BMI wynosi: {bmi:.2f}")
#######################################################################
# value_netto = float(input("Podaj wartość netto: "))
# vat = 1.23
# value_brutto = value_netto * vat
# print(f"Wartość brutto produktu wynosi: {value_brutto}")
#######################################################################
# value_a = float(input("Podaj wartość a: "))
# value_b = float(input("Podaj wartość b: "))
# value_h = float(input("Podaj wartość h: "))
# const = 2
# field = ((value_a + value_a) * value_h / const)
# print(f"Pole trapezu wynosi: {field}")
#######################################################################
# value = int(input("Podaj liczbę: "))
# if value % 2 == 0:
#     print("Liczba parzysta")
# else:
#     print('Liczba nieparzysta')
#######################################################################
# value_1 =int(input("Podaj liczbę 1: "))
# value_2 =int(input("Podaj liczbę 2: "))
# if value_1 > value_2:
#     print(f"Wartość {value_1} jest większa od wartości {value_2}")
# elif value_1 == value_2:
#     print(f"Wartość {value_1} jest równa wartośc {value_2}")
# else:
#     print(f"Wartość {value_2} jest większa od warotści {value_1}")
#######################################################################
# temperature = float(input("Podaj jaka jest temperatura: "))
# if temperature <= 10 :
#     print("Zostań w domu")
# elif temperature > 10 and temperature < 20:
#     print("Weź kurtkę")
# else:
#     print("baw się dobrze")
#######################################################################
# degrees_Celsjusz = float(input("Podaj stopnie w C: "))
# degrees_Fahrenheit = (degrees_Celsjusz * 9 / 5) + 32
# print(f"Temperatura w Fahrenheit'a wynosi: {degrees_Fahrenheit:.2f}")
#######################################################################
value = int(input("Podaj liczbę: "))
if value % 11 == 0 and value % 5 == 0:
    print(f"Liczba {value} jest podzielna przez 5 i 11")
elif value % 11 == 0:
    print(f"Liczba {value} jest podzielna przez 11")
elif value % 5 == 0:
    print(f"Liczba {value} jest podzielna przez 5")
else:
    print(f"Liczba {value} nie jest podzielna przez 5 i 11")
#######################################################################
