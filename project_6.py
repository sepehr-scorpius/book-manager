import json

class Book:
    Available = True
    num_book = 0
    try:
        with open("library.json") as f:
            library = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        library = {"Books": {}} 

    def __init__(self, title, author, year, rating):
        self.title = title
        self.author = author
        self.year = year
        self.rating = rating

        if 0 < rating <= 5:
            Book.num_book += 1
            Book.library["Books"][title] = {  
                "author": author,
                "year": year,
                "rating": rating
            }

            with open("library.json", "w") as f:
                json.dump(Book.library, f, indent=2)
        else:
            print("Invalid rating format (must be 1-5)")
            self.rating = None
            Book.Available = False
    @classmethod
    def b_find(cls, title):
        """Find book by title (direct dictionary access)"""
        if title in cls.library["Books"]:
            print(cls.library["Books"][title])
        else:
            print(f"Book with title '{title}' not found.")
    
    @classmethod
    def view_all(cls):
        """Print all books in a readable format"""
        if not cls.library["Books"]:  
            print("No books in the library yet!")
            return
        
        print("\n=== ALL BOOKS IN LIBRARY ===")
        for title, details in cls.library["Books"].items():
            print(f"\nTitle: {title}")
            print(f"Author: {details['author']}")
            print(f"Year: {details['year']}")
            print(f"Rating: {details['rating']}/5")
        print("\n=== END OF CATALOG ===")

    @classmethod
    def delete_by_title(cls, title):
        """Delete a book by its title (case-sensitive)"""
        if title in cls.library["Books"]:
            del cls.library["Books"][title]  
            with open("library.json", "w") as f:
                json.dump(cls.library, f, indent=2)  
            print(f"Book '{title}' deleted successfully.")
            cls.num_book -= 1  
        else:
            print(f"Book '{title}' not found - cannot delete.")

