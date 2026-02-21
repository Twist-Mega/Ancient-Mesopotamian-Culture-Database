/*Michael Randazzo, May 3rd 2025*/
CREATE SCHEMA MESOPOTAMIA_INFO;
USE MESOPOTAMIA_INFO;

CREATE TABLE DEITIES (
Name VARCHAR(50) NOT NULL, 
Description TEXT, 
Desc_writer VARCHAR(50),

PRIMARY KEY(Name)
);

CREATE TABLE DEITY_TAGS (
Deity_name VARCHAR(50) NOT NULL,
Tag_name VARCHAR(25) NOT NULL,

PRIMARY KEY(Deity_name, Tag_name),
FOREIGN KEY(Deity_name) REFERENCES DEITIES(Name)
);

CREATE TABLE ASPECTS_OF (
Deity_name VARCHAR(50) NOT NULL,
Aspect_name VARCHAR(50) NOT NULL,

PRIMARY KEY(Deity_name, Aspect_name),
FOREIGN KEY(Deity_name) REFERENCES DEITIES(Name),
FOREIGN KEY(Aspect_name) REFERENCES DEITIES(Name)
);

CREATE TABLE REGIONS (
Modern_equivalent VARCHAR(50),
Name VARCHAR(50) NOT NULL, 
Description TEXT,

PRIMARY KEY(Name)
);

CREATE TABLE LANGUAGES (
Name VARCHAR(50) NOT NULL, 
Description TEXT,

PRIMARY KEY(Name)
);

CREATE TABLE LANGUAGE_FOUND_IN (
Region_name VARCHAR(50) NOT NULL,
Lang_name VARCHAR(50) NOT NULL,

PRIMARY KEY(Region_name, Lang_name),
FOREIGN KEY(Region_name) REFERENCES REGIONS(Name),
FOREIGN KEY(Lang_name) REFERENCES LANGUAGES(Name)
);

CREATE TABLE RELIGIOUS_TEXTS (
Title VARCHAR(100), 
Content TEXT,
Designation VARCHAR(20) NOT NULL,
Lang_name VARCHAR(50) NOT NULL,

PRIMARY KEY(Designation),
FOREIGN KEY(Lang_name) REFERENCES LANGUAGES(Name)
);

CREATE TABLE GLYPHS (
Name VARCHAR(50), 
Unicode_no VARCHAR(50) NOT NULL,
Appearance TEXT,
Description TEXT,
Lang_name VARCHAR(50) NOT NULL,

PRIMARY KEY(Unicode_no),
FOREIGN KEY(Lang_name) REFERENCES LANGUAGES(Name)
);

CREATE TABLE GLYPHS_USED_IN (
Deity_name VARCHAR(50) NOT NULL,
Glyph_code VARCHAR(50) NOT NULL,
Number_of_instances SMALLINT NOT NULL,

PRIMARY KEY(Deity_name, Glyph_code),
FOREIGN KEY(Deity_name) REFERENCES DEITIES(Name),
FOREIGN KEY(Glyph_code) REFERENCES GLYPHS(Unicode_no)
);

CREATE TABLE ARTICLES (
Title VARCHAR(200) NOT NULL,
Journal VARCHAR(80),
Doi VARCHAR(50) NOT NULL,
Content MEDIUMTEXT,

PRIMARY KEY(Title, Doi)
);

CREATE TABLE ARTICLE_ABOUT (
Deity_name VARCHAR(50) NOT NULL,
Article_title VARCHAR(200) NOT NULL,
Article_doi VARCHAR(50) NOT NULL,

PRIMARY KEY(Deity_name, Article_title, Article_doi),
FOREIGN KEY(Deity_name) REFERENCES DEITIES(Name),
FOREIGN KEY(Article_title, Article_doi) REFERENCES ARTICLES(Title, Doi)
);

CREATE TABLE AUTHORS (
Name VARCHAR(50) NOT NULL,
Field_of_study VARCHAR(80),

PRIMARY KEY(Name)
);

CREATE TABLE AUTHOR_WROTE_ARTICLES (
Article_title VARCHAR(200) NOT NULL,
Article_doi VARCHAR(50) NOT NULL,
Author_name VARCHAR(50) NOT NULL,

PRIMARY KEY(Article_title, Article_doi, Author_name),
FOREIGN KEY(Article_title, Article_doi) REFERENCES ARTICLES(Title, Doi),
FOREIGN KEY(Author_name) REFERENCES AUTHORS(Name)
);

CREATE TABLE WORSHIPPED_IN (
Deity_name VARCHAR(50) NOT NULL,
Region_name VARCHAR(50) NOT NULL,

PRIMARY KEY(Deity_name, Region_name),
FOREIGN KEY(Deity_name) REFERENCES DEITIES(Name),
FOREIGN KEY(Region_name) REFERENCES REGIONS(Name)
);

