# объявление функции
def is_pangram(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in alphabet:
        if letter != ' ' and letter not in text:
            return False
    return True


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
