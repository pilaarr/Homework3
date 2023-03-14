import requests

r = requests.get("https://raw.githubusercontent.com/itb-ie/contest/master/text.txt")
a = r.text

alphabet = " abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

hidden_message = ""
for line in a.splitlines():
    count_of_vowels = 0
    for letter in line:
        if letter in vowels:
            count_of_vowels += 1
    hidden_message += alphabet[count_of_vowels]

print(f"The secret message is: {hidden_message}")

