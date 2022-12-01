-- TODO 3.3 Créer un trigger pertinent
-- cree trigger pour foreign key bronze, silver, gold
-- verifier si personne dans equipe meme pays
-- verifier si equipe mis coherent avec type de l'epreuve (si epreeuve duo pas plus de 2 personne dans equipe)


-- CREATE TRIGGER IF NOT EXISTS  NbLimitSportif
-- BEFORE INSERT ON LesSportifsEQ
-- -- FOR EACH ROW
-- WHEN(numEq NOT NULL)
-- BEGIN 
--     WITH nbTotalEq AS (
--         -- pas besoin de COUNT(DISTINCT(numSp))
--         SELECT COUNT(numSp)
--         FROM LesSportifsEQ 
--         WHERE numEq = NEW.numEq
--     ), nbLimitEq AS (
--         SELECT nbSportifsEp INTO nbLimitEq
--         FROM LesEpreuves 
--         WHERE numEp = NEW.numEq
--     )
--     IF nbLimitEq != NULL THEN
--         IF nbTotalEq == nbLimitEq THEN
--             SELECT RAISE (ABORT, ’Cannot have more sportist in this equipe’); 
--         END IF;
--     END IF;
-- END;

CREATE TRIGGER IF NOT EXISTS TriggerInscriptionNumInsert
BEFORE INSERT ON LesInscriptions
WHEN (
    NEW.numIn NOT IN (
        SELECT DISTINCT numSp FROM LesSportifs
        UNION 
        SELECT numEq FROM LesEquipes
    )
)
BEGIN 
    SELECT RAISE (ABORT, "Value not a Sportif or an Equpe");
END;
/
CREATE TRIGGER IF NOT EXISTS TriggerInscriptionNumUpdate
BEFORE UPDATE ON LesInscriptions
WHEN (
    NEW.numIn NOT IN (
        SELECT DISTINCT numSp FROM LesSportifs
        UNION 
        SELECT numEq FROM LesEquipes
    )
)
BEGIN 
    SELECT RAISE (ABORT, "Value not a Sportif or an Equpe");
END;
/
CREATE TRIGGER IF NOT EXISTS TriggerInscriptionNumInsertPasse
BEFORE INSERT ON LesInscriptions
WHEN (
    NEW.numEp IN (
        SELECT numEp FROM LesResultats
    )
)
BEGIN 
    SELECT RAISE (ABORT, "Epreuve deja passe");
END;
/
CREATE TRIGGER IF NOT EXISTS TriggerInscriptionNumUpdatePasse
BEFORE UPDATE ON LesInscriptions
WHEN (
    NEW.numEp IN (
        SELECT numEp FROM LesResultats
    )
)
BEGIN 
    SELECT RAISE (ABORT, "Epreuve deja passe");
END;
/
CREATE TRIGGER IF NOT EXISTS TriggerInscriptionNumDeletePasse
BEFORE DELETE ON LesInscriptions
WHEN (
    OLD.numEp IN (
        SELECT numEp FROM LesResultats
    )
)
BEGIN 
    SELECT RAISE (ABORT, "Epreuve deja passe");
END;
/
CREATE TRIGGER IF NOT EXISTS TriggerEquipePays
BEFORE INSERT ON LesEquipes
WHEN (
    WITH NewPays AS (
        SELECT pays FROM LesSportifs WHERE numSp == New.numSp
    ), EquipePays AS (
        SELECT DISTINCT pays FROM LesEquipes JOIN LesSportifs USING(numSp) WHERE numEq == NEW.numEq
    )
    SELECT COUNT(pays) FROM (
        SELECT pays FROM NewPays 
        UNION 
        SELECT pays FROM EquipePays
    )
    ) > 1
    AND
    NEW.numEq IN (SELECT numEq FROM LesEquipes)
BEGIN
    SELECT RAISE (ABORT, "Sportif pas bon pays");
END;
/
CREATE TRIGGER IF NOT EXISTS TriggerEquipePaysUpdate
BEFORE UPDATE ON LesEquipes
WHEN (
    WITH NewPays AS (
        SELECT pays FROM LesSportifs WHERE numSp == New.numSp
    ), EquipePays AS (
        SELECT DISTINCT pays FROM LesEquipes JOIN LesSportifs USING(numSp) WHERE numEq == NEW.numEq
    )
    SELECT COUNT(pays) FROM (
        SELECT pays FROM NewPays 
        UNION 
        SELECT pays FROM EquipePays
    )
    ) > 1
    AND
    NEW.numEq IN (SELECT numEq FROM LesEquipes)
BEGIN
    SELECT RAISE (ABORT, "Sportif pas bon pays");
END;



