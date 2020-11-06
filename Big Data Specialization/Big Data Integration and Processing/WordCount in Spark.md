## WordCount in Spark
<br>

_Correct answers are in **bold**._
<br>

**Question 1**. What does the following line of code do?

_words = lines.flatMap(lambda line: line.split(“ “))_

* Each word is merged into lines to be counted later.

* Each line in the document is split into various Spark partitions.

* Each word in each line is counted.

* **Each line in the document is split up into words.**


**Question 2**. What does the following line of code imply about the state of partitions before the action is performed?

_words = lines.flatMap(lambda line: line.split(“ “))_

* There is only one single partition containing the full document.

* **Each Spark partition corresponds to a line in the document.**

* Each Spark partition corresponds to a word in the document.


**Question 3**. When the following command is executed, where is the file written and how can it be accessed?

_counts.coalesce(1).saveAsTextFile(‘hdfs:/user/cloudera/wordcount/outputDir’)_

* HDFS and through the system directory with the “cd” terminal command.

* **HDFS and through the “hadoop fs” command.**

* The local file system and through the “hadoop fs” command.

* The local file system and through the directory with the “cd” terminal command.


**Question 4**. What does the number one (1) allow us to do in the following line of code?

_tuples = words.map(lambda word: (word,1))_

* The number represents the number of partitions in charge of keeping track of each word.

* None, completely arbitrary in order to apply an algorithm that requires a tuple.

* The number represents the number of partitions in charge of counting each line.

* **Treat each word with a weight of one during the counting process.**

