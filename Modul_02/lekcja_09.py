# # wprowadzenie do list, deklaracja ich w nawiasach kwadratowych
# fruits = ["mango", "banan", "ananas"]
# print(fruits)
# # rzutowanie na listę i tuplę
# word = "Samuraj"
# print(list(word))
# print(tuple(word))
# word_as_a_list = list(word)
# word_as_a_list[-1] = "i"
# print(word_as_a_list)

##################################################
# values = []
# value = int(input("Podaj liczbę: "))
# values.append(value)
# print(values)
# value = int(input("Podaj liczbę: "))
# values.append(value)
# print(values)
# value = int(input("Podaj liczbę: "))
# values.append(value)
# print(values)
# print(f"Suma liczb w liście wynosi: {sum(values)}")
# print(f"Średnia liczb w liście wynosi: {sum(values) / len(values)}")
# print(f"W liście jest {len(values)} elementów")
##################################################
# usuwanie po nazwie albo indeksie
fruits = ["mango", "banan", "ananas"]
print(fruits)
fruits.remove("mango")
print(fruits)
del fruits[0]
print(fruits)