import re

def is_latvia_phone(number):
    pattern = r'^\+371\d{8}$'
    return bool(re.match(pattern, number))

print(is_latvia_phone("+37112345678"))