SELECT a.ANIMAL_ID
     , a.NAME
     , a.SEX_UPON_INTAKE
  FROM ANIMAL_INS a
 WHERE a.NAME in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
 ORDER by a.ANIMAL_ID
 ;
 