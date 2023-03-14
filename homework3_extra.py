message = "these are not the droids we are looking for"

alphabet = " abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

output = ""
for letter in message:
    count_of_vowels = alphabet.find(letter)
    line = ("a" * count_of_vowels) + "ncysgqwycxmzpsfhryvbgtnncbbztzzqmwsfqwrtypsdfghklmnbvcxz"
    output += line + "\n"

print(output)