INSERT INTO DEITIES VALUES
	('Inanna', 'Inanna is the ancient Mesopotamian goddess of war, love, and fertility. She is also associated with political power, divine law, sensuality, and procreation. Her primary title is "the Queen of Heaven".', 'Anonymous Wikipedian #1'),
    ('Marduk', 'Marduk is a god from ancient Mesopotamia and patron deity of Babylon. He was a prominent figure in Babylonian cosmology, especially in the Enūma Eliš creation myth.', 'Anonymous Wikipedian #2'),
    ('Baal', 'Name means "Lord" in ancient Semitic languages. Applied to several gods, though sometimes used as a mononnym for Hadad', 'Michael Randazzo'),
    ('Hadad', 'Fertility and storm god in some ancient Semitic cultures. Focal point of the Baal Cycle.', 'Michael Randazzo'),
    ('Ereshkigal', 'Sumerian goddess of the underworld', 'Anonymous Wikipedian #3'),
    ('Gilgamesh', 'Semi-legendary god-king of Uruk. Features in Epic of Gilgamesh, among the oldest proper stories.', 'Michael Randazzo'),
    ('Shaushka', NULL, NULL);
    
INSERT INTO DEITY_TAGS VALUES
	('Inanna', 'War'),
    ('Inanna', 'Venus'),
    ('Gilgamesh', 'King'),
    ('Ereshkigal', 'No cult');
    
INSERT INTO ASPECTS_OF VALUES
	('Inanna', 'Shaushka'),
    ('Baal', 'Hadad');
    
INSERT INTO REGIONS VALUES
	('Iraq','Sumer','Earliest known civilization.'),
    (NULL,'Akkad','Capital of Akkadian empire.'),
    ('Iraq','Babylon','Ancient city-state.'),
    ('Syria','Ugarit','Ancient port city.'),
    ('Turkey','Anatolia',NULL);

INSERT INTO LANGUAGES VALUES
	('Sumerian','One of the oldest known languages.'),
    ('Akkadian','Earliest documented Semitic language.'),
    ('Ugaritic',NULL),
    ('Eblaite',NULL),
    ('Hattic',NULL);
    
INSERT INTO LANGUAGE_FOUND_IN VALUES
	('Sumer', 'Sumerian'),
    ('Ugarit','Ugaritic'),
    ('Anatolia','Hattic');

INSERT INTO RELIGIOUS_TEXTS VALUES
	('Epic of Gilgamesh', '[Epic poem]', 'Tablets 1-12', 'Sumerian'),
    ('Baal Cycle', '[Six tablets of the Cycle of Baal]', 'KTU 1.1-1.6', 'Ugaritic'),
    (NULL,NULL,'CTH 796', 'Hattic'),
    ('The Descent of Inanna','From the great heaven she set her mind on the great below...','ETCSL 1.4.1','Sumerian'),
    ('The Descent of Inanna','[Akkadian version of Inanna underworld myth]','LAOS [UNKNOWN]','Akkadian');
    
INSERT INTO GLYPHS VALUES
	('DINGIR','U+1202D','Star-shaped','Divine signifier','Sumerian'),
    ('Ugaritic lambda','U+1038D','Three downward points','makes l sound','Ugaritic');
    
INSERT INTO GLYPHS_USED_IN VALUES
	('Inanna','U+1202D','1'),
    ('Baal','U+1038D','1'),
    ('Ereshkigal','U+1202D','1');

INSERT INTO ARTICLES VALUES
	('Ishtar of Nineveh Reconsidered','Journal of Cuneiform Studies','10.2307/1360026','Forty years ago, M. Vieyra produced his "prolegomenon" to the study of the goddess Igtar of Nineveh (1957), a deity found not only in Assyria, but across the periphery of cuneiform civilization...'),
    ('The Hittite Gilgamesh',NULL,'10.2307/j.ctvd1c8xx','From the late third millennium BCE on, the adventures of Gilgamesh were well known throughout Babylonia and Assyria...'),
    ('An Unrecognized Synonym of Sumerian sukkal, "vizier"','Zeitschrift für Assyriologie und Vorderasiatische Archäologie','10.1515/zava','Lorem ipsum dolor sit amet...');

INSERT INTO ARTICLE_ABOUT VALUES
	('Inanna','An Unrecognized Synonym of Sumerian sukkal, "vizier"','10.1515/zava'),
    ('Inanna','Ishtar of Nineveh Reconsidered','10.2307/1360026'),
    ('Gilgamesh','The Hittite Gilgamesh','10.2307/j.ctvd1c8xx');

INSERT INTO AUTHORS VALUES
	('Gary Beckman','Hittitology'),
    ('Frans Wiggermann','Assyriology');

INSERT INTO AUTHOR_WROTE_ARTICLES VALUES
	('Ishtar of Nineveh Reconsidered','10.2307/1360026','Gary Beckman'),
    ('An Unrecognized Synonym of Sumerian sukkal, "vizier"','10.1515/zava','Frans Wiggermann'),
    ('The Hittite Gilgamesh','10.2307/j.ctvd1c8xx','Gary Beckman');
    
INSERT INTO WORSHIPPED_IN VALUES
	('Inanna','Sumer'),
    ('Shaushka','Anatolia'),
    ('Marduk','Babylon'),
    ('Inanna','Akkad');
    
SELECT * FROM DEITY_TAGS;
SELECT * FROM WORSHIPPED_IN;
SELECT * FROM ASPECTS_OF;
SELECT * FROM GLYPHS_USED_IN;
SELECT * FROM REGIONS;
SELECT * FROM  DEITIES;