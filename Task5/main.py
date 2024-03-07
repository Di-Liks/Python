import re
def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, email):
        return True
    else:
        return False
def get_email_address(email):
    if not email or not isinstance(email, str):
        raise ValueError("Некорректный аргумент. Введите строку с адресом электронной почты.")
    if is_valid_email(email):
        return email
    else:
        raise ValueError("Некорректный адрес электронной почты.")

try:
    user_input = input("Введите адрес электронной почты: ")
    result = get_email_address(user_input)
    print("Введенный адрес электронной почты:", result)
except ValueError as e:
    print(f"Ошибка: {e}")
