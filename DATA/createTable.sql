CREATE TABLE IF NOT EXISTS Player
(
    id    INTEGER UNIQUE,
    nom   TEXT,
    score INTEGER,
    PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS Item
(
    score INTEGER,
    item  varchar(50) UNIQUE,
    PRIMARY KEY ("item")
);

CREATE TABLE IF NOT EXISTS Mobs
(
    couleur varchar(10),
    nom     varchar(10),
    puissance     INTEGER,
    PRIMARY KEY ("nom", "couleur")
);