
"""
subject: Some SQL Script Collections
@author: ywu
"""

/*626. Exchange SeatsUsing flow control statement */
Select Case
        When id%2 = 1 AND id <> (Select max(id) From seat) Then id + 1
        When id%2 = 0 Then id - 1
        Else id End
        As id, student
From seat
Order By id;

/*627.  Using update and Case When (flow control statement) */
Update Salary 
Set
    sex = Case sex
            When 'm' Then 'f'
            Else 'm'
    End;
    	
/* Q1 write a query that shows the top 3 authors who sold the most 
# books in total*/
SELECT authros.author_name, SUM(books.sold_copies) as sum_sold
	FROM authors, books
	WHERE authors.book_name = books.book_name
	GROUP BY authors.author_name
	ORDER BY sum_sold DESC
	LIMIT 3;
	
/*Q2	write a query to find out how many users inserted more than 1000
# but less than 2000 images in their presentations*/
SELECT COUNT(*) FROM 
	(SELECT user_id, COUNT(event_date_time) AS image_per_user
	FROM event_log
	GROUP BY user_id) AS image_per_user
	WHERE image_per_user < 2000 AND image_per_user > 1000;
	
/* Q3 write a query that print every department where the average salary
# per employee is lower than 500*/
SELECT ee.department_name, AVG(ss.salary) AS avg_salary
	FROM employees ee, salaries ss
	WHERE ee.employee_id = ss.employee_id
	AND avg_salary < 500
	GROUP BY ee.department_name;

/* Q1 Given the following data definition, write a query that returns 
# the number of students whose first name is John. */
SELECT count(id)
  FROM students
  WHERE firstName == 'John';
  
/* Q2 A table containing the students enrolled in a yearly course 
# has incorrect data in records with ids between 20 and 100 (inclusive).*/
UPDATE enrollments SET year = 2015
  WHERE id >= 20 AND id <= 100;
  
/* Q3 Write a query that select all distinct pet names.*/
SELECT DISTINCT(dogs.name)
  FROM dogs
UNION
SELECT DISTINCT(cats.name)
  FROM cats;
  
/* Q4 Write a query that selects userId and average 
# session duration for each user who has more than one session.*/
SELECT DISTINCT userId, avg(duration) as avg_session
  FROM sessions
  GROUP BY userId
  HAVING count(userId) > 1;

/* Q5 Write a query that selects the item name and the name of its seller 
# for each item that belongs to a seller with a rating greater than 4. 
# The query should return the name of the item as the first column and 
# name of the seller as the second column.*/
SELECT items.name, sellers.name
  FROM sellers, items
  WHERE sellers.id = items.sellerId
  AND sellers.rating > 4;
  
/* Q6 Write a query that selects the names of employees who are not managers.  */
SELECT name
  FROM employees
  WHERE id not in 
          (SELECT managerId FROM employees WHERE managerId is not Null);

/* Q7 Modify the provided SQLite create table statement so that:
1.Only users from the users table can exist within users_roles.
2.Only roles from the roles table can exist within users_roles.
3.A user can only have a specific role once.*/
CREATE TABLE users_roles (
  userId INTEGER not NULL,
  roleId INTEGER not NULL,
  primary key (UserId, roleId),
  foreign key (userId) references users (id),
  foreign key (roleId) references roles (id)
);

/* output the names of those students whose best friends 
   got offered a higher salary than them */
Select S.Name
From ( Students S join Friends F Using(ID)
       join Packages P1 on S.ID=P1.ID
       join Packages P2 on F.Friend_ID=P2.ID)
Where P2.Salary > P1.Salary
Order By P2.Salary;
