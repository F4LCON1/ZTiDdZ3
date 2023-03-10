import base64


ex = "zarzadzanie tozsamoscia i dostepem do zasobow"


def encod_func(s):
    message_bytes = s.encode('ascii')               # zmiana ciagu na typ bytes
    message_b64 = base64.b64encode(message_bytes)   # kodowanie ciagu w typie bytes
    clear_b64 = message_b64.decode('ascii')         # zmiana zakodowanego ciagu w typie bytes na string

    return clear_b64


def decode_func(s):
    encoded_bytes = s.encode('ascii')                   # kodowanie na bytes
    decoded_string = base64.b64decode(encoded_bytes)    # funkcja decode
    clear_string = decoded_string.decode('ascii')       # zmiana na string

    return clear_string


print('Your raw string: {0} ---> Your encode string: {1} Your decode string ---> {2} '.format(ex, encod_func(ex), decode_func(encod_func(ex))))
