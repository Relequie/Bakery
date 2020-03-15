CREATE TABLE "BakeryItem" (
	"ItemNumber"	INTEGER NOT NULL,
	"Name"	TEXT NOT NULL,
	"ExpiryDate"	TEXT NOT NULL,
	"Type"	TEXT NOT NULL,
	"Price"	INTEGER NOT NULL,
	"Source"	TEXT NOT NULL,
	PRIMARY KEY("ItemNumber")
);

CREATE TABLE "Cake" (
	"ItemNumber"	INTEGER NOT NULL,
	"Country"	TEXT NOT NULL,
	PRIMARY KEY("ItemNumber"),
	FOREIGN KEY("ItemNumber") REFERENCES "BakeryItem"("ItemNumber")
);

CREATE TABLE "Bread" (
	"ItemNumber"	INTEGER NOT NULL,
	"Subtype"	TEXT NOT NULL,
	PRIMARY KEY("ItemNumber"),
	FOREIGN KEY("ItemNumber") REFERENCES "BakeryItem"("ItemNumber")
);

CREATE TABLE "Mooncake" (
	"ItemNumber"	INTEGER NOT NULL,
	"Lard"	INTEGER NOT NULL,
	FOREIGN KEY("ItemNumber") REFERENCES "BakeryItem"("ItemNumber"),
	PRIMARY KEY("ItemNumber")
);