# 1. creating a Readers table (email must be unique)
query_1 = """
CREATE TABLE Readers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(60),
    email VARCHAR(60) UNIQUE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);
"""

# 2. creating a PublishingHouses table
query_2 = """
CREATE TABLE PublishingHouses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(60),
    city VARCHAR(20),
    address VARCHAR(120)
);
"""

# 3. creating a Books table (add an appropriate relationship with the PublishingHouses table
query_3 = """
CREATE TABLE Books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(60),
    price DECIMAL(5,2),
    author VARCHAR(60),
    publishing_houses_id INT REFERENCES PublishingHouses(id)
);
"""

# 4. creating a many-to-many relationship between tables Readers and Books
query_4 = """
CREATE TABLE Readers_Books (
    reader_id INT REFERENCES Readers(id),
    book_id INT REFERENCES Books(id),
    PRIMARY KEY (reader_id, book_id)
);
"""

# 5. retrieving from the database all books with a price greater than 10
query_5 = """
SELECT * FROM Books WHERE price > 10;
"""

# 6. inserting into the PublishingHouses
query_6 = """
INSERT INTO PublishingHouses (name, city, address)
VALUES ('Perfect books', 'Brno', 'Petrinska 20');
"""

# 7. removing the book with id 12
query_7 = """
DELETE FROM Books WHERE id = 12;
"""

# 8. selecting all readers who have ever borrowed a book
query_8 = """
SELECT DISTINCT Readers.*
FROM Readers
JOIN Readers_Books ON Readers.id = Readers_Books.reader_id;
"""

# 9. deactivating the user with id 2
query_9 = """
UPDATE Readers SET is_active = FALSE WHERE id = 2;
"""

# 10. adding an date_of_birth field to the Readers table
query_10 = """
ALTER TABLE Readers ADD COLUMN date_of_birth DATE;
"""
