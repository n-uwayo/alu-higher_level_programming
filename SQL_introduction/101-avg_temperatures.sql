-- List average temperatures
SELECT city, AVG(value) AS avg_temp FROM `temperatures` GROUP BY `city` ORDER BY AVG(value) desc;

