## SparkSQL and Spark Streaming
<br>

_Correct answers are in **bold**._
<br>


**Question 1**. What does the following filter line of code do?

_df.filter(df[“teamlevel”] > 1)_

* Select the first two columns of the data and filter each column to show only team levels larger than 1.

* **Filter each row to show only team levels larger than 1.**

* Filter each column to show only team levels larger than 1.

* Select the first two columns of the data and displays only team levels greater than 1.


**Question 2**. What does the following do?

_df.select(“userid”, “teamlevel”).show(5)_

* Select the rows named “userid” and “teamlevel” and display first 5 rows.

* Display all rows except “userid” and “teamlevel”.

* Display all columns except “userid” and “teamlevel”.

* **Select the columns named “userid” and “teamlevel” and display first 5 rows.**


**Question 3**. What does the 1 represent in the following line of code?

_ssc = StreamingContext(sc,1)_

* To create only one partition to manage the stream.

* To specific debug output.

* **A batch interval of 1 second.**

* To create one single context.


**Question 4**. What does the following code do?

_window = vals.window(10, 5)_

* Creates 10 windows with 5 batch intervals inbetween.

* **Creates a window that combines 10 seconds worth of data and moves by 5 seconds.**

* Creates a batch interval between 10 seconds and 5 seconds.

* Creates 10 windows with 5 seconds worth of data in them.

