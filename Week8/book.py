class Book:
    def __init__(self, title, author, page_amount):
        self.title = title
        self.author = author
        self.page_amount = page_amount

    
    def description(self):
        return f"Het boek {self.title} van {self.author} bevat {str(self.page_amount)} pagina's"

    def add_pages(self, amount):
        self.page_amount += amount


def main():
    #opvragen van title , author en page_amount
    title = input("Naam van het boek: ")
    author = input("Naam van Auteur: ")
    page_amount = int(input("Hoeveel pagina's bevat het boek: "))

    #instantieren en meegeven
    book = Book(title, author, page_amount)

    print(book.description())
    book.add_pages(50)
    print(book.description())


if __name__ == "__main__":
    main()
