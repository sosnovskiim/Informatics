# объявление функции
def is_palindrome(text):
    text = text.lower()
    res = ''
    i = 0
    while i < len(text):
        if text[i] not in [' ', ',', '.', '!', '?', '-']:
            res += text[i]
        i += 1
    return res == res[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
