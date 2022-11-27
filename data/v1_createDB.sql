-- on active les cles etrangeres

PRAGMA foreign_keys = ON;

-- TODO 1.3a : Créer les tables manquantes et modifier celles ci-dessous
CREATE TABLE LesSportifsEQ
(
  numSp NUMBER(4),
  nomSp VARCHAR2(20),
  prenomSp VARCHAR2(20),
  pays VARCHAR2(20),
  categorieSp VARCHAR2(10),
  dateNaisSp DATE,
  numEq NUMBER(4),
  CONSTRAINT SP_EQ_PK PRIMARY KEY (numSp, numEq),
  CONSTRAINT SP_CK1 CHECK(numSp > 0),
  CONSTRAINT SP_CK2 CHECK(categorieSp IN ('feminin','masculin')),
  CONSTRAINT SP_CK3 CHECK(numEq > 0)
);

CREATE TABLE LesEpreuves
(
  numEp NUMBER(3),
  nomEp VARCHAR2(20),
  formeEp VARCHAR2(13),
  nomDi VARCHAR2(25),
  categorieEp VARCHAR2(10),
  nbSportifsEp NUMBER(2),
  dateEp DATE,
  CONSTRAINT EP_PK PRIMARY KEY (numEp),
  CONSTRAINT EP_CK1 CHECK (formeEp IN ('individuelle','par equipe','par couple')),
  CONSTRAINT EP_CK2 CHECK (categorieEp IN ('feminin','masculin','mixte')),
  CONSTRAINT EP_CK3 CHECK (numEp > 0),
  CONSTRAINT EP_CK4 CHECK (nbSportifsEp > 0)
);

CREATE TABLE LesInscriptions
(
  numIn NUMBER(3),
  numEp NUMBER(3),
  CONSTRAINT IN_EP_PK PRIMARY KEY (numIn, numEp),
  CONSTRAINT EP_FK FOREIGN KEY (numEp) REFERENCES LesEpreuves(numEp),
  CONSTRAINT IN_CK CHECK (numIn > 0)
);

CREATE TABLE LesResultats
(
  numEp NUMBER(3),
  gold NUMBER(3),
  silver NUMBER(3),
  bronze NUMBER(3),
  CONSTRAINT EP_PK PRIMARY KEY (numEp),
  CONSTRAINT EP_FK FOREIGN KEY (numEp) REFERENCES LesEpreuves(numEp),
  CONSTRAINT GOLD_CK CHECK (gold > 0)
  CONSTRAINT SILVER_CK CHECK (silver > 0)
  CONSTRAINT BRONZE_CK CHECK (bronze > 0)
  CONSTRAINT DIFFERENT_CK CHECK (gold <> bronze and bronze <> silver and gold <> silver)
);

-- TODO 1.4a : ajouter la définition de la vue LesAgesSportifs

CREATE VIEW LesAgesSportifs(numSp, nomSp, prenomSp, pays, categorieSp, dateNaisSp, age)
as
  SELECT numSp, nomSp, prenomSp, pays, categorieSp, dateNaisSp, cast(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', dateNaisSp) as int)
  FROM LesSportifsEQ
;


CREATE VIEW LesNbsEquipiers (numEq, nombreEqupier)
as
  SELECT numEq, COUNT(numEq)
  FROM LesSportifsEQ
  GROUP BY numEq
  HAVING numEq is not null
;

CREATE VIEW ageMoyEq (numEq, age)
as
  WITH ageMoyEq(numEq, age) AS 
  (
    SELECT numEq, cast(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', dateNaisSp) as int) 
    FROM LesSportifsEQ
  ) 
  SELECT numEq,AVG(age)  
  FROM ageMoyEq GROUP BY numEq 
  HAVING numEq in (SELECT gold FROM LesResultats)
;


CREATE VIEW classementPays (pays, gold, silver, bronze)
as
  with paysNum(pays,num) as ( SELECT distinct pays, numEq FROM LesSportifsEQ UNION SELECT pays, numSp FROM LesSportifsEQ ),
  tgoldb(pays, nb) as ( SELECT pays, COUNT(gold) FROM paysNum JOIN LesResultats ON(num = gold) GROUP BY pays ),
  tgold(pays,gold) as (SELECT DISTINCT pays, 0 FROM LesSportifsEQ WHERE pays not in (select pays from tgoldb) UNION select pays, nb FROM tgoldb),
  tsilverb(pays, nb) as ( SELECT pays, COUNT(silver) FROM paysNum JOIN LesResultats ON(num = silver) GROUP BY pays ),
  tsilver(pays,silver) as (SELECT DISTINCT pays, 0 FROM LesSportifsEQ WHERE pays not in (select pays from tsilverb) UNION select pays, nb FROM tsilverb),
  tbronzeb(pays, nb) as ( SELECT pays, COUNT(bronze) FROM paysNum JOIN LesResultats ON(num = bronze) GROUP BY pays ),
  tbronze(pays,bronze) as (SELECT DISTINCT pays, 0 FROM LesSportifsEQ WHERE pays not in (select pays from tbronzeb) UNION select pays, nb FROM tbronzeb)
  SELECT pays, gold, silver, bronze
  FROM tgold JOIN tsilver USING(pays) JOIN tbronze USING(pays)
  ORDER by gold DESC, silver DESC, bronze DESC
;

-- TODO 1.5a : ajouter la définition de la vue LesNbsEquipiers
-- TODO 3.3 : ajouter les éléments nécessaires pour créer le trigger (attention, syntaxe SQLite différent qu'Oracle)
