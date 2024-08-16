from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated book title: {book.title}")
# Expected output: Updated book title: Nineteen Eighty-Four 
