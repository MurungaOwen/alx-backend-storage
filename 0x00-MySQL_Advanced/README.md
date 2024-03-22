# Into to sql queries and building tables

## task 0
a SQL script that creates a table users following these requirements:

With these attributes:
id, integer, never null, auto increment and primary key
email, string (255 characters), never null and unique
name, string (255 characters)
If the table already exists, your script should not fail

## task1
a SQL script that creates a table users following these requirements:

With these attributes:
id, integer, never null, auto increment and primary key
email, string (255 characters), never null and unique
name, string (255 characters)
country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
If the table already exists, your script should not fail
Your script can be executed on any database

## task2 
Best band ever!
Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

Requirements:

Import this table dump: metal_bands.sql.zip
Column names must be: origin and nb_fans
Your script can be executed on any database
Context: Calculate/compute something is always power intensive… better to distribute the load

## task 3
 a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

Requirements:

Import this table dump: metal_bands.sql.zip
Column names must be: band_name and lifespan (in years until 2022 - please use 2022 instead of YEAR(CURDATE()))
You should use attributes formed and split for computing the lifespan
Your script can be executed on any database

## task 4 ```triggers```
Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
Quantity in the table items can be negative.

## task 5
Email validation to sent
a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

## task 6
a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

Requirements:
Procedure AddBonus is taking 3 inputs (in this order):
user_id, a users.id value (you can assume user_id is linked to an existing users)
project_name, a new or already exists projects - if no projects.name found in the table, you should create it
score, the score value for the correction

## task 7
a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal

Requirements:

Procedure ComputeAverageScoreForUser is taking 1 input:
user_id, a users.id value (you can assume user_id is linked to an existing users)

## task 8
a SQL script that creates an index idx_name_first on the table names and the first letter of name.
Import this table dump: names.sql.zip
Only the first letter of name must be indexed

## task 9
a SQL script that creates an index idx_name_first_score on the table names and the first letter of name and the score.

Requirements:

Import this table dump: names.sql.zip
Only the first letter of name AND score must be indexed

## task 10
SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

## task 11
a SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.

Requirements:

The view need_meeting should return all students name when:
They score are under (strict) to 80
AND no last_meeting date OR more than a month

## task 12
SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

Requirements:

Procedure ComputeAverageScoreForUser is taking 1 input:
user_id, a users.id value (you can assume user_id is linked to an existing users)

## task 13
Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.

Requirements:

Procedure ComputeAverageWeightedScoreForUsers is not taking any input.