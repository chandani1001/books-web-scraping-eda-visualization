import requests
from bs4 import BeautifulSoup
import csv


# Step 1: Define a function to scrape books from a page
# Type: Function
# Input: URL of the page
# Output: List of book dictionaries

def get_books_from_page(url):
    """Scrapes all books from a single page and returns a list of dictionaries"""
    try:
        r = requests.get(url)  # Step 1.1: Send GET request to URL
        r.raise_for_status()   # Step 1.2: Check if request was successful
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return []

    # Step 1.3: Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(r.content, 'html.parser')

    # Step 1.4: Find all book containers
    book_containers = soup.find_all('article', class_='product_pod')

    books = []
    # Step 1.5: Extract book details
    for book in book_containers:
        title = book.h3.a.get('title', 'N/A')  # Step 1.5.1: Book title
        price_tag = book.find('p', class_='price_color')
        price = price_tag.text if price_tag else 'N/A'  # Step 1.5.2: Book price
        rating = book.p.get('class')[1] if book.p and len(book.p.get('class', [])) > 1 else 'N/A'  # Step 1.5.3: Rating
        availability_tag = book.find('p', class_='instock availability')
        availability = availability_tag.text.strip() if availability_tag else 'N/A'  # Step 1.5.4: Availability

        # Step 1.6: Append book dictionary to list
        books.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

    return books


# Step 2: Define a function to save books to CSV
# Type: Function
# Input: List of book dictionaries, CSV filename
# Output: CSV file

def save_books_to_csv(books, filename='books.csv'):
    """Saves a list of book dictionaries to a CSV file"""
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Title', 'Price', 'Rating', 'Availability'])
        writer.writeheader()           # Step 2.1: Write CSV header
        writer.writerows(books)       # Step 2.2: Write book data
    print(f"Data successfully saved to {filename}")


# Step 3: Main execution
# Type: Script

if __name__ == "__main__":
    url = "https://books.toscrape.com/"  # Step 3.1: Target URL
    books = get_books_from_page(url)      # Step 3.2: Scrape books
    save_books_to_csv(books)              # Step 3.3: Save to CSV
