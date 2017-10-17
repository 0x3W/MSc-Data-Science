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


-- Create table Users, works for now
CREATE TABLE Users (
Id INT,
Reputation INT,
CreationDate DATETIME,
DisplayName VARCHAR(40),
LastAccessDate DATETIME, 
WebsiteUrl VARCHAR(200),
Location VARCHAR(100),
AboutMe LONGTEXT,
Views INT,
UpVotes INT,
DownVotes INT,
ProfileImageUrl VARCHAR(200),
EmailHash VARCHAR(32),
Age INT,
AccountId INT,
PRIMARY KEY (Id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOAD DATA LOCAL INFILE '/Users/Dovla/Downloads/Users.csv' INTO TABLE Users
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

SELECT * FROM Users;

-- Create Table Comments, works for now
CREATE TABLE Comments (
 Id INT,
 PostId INT,
 Score INT,
 Text1 VARCHAR(600),
 CreationDate DATETIME,
 UserDisplayName VARCHAR(30),
 UserId INT,
 PRIMARY KEY  (Id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOAD DATA LOCAL INFILE '/Users/Dovla/Downloads/Comments.csv' INTO TABLE Comments
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

SELECT * FROM test1.Comments;
