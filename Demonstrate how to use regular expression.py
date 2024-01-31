import re
text = "Hello, my email is monishkarthik07@gmail.com, and my phone number is 8614333737."
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'
emails = re.findall(email_pattern, text)
print("Email addresses found:")
for email in emails:
    print(email)
phones = re.findall(phone_pattern, text)
print("\nPhone numbers found:")
for phone in phones:
    print(phone)
