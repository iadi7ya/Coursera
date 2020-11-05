## Graph Analytics Applications
<br>

_Correct answers are in **bold**._
<br>

**Question 1**. A graph representing tweets would have only “one type” (e.g. label) of node.

* True

* **False**


**Question 2**. In a network representing the world wide web nodes would likely represent:

* Hyperlinks

* **Webpages**

* Google search terms

* Individual computers


**Question 3**. In a network representing the world wide web edges (or links) would likely represent

* **Hyperlinks**

* Webpages

* Google search terms

* Individual computers


**Question 4**. In an email network, which might reasonably be represented by weight on edges?

* the total number of emails sent by one user in a week

* the total number of people who sent an email in a week

* **average number of emails sent from one user to another in a week**


**Question 5**. A loop in a graph is where:

* when there is a edge from A->B, there is also an edge from B->A.

* where there is a path in some way from a node, through 1 or more other nodes, back to the original node.

* **where there is an edge from a node to itself.**


**Question 6**. An example of a loop in a graph could occur when:

* **Someone emails themself**

* Someone emails a friend who replies

* Someone emails a friend, who emails another friend, who then replies to you


**Question 7**. When trying to represent a relationship between Maria and Julio who have more than one relationship to each other (e.g., tennis partner, co-worker, emergency contact) which of the following would be needed in a graph representing those relationships

* **Multiple edges between Maria and Julio**

* Multiple nodes for each of Maria and Julio, to capture the various relationships

* Separate graphs for each kind of relationship


**Question 8**. In many applications paths (where we go from one node to another without repeating nodes) are more useful than walks (where we can repeat a node when going from one node to another).

* **True**

* False


**Question 9**. Trails (paths without repeated edges) can be interesting in which of the following problem applications?

* An email network tracing frequency of emails from one person to another.

* An email network tracing email replies.

* **Routing to avoid using the same bridge or road.**

* Routing to avoid visiting the same city.


**Question 10**. Suppose we have an email network where the edges of a graph represent the number of emails from one user to another.

If I was going to ask if Maria had sent any emails that (either directly or through forwarding from others) reached Julio, I would ask if:

* **Julio’s node was reachable from Maria node**

* Maria’s node was reachable from Julio’s node


**Question 11**. If I want to find the diameter of a graph, I should start by finding the shortest path between each set of nodes.

* **True**

* False


**Question 12**. What is the diameter of this graph?

* 1

* **2**

* 3


**Question 13**. This question is about "best paths". To find the most discussed email in an email network, would we be looking to minimize a function or maximize a function?

* **Maximize**

* Minimize


**Question 14**. Which are the two kinds of constraints on paths discussed in the video on basic path analytics? (check 2) Hint: remember the example of Amarnath needing to get to work by taking his son to school.

* **Inclusion of nodes and/or edges**

* **Exclusion of nodes and/or edges**

* Directionality


**Question 15**. What are examples of preference constraints in the Google Maps application?

* **Avoid roads under construction**

* **Avoid highways**

* Include son's school


**Question 16**. Which of the statements below is true?

* **Dijsktra's algorithm is computationally inefficient (has high computational complexity).**

* Dijsktra's algorithm is computationally efficient (has low computational complexity).


**Question 17**. In the video on "Inclusion and Exclusion Constraints" we learn that adding constraints can actually make our analysis job easier. For example, when we require that a given node be included on a path, which of the following impacts now make the analysis job easier? (Choose 2)

* Changing the weights on the edges of the graph and/or subgraphs

* **Reduction of the size of the graph**

* **Splitting the task into 2 independent shortest path problems**
