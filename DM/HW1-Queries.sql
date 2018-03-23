USE test1;
-- (a) return the names of all the students living in Rome;
-- return the names of users who live in Apex, NC
SELECT DisplayName 
FROM Users 
WHERE Location = "Apex, NC";

-- (b) return the names of the professors of the exams passed by John Doe;
-- return the names of Post types of posts created by user 2961 with comment count equal to 0
SELECT DISTINCT t.PostName 
FROM Posts p 
INNER JOIN PostTypes t 
	on p.PostTypeId = t.Id
WHERE p.OwnerUserId = "2961" AND CommentCount = 0;

-- (c) return the names of the professors of the exams passed by John Doe in 2015;
-- return the post types of posts types of posts created by user 2951 after 2009-09-03 11:26:10 and comment comment equal to 0
SELECT DISTINCT t.PostName 
FROM Posts p 
INNER JOIN PostTypes t 
	on p.PostTypeId = t.Id
WHERE p.OwnerUserId = "2961" AND p.CreationDate > "2009-09-03 11:26:10" AND p.CommentCount = 0;

-- (d) return the ID and the birthdate of all the students that have passed at least an exam in 2016;
-- return the display name and id of all users whos posts have answer count greater than 50 and creation date greater than 2009-07-28 09:25:28
SELECT u.DisplayName, u.Id 
FROM Users u 
INNER JOIN Posts p 
	on u.Id=OwnerUserId
WHERE p.AnswerCount > 50 AND p.CreationDate > "2009-07-28 09:25:28";

-- (e) return name and number of CFUs of all the courses that were passed by the students enrolled in 2015;
-- return the comment and text of suggested edits of all posts created by users who registered after 2011-07-27 00:00:00 and have View Count greater than 100
SELECT s.Comment, s.Text 
FROM SuggestedEdits s 
INNER JOIN Posts p 
	on s.PostId=p.Id
INNER JOIN Users u
	on s.OwnerUserId = u.Id
WHERE u.CreationDate > "2011-07-27 00:00:00" AND p.ViewCount > 100;

-- (f) return the names of the professors that have registered exams that were not reserved by students;
-- course edition prof name, exam reservations (does not include), exams
-- return the names of users whos posts do not have suggested edits

SELECT u.DisplayName 
FROM Users u
INNER JOIN Posts p
	on u.Id=p.OwnerUserId
LEFT JOIN SuggestedEdits s
	on p.Id = s.PostId
WHERE  s.OwnerUserId is NULL ;

-- SELECT * 
-- FROM Posts p
-- LEFT JOIN SuggestedEdits s
-- 	on p.Id = s.PostId
-- WHERE s.OwnerUserId is NULL AND p.CreationDate > "2015-06-28 07:14:29";

-- (g) for every student, return the name and the number of exams passed by the student;
-- for every user return display name and number of posts created after 2015
SELECT u.DisplayName,  count(p.Id)
FROM Users u
INNER JOIN Posts p
	on u.Id = p.OwnerUserId
WHERE p.CreationDate > "2015-12-28 07:14:29"
GROUP BY u.DisplayName;
    
-- (h) for every student, return the name and the average grade of the of exams passed by the student;
-- for every user return display name and avg number of answers created after 2015
SELECT u.DisplayName,  avg(p.AnswerCount)
FROM Users u
INNER JOIN Posts p
	on u.Id = p.OwnerUserId
WHERE p.CreationDate > "2015-12-28 07:14:29"
GROUP BY u.DisplayName;

-- (i) for every student, return the name and the number of exams that were reserved but not passed by the student;
-- for every user, return name and number of posts that were submitted but not answered
SELECT u.DisplayName, count(p.Id)
FROM Users u
INNER JOIN Posts p
	on u.Id = p.OwnerUserId
WHERE p.AnswerCount = 0
GROUP BY u.DisplayName;

-- (j) return the professor(s) who registered the maximum number of exams with the maximum grade (either 30 or 30 cum laude).
-- return users who posted maximum number of posts after 2015
SELECT u.DisplayName, count(p.Id)
FROM Users u
INNER JOIN Posts p
	on u.Id = p.OwnerUserId
WHERE p.CreationDate > "2015-01-01 00:00:00"
GROUP BY u.DisplayName
ORDER BY count(p.Id) DESC
LIMIT 2;

SELECT u.DisplayName
FROM Users u
LEFT JOIN Posts p
	on u.Id = p.OwnerUserId
WHERE p.PostTypeId is NULL;

SELECT u.DisplayName
FROM Users u
WHERE u.DisplayName NOT IN
(SELECT DISTINCT u.DisplayName
FROM Users u
INNER JOIN Posts p
	on u.Id = p.OwnerUserId);
