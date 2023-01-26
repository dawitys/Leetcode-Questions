# Write your MySQL query statement below
SELECT firstName, lastName, city, state from Person LEFT JOIN Address on Person.PersonId = Address.PersonId