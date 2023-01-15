import random


char_lowercase = "abcdefghijklmnopqrstuvwxyz"
char_APPERcase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
char_numbers = "0123456789"
char_specials = "!#$%&'()*+,-./:;<=>?@[}\^_`{|}~"

password = ''


def random_func(seq):                           # funkcja wybiera po 3 znaki z każdego ciagu wyżej, zapisuje je i zwraca
    password_inside = ''
    for i in range(3):
        random_ch = random.choice(seq)
        password_inside += random_ch
    return password_inside


password += random_func(char_lowercase)        # wykorzystanie funkcji na kazdej sekwencji
password += random_func(char_specials)
password += random_func(char_numbers)
password += random_func(char_APPERcase)

password_list = list(password)          # zmiana hasla na typ list aby ponziej użyc go na metodzie shuffle
random.shuffle(password_list)           # losowa zmiana kolejnosci
result = ''.join(password_list)
print(result)

