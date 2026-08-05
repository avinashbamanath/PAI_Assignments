class Email:
    def send(self):
        print("Notification sent via Email")


class SMS:
    def send(self):
        print("Notification sent via SMS")


class WhatsApp:
    def send(self):
        print("Notification sent via WhatsApp")


class Notification:
    def __init__(self, service):
        self.service = service

    def notify(self):
        self.service.send()


print("Select Notification Service")
print("1. Email")
print("2. SMS")
print("3. WhatsApp")

choice = int(input("Enter Choice: "))

if choice == 1:
    notification = Notification(Email())
elif choice == 2:
    notification = Notification(SMS())
elif choice == 3:
    notification = Notification(WhatsApp())
else:
    print("Invalid Choice")
    exit()

notification.notify()

"""
Select Notification Service
1. Email
2. SMS
3. WhatsApp
Enter Choice: 1
Notification sent via Email
"""