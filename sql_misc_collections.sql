"""
subject: Some SQL Script Collections
"""
/*626. Exchange Seats - using flow control statement */
Select Case
        When id%2 = 1 AND id <> (Select max(id) From seat) Then id + 1
        When id%2 = 0 Then id - 1
        Else id End
        As id, student
From seat
Order By id;

/*626. Exchange Seats - using update and Case When (flow control statement) */
Update Salary 
Set
    sex = Case sex
            When 'm' Then 'f'
            Else 'm'
    End;
	
/*175. Swap Salary - using Left Join statement */	
Select Person.FirstName, Person.LastName, Address.City, Address.State
From Person Left Join Address
On Person.PersonId = Address.PersonId;
	
/*176. Second Highest Salary - using subquery  */	
Select max(Salary) as 'SecondHighestSalary'
From Employee
Where Salary != (Select max(em.Salary) From Employee em);

/*176. Second Highest Salary - using subquery and LIMIT clause */	
SELECT
(SELECT DISTINCT Salary 
    FROM Employee 
    ORDER BY Salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;

/*177. Nth Highest Salary - using subquery and LIMIT clause */	
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
Declare Var Int;
Set Var = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      Select distinct(Salary)
      From Employee
      Order by Salary Desc
      Limit 1 Offset Var
  );
END	

/*178. Rank Scores - using Dense_Rank() Over Clause */	
Select score,
       Dense_Rank() Over (Order By score DESC) as 'Rank'
From Scores;

/*180. Consecutive Numbers - using distinct where clause with multiple tables */
Select DISTINCT l1.Num as 'ConsecutiveNums'
From Logs l1, Logs l2, Logs l3
Where l1.id = l2.id + 1 AND l2.id = l3.id + 1
And l1.Num = l2.Num AND l2.Num = l3.Num

/*181. Employees Earning More Than Their Managers - using Where clause */
Select Name as 'Employee'
From Employee
Where ManagerId is not NULL
And Salary > (Select em.Salary From Employee em
                Where em.Id = Employee.ManagerId);
			
/*181. Employees Earning More Than Their Managers - using Where clause with multiple tables */
Select a.Name as 'Employee'
From Employee a, Employee b
Where a.ManagerId = b.Id
And a.Salary > b.Salary;

/*182. Duplicate Emails - using Group By and Having clause */
Select Distinct(Email) From Person Group By Email Having Count(Email) > 1;

/*182. Duplicate Emails - using multiple tables approach */
Select Distinct p1.Email
From Person p1, Person p2
Where p1.Email = p2.Email
And p1.Id <> p2.Id;

/*183. Customers Who Never Order - using NOT In clause	*/
Select Name as 'Customers'
From Customers
Where Id NOT IN (Select CustomerId From Orders);

/*183. Customers Who Never Order - using LEFT JOIN clause	*/
Select Customers.Name as Customers
From Customers Left Join Orders
On Customers.Id = Orders.CustomerId
Where Orders.CustomerId Is NULL;

/*184. Department Highest Salary - using JOIN, In clause */
Select dep.Name as 'Department',
       emp.Name as 'Employee',
       emp.Salary as 'Salary'
From Employee emp, Department dep
Where emp.DepartmentId = dep.Id
And (emp.DepartmentId, emp.Salary) in (Select DepartmentId, MAX(Salary)
                                            From Employee
                           		    GROUP BY DepartmentId);
											
/*196. Delete Duplicate Emails - using multiple tables approach */
Delete p1
From Person p1, Person p2
Where p1.Id > p2.Id
And p1.Email = p2.Email;

/*196. Delete Duplicate Emails - using NOT IN clause */
Delete From Person 
Where Id NOT IN (Select * From 
                  (Select Min(Id) From Person Group by Email) i);

/*197. Rising Temperature - using Datediff, multiple tables approach */
Select w1.id 
From Weather w1, Weather w2
Where w1.Temperature > w2.Temperature
And Datediff(w1.recordDate, w2.recordDate) = 1;

/*Q1 write a query that shows the top 3 authors who sold the most books in total*/
SELECT authros.author_name, SUM(books.sold_copies) as sum_sold
	FROM authors, books
	WHERE authors.book_name = books.book_name
	GROUP BY authors.author_name
	ORDER BY sum_sold DESC
	LIMIT 3;
	
/*Q2 write a query to find out how many users inserted more than 1000
# but less than 2000 images in their presentations*/
SELECT COUNT(*) FROM 
	(SELECT user_id, COUNT(event_date_time) AS image_per_user
	FROM event_log
	GROUP BY user_id) AS image_per_user
	WHERE image_per_user < 2000 AND image_per_user > 1000;
	
/*Q3 write a query that print every department where the average salary
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
