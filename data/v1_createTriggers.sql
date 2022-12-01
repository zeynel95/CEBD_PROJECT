-- TODO 3.3 Créer un trigger pertinent
-- cree trigger pour foreign key bronze, silver, gold
-- verifier si personne dans equipe meme pays
-- verifier si equipe mis coherent avec type de l'epreuve (si epreeuve duo pas plus de 2 personne dans equipe)


CREATE TRIGGER IF NOT EXISTS  NbLimitSportif
BEFORE INSERT ON LesSportifsEQ
-- FOR EACH ROW
WHEN(numEq NOT NULL)
BEGIN 
    WITH nbTotalEq AS (
        -- pas besoin de COUNT(DISTINCT(numSp))
        SELECT COUNT(numSp)
        FROM LesSportifsEQ 
        WHERE numEq = NEW.numEq
    ), nbLimitEq AS (
        SELECT nbSportifsEp INTO nbLimitEq
        FROM LesEpreuves 
        WHERE numEp = NEW.numEq
    )
    IF nbLimitEq != NULL THEN
        IF nbTotalEq == nbLimitEq THEN
            SELECT RAISE (ABORT, ’Cannot have more sportist in this equipe’); 
        END IF;
    END IF;
END;