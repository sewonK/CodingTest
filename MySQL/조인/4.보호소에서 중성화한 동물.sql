SELECT a.ANIMAL_ID, a.ANIMAL_TYPE, a.NAME
FROM  ANIMAL_INS a
    , ANIMAL_OUTS b
WHERE a.ANIMAL_ID = b.ANIMAL_ID
  and a.SEX_UPON_INTAKE like 'Intact%'
  and ((b.SEX_UPON_OUTCOME like 'Spayed%') or (b.SEX_UPON_OUTCOME like 'Neutered%'))
ORDER by a.ANIMAL_ID
;