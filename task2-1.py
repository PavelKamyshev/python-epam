def is_palindrome(string):
    string = string.lower().replace(' ', '')
    rev_string = ''.join(reversed(string))

    return string == rev_string

my_str = input("Введите строку: ")
print('YES' if is_palindrome(my_str) else 'NO')
