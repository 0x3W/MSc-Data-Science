-- Create schema
CREATE SCHEMA test2;
USE test2;

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
CommunityOwnedDate DATETIME
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOAD DATA LOCAL INFILE '/Users/Dovla/Downloads/Posts.csv' INTO TABLE Posts
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

SELECT * FROM test2.Posts;
-- DROP TABLE test2.Posts;

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
AccountId INT
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

SELECT * FROM test2.Comments;

-- Create Table Badges, works for now
CREATE TABLE Badges (
 Id INT, 
 UserId INT, 
 Name VARCHAR(40), 
 Date DATETIME, 
 Class TINYINT, 
 TagBased BIT,
 PRIMARY KEY  (Id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOAD DATA LOCAL INFILE '/Users/Dovla/Downloads/Badges.csv' INTO TABLE Badges
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

SELECT * FROM test2.Badges;

-- Create Table PostTags, works for now
CREATE TABLE PostTags (
 PostId INT,
 TagId INT,
  PRIMARY KEY (PostId)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOAD DATA LOCAL INFILE '/Users/Dovla/Downloads/PostTags.csv' INTO TABLE PostTags
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

SELECT * FROM test2.PostTags;

-- Create Table PostTypes, works for now
CREATE TABLE PostTypes (
  Id TINYINT UNSIGNED NOT NULL,
  PostName VARCHAR(50) NOT NULL,
  PRIMARY KEY  (Id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOAD DATA LOCAL INFILE '/Users/Dovla/Downloads/PostTypes.csv' INTO TABLE PostTypes
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

SELECT * FROM test2.PostTypes;

-- Create Table Tags, works for now
CREATE TABLE Tags (
 Id INT,
 TagName VARCHAR(30),
 Count INT,
 ExcerptPostId INT,
 WikiPostId INT,
 PRIMARY KEY (Id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOAD DATA LOCAL INFILE '/Users/Dovla/Downloads/Tags.csv' INTO TABLE Tags
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

SELECT * FROM test2.Tags;


-- Create Table Votes, works for now
CREATE TABLE Votes (
 Id INT, 
 PostId INT, 
 VoteTypeId TINYINT, 
 UserId INT,  
 CreationDate DATETIME, 
 BountyAmount INT,
 PRIMARY KEY  (Id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOAD DATA LOCAL INFILE '/Users/Dovla/Downloads/Votes.csv' INTO TABLE Votes
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

SELECT * FROM test2.Votes;

-- Create Table SuggestedEdits, works for now
CREATE TABLE SuggestedEdits (
 Id INT, 
 PostId INT, 
 CreationDate DATETIME, 
 ApprovalDate DATETIME,  
 RejectionDate DATETIME, 
 OwnerUserId INT, 
 Comment VARCHAR(800), 
 Text VARCHAR(800), 
 Title VARCHAR(250), 
 Tags VARCHAR(250), 
 RevisionGUID CHAR(50) NOT NULL,
 PRIMARY KEY  (Id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOAD DATA LOCAL INFILE '/Users/Dovla/Downloads/SuggestedEdits.csv' INTO TABLE SuggestedEdits
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

SELECT * FROM test2.SuggestedEdits;