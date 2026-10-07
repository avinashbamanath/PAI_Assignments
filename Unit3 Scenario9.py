import csv
import re

def read_movies(filename):
    movies = []

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                movies.append(row)
    except FileNotFoundError:
        print("Error: movies.csv file not found.")

    return movies

def display_movies(movies):
    if not movies:
        print("No movie records found.")
        return

    print("\n--- All Movie Records ---")

    for movie in movies:
        for key, value in movie.items():
            print(f"{key}: {value}")
        print("-" * 40)

def search_by_id(movies, movie_id):
    found = False

    for movie in movies:
        if movie.get("Movie ID", "").lower() == movie_id.lower():
            print("\n--- Movie Found ---")
            for key, value in movie.items():
                print(f"{key}: {value}")
            found = True
            break

    if not found:
        print("Movie with the given ID was not found.")

def search_by_title(movies, pattern):
    found = False

    try:
        regex = re.compile(pattern, re.IGNORECASE)

        print("\n--- Matching Movies ---")

        for movie in movies:
            title = movie.get("Title", "")

            if regex.search(title):
                for key, value in movie.items():
                    print(f"{key}: {value}")
                print("-" * 40)
                found = True

        if not found:
            print("No movies matched the given pattern.")

    except re.error:
        print("Invalid regular expression.")

def main():
    filename = "movies.csv"
    movies = read_movies(filename)

    while True:
        print("\n===== Movie Collection System =====")
        print("1. Display all movies")
        print("2. Search movie by Movie ID")
        print("3. Search movie by title using Regular Expression")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_movies(movies)

        elif choice == "2":
            movie_id = input("Enter Movie ID: ")
            search_by_id(movies, movie_id)

        elif choice == "3":
            pattern = input("Enter title/search pattern: ")
            search_by_title(movies, pattern)

        elif choice == "4":
            print("Exiting Movie Collection System...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()