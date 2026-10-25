
class Book:

    def __init__(self, title, author, price, copies):
        self.title = title
        self.author = author
        self.price = price
        self.copies = copies
    def calculate_stock_value(self):
        return self.price * self.copies

    def check_stock(self):
        if self.copies > 0:
            return "In Stock"
        else:
            return "Out of Stock"

book1 = Book("Python Basics", "John Simiyu", 1200, 5)

book2 = Book("Database Systems", "Mary Mueni", 2500, 0)

print("BOOK 1")
print("Title:", book1.title)
print("Author:", book1.author)
print("Stock Value:", book1.calculate_stock_value())
print("Availability:", book1.check_stock())

print("----------------------")
print("BOOK 2")
print("Title:", book2.title)
print("Author:", book2.author)
print("Stock Value:", book2.calculate_stock_value())
print("Availability:", book2.check_stock())
