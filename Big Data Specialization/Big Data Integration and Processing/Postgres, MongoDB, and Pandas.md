## Postgres, MongoDB, and Pandas
<br>

_Correct answers are in **bold**._
<br>


**Question 1**. This quiz encompasses data and content from Week 1 and 2, so we recommend reviewing that material from last week for this quiz as well. What is the highest level that the team has reached in gameclicks? (Hint: use the MAX operation in postgres).


* **8**

* 7

* 9

* 6

* 10


**Question 2**. How many user id's (repeats allowed) have reached the highest level as found in the previous question? (Hint: For postgres: you may either use two queries or use a sub-query).

* 67271

* 106436

* 98823

* **51294**

* 122757


**Question 3**. How many user id’s (repeats allowed) reached the highest level in game-clicks and also clicked the highest costing price in buy-clicks? Hint: Refer to question 4 for ideas.

* 73226

* **32747**

* 23301

* 66887


**Question 4**. What does the following line of code do in postgres?

SELECT count(userid) FROM (SELECT buyclicks.userId, teamLevel, price FROM buyclicks JOIN gameclicks on buyclicks.userId = gameclicks.userId) temp WHERE price=3 and teamLevel=5;

* **Finds the total number of user ids (repeats allowed) in buy-clicks that have bought items with prices worth $3 and was in a team with level 5 at some point in time.**

* Counts the users who exists between both gameclicks and buyclicks files.

* Displays the users who have bought items worth $3 and have had a team with level 5.

* This is an invalid line of code, the subquery is not formatted properly.


**Question 5**. In the MongoDB data set, what is the username of the twitter account who has a tweet_followers_count of exactly 8973882?

* Autocenterit

* **FIFAcom**

* CreateImga

* SasSpear
