-- Create schema
CREATE SCHEMA test1;
USE test1;

-- Create table Posts, work properly
CREATE TABLE Posts (
Id INT,
PostTypeId TINYINT,
AcceptedAnswerId INT,
ParentId INT,
CreationDate DATETIME,
DeletionDate DATETIME,
Score INT,
ViewCount INT,
Body VARCHAR(800),
OwnerUserId INT,
OwnerDisplayName VARCHAR(40),
LastEditorUserId INT,
LastEditorDisplayName VARCHAR(40),
LastEditDate DATETIME,
LastActivityDate DATETIME,
Title VARCHAR(250),
Tags VARCHAR(250),
AnswerCount INT,
CommentCount INT,
FavoriteCount INT,
ClosedDate DATETIME,
CommunityOwnedDate DATETIME,
PRIMARY KEY (Id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOAD DATA LOCAL INFILE '/Users/Dovla/Downloads/Posts.csv' INTO TABLE Posts
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

SELECT * FROM test1.Posts;
-- DROP TABLE test1.Posts;
