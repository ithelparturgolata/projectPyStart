# deklaracja tupli numbers w zakresie od 1 do 20
# numbers = tuple(range(1,21))
# wydruk tupli
# print(numbers)
# wydruk tupli od 1 do 11 elementu tupli
# print(f"Wydruk tupli od 0 do 11 elementu: {numbers[:11]}")
# wydruk od 1 do 10 elementu tupli
# print(f"Wydruk tupli od 0 do 10 elementu: {numbers[:10]}")
# wydruk tupli od 1 elementu(czyli :) do 10 (czyli :30) ze skokiem co 3 element(:10:3)
# print(f"Wydruk tupli od 0 do 10 ze skokiem co 3 elementy: {numbers[:10:3]}")
# wydruk ostatniego elementu tupli
# print(f"Wydruk ostatniego elementu: {numbers[-1]}")
# wydruk 3 od konca elemntu tupli
# print(f"Wydruk 3 elementu od konca: {numbers[-3]}")
# wydruk od 3 ostatniego elementow do konca tupli
# print(f"Wydruk od 3 elementu od konca do konca tupli: {numbers[-3:]}")
# wydruk od 5 ostatniego elementu do konca
# print(f"Wydruk od 5 od konca do ostatniego: {numbers[-5:]}")
# wydruk od 5 ostatniego do 3 ostatniego
# print(f"Wydruk od 5 do 3 elementu od konca: {numbers[-5:-3]}")
# wydruk calej tupli od poczatku z krokiem co 3 element
# print(f"Wydruk całej tupli od początku do końca ze skokiem co 3 element: {numbers[::3]}")
# wydruk calej tupli od od konca co 4 element
# print(f"Wydruk całej tupli co czwarty element ale wydruk od końca: {numbers[::-4]}")
# wydruk ilosci elementow tupli
# print(f"Liczba elementów tupli wynosi: {len(numbers)}")
# print(f"Wydruk największej liczby w tupli: {max(numbers)}")
# print(f"Wydruk najmniejsze liczby w tupli: {min(numbers)}")
# print(f"Wydruk sumy liczb w tupli: {sum(numbers)}")
# print(f"Sortowanie tupli od najmniejszej do największej: {sorted(numbers)}")
# print(f"Odwrócone sortowanie tupli: {sorted(numbers, reverse=True)}")
#######################################################################
numbers = tuple(range(12,1025,6))
print(f"Deklaracja tupli od 12 do 1025 z krokiem co 6 liczb: {numbers}")
# print(numbers[:3])
print(f"Wydruk tupli od 0 elementu do 3: {numbers[:3]}")
# print(numbers[-2:-1])
print(f"Wydruk 2 od konca do 1 od konca elementu tupli: {numbers[-2:-1]}")
# print(numbers[4::6])
print(f"Wydruk od 4 elementu do końca ze skokiem co 6 element(liczbę): {numbers[4::6]}")
# print(numbers[-1::-3])
print(f"Wydruk od ostatniego do pierwszego elementu ze skokiem co 3 element(liczbę): {numbers[-1::-3]}")
# len(numbers)
print(f"Wydruk ilości elementów tupli: {len(numbers)}")
average = sum(numbers[-10:]) / len(numbers[-10:])
print(f"Średnia 10 0statnich wartości wynosi: {average}")