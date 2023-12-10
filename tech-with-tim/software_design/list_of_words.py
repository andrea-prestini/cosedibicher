# Program Goal: print a list of words delimited by comas


list_of_words = ["uno", "due", "tre", "quattro", "cinque"]

print("soluzione INDICI")
print(list_of_words[0] + "." +
      list_of_words[1] + "." +
      list_of_words[2] + "," +
      list_of_words[3] + "," +
      list_of_words[4])

print("-" * 50)

print("soluzione FOR")
to_print = ""
for i in range(5):
    to_print += list_of_words[i]
    if i != 4:
        to_print += ","
print(to_print)

print("-" * 50)

print("Soluzione JOIN con carattere")
print(",".join(list_of_words))

print("-" * 50)

print("Soluzione JOIN con COSTANTE")
DELIMITER = ","
print(DELIMITER.join(list_of_words))
