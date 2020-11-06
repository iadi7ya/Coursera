## More on Spark
<br>

_Correct answers are in **bold**._
<br>


**Question 1**. Which part of SPARK is in charge of creating RDDs?

* Spark Executor

* Local CPU

* Worker Node

* **Driver Program**

* Storage


**Question 2**. How does lazy evaluation work in Spark?

* **Transformations are not executed until the action stage.**

* Transformations are queued and executed at a certain threshold.

* Actions are not executed until the transformation stage.

* Actions are queued and executed at a certain threshold.


**Question 3**. What are the consequences of lazy evaluation as mentioned in lecture?

* There are no consequences.

* **Errors sometimes do not show up until the action stage.**

* Hiccups within the system during queue execution.


**Question 4**. What is a wide transformation?

* The name for the most used transformations.

* **A transformation that requires data shuffling across node partitions.**

* Transformations that take a lot of nodes to complete.

* A longer time-taking transformation compared to narrow transformations.


**Question 5**. Where does the data for each worker node get sent to after a collect function is called?

* **Spark Context**

* Spark Streaming

* Other Worker Nodes

* None; Stays in the Same Node

* Spark SQL


**Question 6**. What are DataFrames?

* **A column like data format that can be read by Spark SQL.**

* A type of narrow transformation.

* A special type of data node that contains framework to manipulate SQL.


**Question 7**. Can RDD's be converted into DataFrames directly without manipulation?

* **No: lines have to be converted into row.**

* No: RDD’s needed to be made relational first.

* No: RDD’s cannot be converted into DataFrames.

* Yes


**Question 8**. What is the function of Spark SQL as mentioned in lecture? (Choose 3)

* Better worker node interpolation.

* Efficient data manipulation using SQL like structure.

* **Deploy business intelligence tools over Spark.**

* **Enables relational queries on Spark.**

* **Connect to variety of databases.**

* Better ability to manipulate big data.


**Question 9**. What is a triplet in GraphX?

* A type of data to contain vertex info.

* A type of data to contain edge info.

* A type of data to contain both edge and vertex info.

* **A type of data to contain the information on connections between vertices and edges.**
