import csv
import json

input_file = "student.csv"
output_file = "students.json"

students = []

with open(input_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append(row)

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

print("CSV file converted to JSON successfully!")
print("JSON file saved as:", output_file)

"Comment":-
CSV file converted to JSON successfully!
JSON file saved as: students.json
