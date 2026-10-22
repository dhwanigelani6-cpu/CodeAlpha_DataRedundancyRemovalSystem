
import re


def validate_record(name, email, phone):
    name = name.strip()
    email = email.strip().lower()
    phone = phone.strip()

    if not name or not email or not phone:
        return False, "Please fill in all fields."

    if not re.fullmatch(r"[A-Za-z][A-Za-z .'-]{1,79}", name):
        return False, "Enter a valid name (at least 2 characters)."

    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        return False, "Enter a valid email address."

    if not re.fullmatch(r"[0-9+\-\s()]{7,20}", phone):
        return False, "Enter a valid phone number."

    return True, (name, email, phone)
