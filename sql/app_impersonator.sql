/* Assignment: "Think about your favorite apps, and pick one that stores your
data- like a game that stores scores, an app that lets you post updates, etc.
Now in this project, you're going to imagine that the app stores your data in
a SQL database (which is pretty likely!), and write SQL statements that might
look like their own SQL." */

/* App to be impersonated: a food diary app. */

CREATE TABLE food_diary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    food TEXT,
    amount INTEGER,
    measurement TEXT,
    calories INTEGER,
    time TEXT,
    date TEXT
    );

INSERT INTO food_diary (food, amount, measurement, calories, time, date) 
    VALUES ('egg', 250, 'grams', 300, '8:00am', '5/10/2020');
INSERT INTO food_diary (food, amount, measurement, calories, time, date) 
    VALUES ('milk', 2, 'cups', 300, '8:00am', '5/10/2020');
INSERT INTO food_diary (food, amount, measurement, calories, time, date) 
    VALUES ('orange', 300, 'grams', 150, '8:00am', '5/10/2020');
INSERT INTO food_diary (food, amount, measurement, calories, time, date) 
    VALUES ('rye bread', 85, 'grams', 200, '1:00pm', '5/10/2020');
INSERT INTO food_diary (food, amount, measurement, calories, time, date) 
    VALUES ('ham', 200, 'grams', 250, '1:00pm', '5/10/2020');
INSERT INTO food_diary (food, amount, measurement, calories, time, date) 
    VALUES ('cheese', 85, 'grams', 300, '1:00pm', '5/10/2020');
INSERT INTO food_diary (food, amount, measurement, calories, time, date) 
    VALUES ('mayo', 2, 'TBSP', 200, '1:00pm', '5/10/2020');
INSERT INTO food_diary (food, amount, measurement, calories, time, date) 
    VALUES ('tomato', 1, 'small', 25, '1:00pm', '5/10/2020');
INSERT INTO food_diary (food, amount, measurement, calories, time, date) 
    VALUES ('ribeye', 300, 'grams', 600, '7:00pm', '5/10/2020');
INSERT INTO food_diary (food, amount, measurement, calories, time, date) 
    VALUES ('potato', 300, 'grams', 250, '7:00pm', '5/10/2020');
INSERT INTO food_diary (food, amount, measurement, calories, time, date) 
    VALUES ('broccoli', 250, 'grams', 75, '7:00pm', '5/10/2020');
INSERT INTO food_diary (food, amount, measurement, calories, time, date) 
    VALUES ('wine', 1, 'cup', 200, '7:00pm', '5/10/2020');
    
SELECT id, food, amount, measurement, calories FROM food_diary;
SELECT SUM(calories) AS "Today's total caloric intake:" FROM food_diary 
    WHERE date = '5/10/2020';

/* We will safely update a row in food_diary to show that I put less mayo on
my sandwich at lunch than originally indicated. */
SELECT * FROM food_diary WHERE id = 7;
UPDATE food_diary SET amount = 1 WHERE id = 7;
SELECT id, food, amount, measurement, calories FROM food_diary
    WHERE time = '1:00pm';

/* We will safely delete a row in food_diary to show that I did not actually
have any wine for dinner. */
SELECT * FROM food_diary WHERE id = 12;
DELETE FROM food_diary WHERE id = 12;
SELECT id, food, amount, measurement, calories FROM food_diary
    WHERE time = '7:00pm';