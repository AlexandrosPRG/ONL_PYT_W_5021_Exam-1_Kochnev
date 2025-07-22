from exam_lib import Book
# klasický book v exam_lib.py

class EBook(Book):
    def __init__(self, title, author, page_count, size, registration_code):
        super().__init__(title, author, page_count)
        self.size = size  # velikost v MB
        self.__registration_code = None  # soukromý atribut
        if EBook.check_code(registration_code):  # ověření platnosti
            self.__registration_code = registration_code
        else:
            self.__registration_code = None

    @staticmethod
    def check_code(code):
        return isinstance(code, str) and len(code) == 16 and code.isdigit()
        # jenom cisla a 16 cisel

    @property
    def registration_code(self):
        return self.__registration_code

    @registration_code.setter
    def registration_code(self, value):
        if EBook.check_code(value):
            self.__registration_code = value

ebook1 = EBook("Harry Potter", "J.Rowling", 250, 2, "1234567890123456")
print("EBook 1 - registracni kod:", ebook1.registration_code)

ebook1.registration_code = "1111222233334444"
print("EBook 1 - novej registracni kod:", ebook1.registration_code)

ebook1.registration_code = "Not valid"
print("EBook 2 - spatny registracni kod:", ebook1.registration_code)
