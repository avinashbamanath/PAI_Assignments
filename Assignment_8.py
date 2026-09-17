with open("file.txt", "r") as file:
    lines = file.readlines()

print("Number of lines read:", len(lines))

first_two = lines[:2]

with open("output.txt", "w") as file:
    file.writelines(first_two)

print("Successfully saved the initial two lines into output.txt")
