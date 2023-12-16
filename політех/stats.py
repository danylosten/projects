def count_letters(text):
    letter_count = {}  
    for char in text:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    sorted_letters = sorted(letter_count.keys())
    for letter in sorted_letters:
        print(f'{letter}: {letter_count[letter]}')

text = input("Введіть текст: ")
text = str.lower(text)
sorted(text)
count_letters(text)
