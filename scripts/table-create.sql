BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Jobs" (
	"JobId"	INTEGER UNIQUE,
	"title"	TEXT,
	"description"	TEXT,
	"roleDescription"	TEXT,
	"keyResponsibilities"	TEXT,
	"requirements"	TEXT,
	"applicants"	INTEGER,
	"pay"	INTEGER,
	"date"	TEXT,
	"time"	TEXT,
	PRIMARY KEY("JobId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Nurses" (
	"NurseId"	INTEGER UNIQUE,
	"Name"	TEXT,
	"Race"	TEXT,
	"Gender"	TEXT,
	"Vaccination_Status"	TEXT,
	"Experience"	TEXT,
	"Specialisation"	TEXT,
	"Postal_Code"	TEXT,
	"Available_Work_Timing"	TEXT,
	"Rating"	TEXT,
	PRIMARY KEY("NurseId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "JobApplications" (
    "NurseId" INTEGER,
    "JobId" INTEGER,
    PRIMARY KEY("NurseId", "JobId"),
    FOREIGN KEY("NurseId") REFERENCES "Nurses"("NurseId"),
    FOREIGN KEY("JobId") REFERENCES "Jobs"("JobId")
);
COMMIT;
