-- TODO 1.3a : Détruire les tables manquantes et modifier celles ci-dessous
DROP TABLE IF EXISTS LesEpreuves;
DROP TABLE IF EXISTS LesSportifs;
DROP TABLE IF EXISTS LesEquipes;
DROP TABLE IF EXISTS LesInscriptions;
DROP TABLE IF EXISTS LesResultats;
DROP VIEW IF EXISTS LesAgesSportifs;
DROP VIEW IF EXISTS LesNbsEquipiers;
DROP VIEW IF EXISTS ageMoyEq;
DROP VIEW IF EXISTS classementPays;
DROP TRIGGER IF EXISTS TriggerInscriptionNumInsert;
DROP TRIGGER IF EXISTS TriggerInscriptionNumUpdate;
DROP TRIGGER IF EXISTS TriggerInscriptionNumInsertPasse;
DROP TRIGGER IF EXISTS TriggerInscriptionNumUpdatePasse;
DROP TRIGGER IF EXISTS TriggerInscriptionNumDeletePasse;
DROP TRIGGER IF EXISTS TriggerEquipePays;
DROP TRIGGER IF EXISTS TriggerEquipePaysUpdate;
-- TODO 3.3 : pensez à détruire vos triggers !
