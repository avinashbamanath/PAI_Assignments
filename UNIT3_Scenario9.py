import csv
import re
import os

FILENAME = "movies.csv"

def initialize_csv():
    if not os.path.exists(FILENAME):
        sample_movies = [
            {"Movie ID": "M001", "Title": "Inception", "Genre": "Sci-Fi", "Year": "2010", "Rating": "8.8"},
            {"Movie ID": "M002", "Title": "The Dark Knight", "Genre": "Action", "Year": "2008", "Rating": "9.0"},
            {"Movie ID": "M003", "Title": "Interstellar", "Genre": "Sci-Fi", "Year": "2014", "Rating": "8.7"},
            {"Movie ID": "M004", "Title": "The Prestige", "Genre": "Mystery", "Year": "2006", "Rating": "8.5"},
            {"Movie ID": "M005", "Title": "Dune: Part Two", "Genre": "Sci-Fi", "Year": "2024", "Rating": "8.5"}
        ]
        with open(FILENAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["Movie ID", "Title", "Genre", "Year", "Rating"])
            writer.writeheader()
            writer.writerows(sample_movies)

def read_movies():
    movies = []
    with open(FILENAME, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            movies.append(row)
    return movies

def display_all_movies(movies):
    print("\n--- All Movies ---")
    for movie in movies:
        print(f"ID: {movie['Movie ID']} | Title: {movie['Title']} | Genre: {movie['Genre']} | Year: {movie['Year']} | Rating: {movie['Rating']}")

def search_by_id(movies, movie_id):
    print(f"\n--- Search Result for Movie ID: {movie_id} ---")
    found = False
    for movie in movies:
        if movie["Movie ID"].strip().lower() == movie_id.strip().lower():
            print(f"ID: {movie['Movie ID']} | Title: {movie['Title']} | Genre: {movie['Genre']} | Year: {movie['Year']} | Rating: {movie['Rating']}")
            found = True
            break
    if not found:
        print("Movie not found.")

def search_by_title_regex(movies, pattern):
    print(f"\n--- Regex Search Result for Pattern: '{pattern}' ---")
    try:
        regex = re.compile(pattern, re.IGNORECASE)
        matches = [movie for movie in movies if regex.search(movie["Title"])]
        if matches:
            for movie in matches:
                print(f"ID: {movie['Movie ID']} | Title: {movie['Title']} | Genre: {movie['Genre']} | Year: {movie['Year']} | Rating: {movie['Rating']}")
        else:
            print("No matching movies found.")
    except re.error as e:
        print(f"Invalid regular expression: {e}")

def main():
    initialize_csv()
    movies = read_movies()
    
    while True:
        print("\n=== Movie Collection System ===")
        print("1. Display all movie information")
        print("2. Search movie by Movie ID")
        print("3. Search movies by title (Regex)")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            display_all_movies(movies)
        elif choice == "2":
            m_id = input("Enter Movie ID: ")
            search_by_id(movies, m_id)
        elif choice == "3":
            pattern = input("Enter title regex pattern: ")
            search_by_title_regex(movies, pattern)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
