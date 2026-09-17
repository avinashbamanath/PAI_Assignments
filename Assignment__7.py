import re

text = """
Hello everyone!

You can contact us at:
avinash@gmail.com
student123@college.edu
support@example.org
invalid-email@com
hello@domain.co.in

Thank you!
"""

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

emails = re.findall(email_pattern, text)

print("Extracted Emails:")

if emails:
    for email in emails:
        print(email)
else:
    print("0 emails detected.")

print("\nCount of emails:", len(emails))
