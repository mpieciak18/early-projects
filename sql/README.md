Welcome to my sub-repository of SQL files.

Thus far, everything has been sourced from the "projects" portion of Khan Academy's "Intro to SQL: Querying and Managing Data" course by Pamela Fox. [You can find her course here.](https://www.khanacademy.org/computing/computer-programming/sql)

This course and its projects uses SQLite as its implementation of SQL.

Here's a quick summary of each file:

### authors_books.sql

This file contains a sample of data pertaining to a few fitness authors (as one table) and their publications (as another). The tables not only relate to each other, but the publications table relates its own entries to each other by way of sequel titles to original titles. Queries are made to look at the titles & their authors, the titles & their sequels, and authors + titles + sequels

### app_impersonator.sql

This file seeks to emulate any particular app (in this case, a food diary app) by creating a table for rows to be entered. After a few example rows are entered, one row is updated and another is deleted, both in a "safe" manner that does not risk deleting other database entries.

### world_data.sql

This file contains a data from every country (including population, age, migration, etc.) stored as a table, and queries it for the countries with the min/max of (as well the average of) each column.