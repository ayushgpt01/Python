import re

email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
password_pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d$")
email = 'abc@mail.com'
password = 'kidwarser9'

check_mail = email_pattern.fullmatch(email)
print(check_mail)
check_password = password_pattern.fullmatch(password)
print(check_password)