SELECT a.ANIMAL_ID, a.NAME
  FROM ANIMAL_INS a
 WHERE a.NAME like '%el%'
   and a.ANIMAL_TYPE = 'Dog'
 ORDER by a.NAME
; 