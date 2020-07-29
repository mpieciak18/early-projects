/* Create tables about authors and their books. */
CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    dob TEXT);
    
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    year TEXT,
    sequel_id INTEGER,
    author_id INTEGER);

/* Create entries for authors table. */
INSERT INTO authors (name, dob) 
    VALUES ("Bill Starr", "01/12/1938");
INSERT INTO authors (name, dob) 
    VALUES ("Mark Rippetoe", "02/12/1956");
INSERT INTO authors (name, dob) 
    VALUES ("Pavel Tsatsouline", 08/23/1969);

/* Create entries for books table. Note: sequels aren't necessarily true. */
INSERT INTO books (title, year, sequel_id, author_id) 
    VALUES ("The Strongest Shall Survive", 1979, 2, 1);
INSERT INTO books (title, year, sequel_id, author_id) 
    VALUES ("Defying Gravity: How to Win at Weighlifting", 1981, NULL, 1);
INSERT INTO books (title, year, sequel_id, author_id) 
    VALUES ("Starting Strength: 1st Ed.", 2005, 4, 2);
INSERT INTO books (title, year, sequel_id, author_id) 
    VALUES ("Starting Strength: 2nd Ed.", 2007, 5, 2);
INSERT INTO books (title, year, sequel_id, author_id) 
    VALUES ("Starting Strength: 3rd Ed.", 2011, 6, 2);
INSERT INTO books (title, year, sequel_id, author_id) 
    VALUES ("Practical Programming: 3rd Ed.", 2014, NULL, 2);
INSERT INTO books (title, year, sequel_id, author_id) 
    VALUES ("Power to the People!", 2000, 8, 3);
INSERT INTO books (title, year, sequel_id, author_id) 
    VALUES ("The Russian Kettlebell Challenge", 2001, 9, 3);
INSERT INTO books (title, year, sequel_id, author_id) 
    VALUES ("The Naked Warrior", 2003, 10, 3);
INSERT INTO books (title, year, sequel_id, author_id) 
    VALUES ("Enter the Kettlebell", 2006, 11, 3);
INSERT INTO books (title, year, sequel_id, author_id) 
    VALUES ("Hardstyle Abs", 2006, 12, 3);
INSERT INTO books (title, year, sequel_id, author_id) 
    VALUES ("Kettlebell Simple and Sinister", 2013, 13, 3);
INSERT INTO books (title, year, sequel_id, author_id) 
    VALUES ("The Quick and the Dead", 2019, NULL, 3);
INSERT INTO books (title, year, sequel_id, author_id) 
    VALUES ("Strong Enough?", 2007, NULL, 2);
INSERT INTO books (title, year, sequel_id, author_id) 
    VALUES ("Mean Ol' Mr. Gravity", 2009, NULL, 2);

/* Queries both tables for book titles and respective author names. */
SELECT books.title, authors.name FROM authors 
    JOIN books 
    ON authors.id = books.author_id
    ORDER BY authors.name;

/* Queries both tables for book titles and respective sequel titles. */   
SELECT a.title, b.title AS sequel FROM books a
    JOIN books b
    ON a.sequel_id = b.id;

/* Queries both tables for book titles, respective sequel titles,
and respective author names. */
SELECT authors.name AS Author, a.title AS Title, a.year AS Year, b.title
    AS Sequel, b.year AS Sequel_Year FROM books a
    JOIN books b
    ON a.sequel_id = b.id
    JOIN authors
    ON authors.id = a.author_id;