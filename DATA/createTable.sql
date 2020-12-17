CREATE TABLE "Player" (
	"id"	INTEGER UNIQUE,
	"nom"	TEXT,
	"score"	INTEGER,
	PRIMARY KEY("id")
);

CREATE TABLE "Item" (
	"score"	INTEGER,
	"item"	INTEGER UNIQUE,
	PRIMARY KEY("item")
);