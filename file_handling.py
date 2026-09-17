file = open("student.txt", "w")

file.write("Name: avinash\n")
file.write("Course: B.Tech CSE\n")
file.write("Year: Second Year\n")

file.close()

print("Data written successfully.")

file = open("student.txt", "r")

data = file.read()

print("\nFile Content:")
print(data)

file.close()

file = open("student.txt", "a")

file.write("Subject: Advanced Python\n")

file.close()

print("Data appended successfully.")

file = open("student.txt", "r")

print("\nUpdated File Content:")
print(file.read())

file.close()
