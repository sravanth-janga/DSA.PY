# Representation

In order to work with graphs we first should know the way to model and represent a graph. There are many ways to represent a graph. Let's see two of the most common ways to represent a graph.

Let's see how we can represent the following  graph with n nodes numbered from 1 to 4.



![A mixed Graph \( has both directed and undirected edges \).](https://documents.lucid.app/documents/df5c23af-3428-463b-86df-287bf175faf0/pages/EN8Z4Yltz-~_?a=487&x=440&y=-556&w=446&h=352&store=1&accept=image%2F*&auth=LCA%20e542394b8ebcc17c22998615f7db201211afba75-ts%3D1608800448)



{% tabs %}
{% tab title="Adjacency List" %}
We represent the graph using **n** lists \( arrays\) and each list\(array\) corresponds to a **node.**  
The values of a list corresponding to a node are the nodes that are adjacent to the node. The graph shown in the picture can be represented using an adjacency list as follows

Let's consider node 1. There's a from node 1 to node 3, and edge between 1 and 2. So, nodes 3 and 2 are adjacent to the node 1. We put these values \(3, 2\) in the list\(array\) corresponding to node 1. Similarly you can do for other nodes.

| **Node** | **Adjacent Nodes** |
| :---: | :---: |
| 1 | 3, 2 |
| 2 | 1, 3 |
| 3 | 2 |
| 4 | 3 |
{% endtab %}

{% tab title="Adjacency Matrix" %}
We represent a graph with **n** nodes using a **n X n** matrix **M**. If there is an edge from node **i** to node **j** then **M\[i\]\[j\] = 1,** otherwise **M\[i\]\[j\] = 0.** 

The adjacency matrix for the above graph is,  


![Adjacency matrix](https://documents.lucid.app/documents/df5c23af-3428-463b-86df-287bf175faf0/pages/EN8Z4Yltz-~_?a=1464&x=698&y=-1017&w=481&h=382&store=1&accept=image%2F*&auth=LCA%207e559506c7a4f5b0dc4ca41f237e750d7c78e15f-ts%3D1608800448)

{% hint style="warning" %}
In case of a weighted graph replace the value 1 with corresponding weight of that edge.
{% endhint %}
{% endtab %}
{% endtabs %}



