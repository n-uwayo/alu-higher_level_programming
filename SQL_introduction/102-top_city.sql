-- Display the top 3 cities temperature
SELECT city, AVG(value) AS avg_temp FROM `temperatures` WHERE `month` BETWEEN 7 AND 8 GROUP BY `city` ORDER BY AVG(value) desc LIMIT 3;

