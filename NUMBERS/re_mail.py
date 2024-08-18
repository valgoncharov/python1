import re

email_regexp = r"[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"

email_check_pattern = re.compile(email_regexp)

# Valid
print(email_check_pattern.fullmatch('bs@gmail.com'))
print(email_check_pattern.fullmatch('b_s@gmail.com'))
print(email_check_pattern.fullmatch('b.s@gmail.com'))
# Invalid
print(email_check_pattern.fullmatch('@gmail.com'))
print(email_check_pattern.fullmatch('bs@gmailcom'))
print(email_check_pattern.fullmatch('bsgmail.com'))
print(email_check_pattern.fullmatch('bs@gmail.'))
print(email_check_pattern.fullmatch('bs@.com'))


def check_email(email):
    email_regexp = r"[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check_pattern = re.compile(email_regexp)
    validation_result = "valid" if email_check_pattern.fullmatch(
        email) else "not valid"
    return (email, validation_result)


print(check_email('bs@gmail.com'))
print(check_email('b_s@gmail.com'))
print(check_email('b.s@gmail.com'))
# Invalid
print(check_email('@gmail.com'))
print(check_email('bs@gmailcom'))
print(check_email('bsgmail.com'))
print(check_email('bs@gmail.'))
print(check_email('bs@.com'))
