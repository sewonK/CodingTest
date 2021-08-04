SELECT a.NAME, count(a.NAME) AS count
  FROM ANIMAL_INS a
 GROUP BY a.NAME
 Having count(a.NAME) >= 2
 ORDER BY a.NAME;
