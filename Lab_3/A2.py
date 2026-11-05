import string

password = input('Введите пароль:')
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
ok = True

if len(password) != 8:
    print("Длина пароля не равна 8")
    ok = False
if password == password.lower():
    print("В пароле отсутствуют заглавные буквы")
    ok = False
if password == password.upper():
    print("В пароле отсутствуют строчные буквы")
    ok = False
if not any(symbol.isdigit() for symbol in password):
    print("В пароле отсутствуют цифры")
    ok = False
if not any(symbol in '*-#' for symbol in password):
    print("В пароле отсутствуют специальные символы")
    ok = False
if not all(symbol in allowed for symbol in password):
    print("В пароле используются непредусмотренные символы")
    ok = False

if ok:
    print("Надежный пароль")
