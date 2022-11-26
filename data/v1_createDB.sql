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
  CONSTRAINT SP_PK PRIMARY KEY (numSp),
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
  CONSTRAINT IN_CK CHECK (numIn > 0),
  CONSTRAINT EP_CK CHECK (numEp > 0)
);

CREATE TABLE LesResultats
(
  numEp NUMBER(3),
  gold NUMBER(3),
  silver NUMBER(3),
  bronze NUMBER(3),
  CONSTRAINT EP_PK PRIMARY KEY (numEp),
  CONSTRAINT EP_CK CHECK (numEp > 0)
  CONSTRAINT GOLD_CK CHECK (gold > 0),
  CONSTRAINT SILVER_CK CHECK (silver > 0),
  CONSTRAINT BRONZE_CK CHECK (bronze > 0)
);

-- TODO 1.4a : ajouter la définition de la vue LesAgesSportifs

CREATE VIEW LesAgesSportifs
(
  SELECT numSp, nomSp, prenomSp, pays, categorieSp, dateNaisSp, cast(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', dateNaisSp) as int)  as age
  FROM LesSportifsEQ
);

-- TODO 1.5a : ajouter la définition de la vue LesNbsEquipiers
-- TODO 3.3 : ajouter les éléments nécessaires pour créer le trigger (attention, syntaxe SQLite différent qu'Oracle)
