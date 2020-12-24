---
description: >-
  This section introduces the basic and useful terminology that will be followed
  throughout this series.
---

# Terminology

## **Graph**

A graph can be represented in terms of it's vertices and edges. A graph G = \(V, E\) consists of V, a nonempty set of vertices \(or nodes\) and E, a set of edges. 

## Edge

We can think of an edge in a graph as a kind of relation between two nodes or vertices. If two nodes have an between them then there is some sort of relation between them.  
Each edge has either one or two vertices associated with it, called its endpoints. An edge is said to connect its endpoints.

For example, If there is a road that connects city A and city B, then we can say that there is an edge **\(A,B\)** between node A and node B in it's graph representation.



![Edge between nodes A and B.](https://documents.lucid.app/documents/df5c23af-3428-463b-86df-287bf175faf0/pages/EN8Z4Yltz-~_?a=363&x=378&y=-547&w=484&h=154&store=1&accept=image%2F*&auth=LCA%202f87943b7869770a24d135d1662a4eb1c7c8cd4f-ts%3D1608800448)

### Types of Edges 

There are two types of edges, they are  :

{% tabs %}
{% tab title="Directed Edge   " %}
A directed edge as the suggests has a direction, we should specify it's starting point and ending point.   
We say that there is a directed edge **from** A **to** B,  if it's starting point \( tail \) is A, and ending point \( head\) is B. We generally represent these types of edges with a directed arrow \( -------&gt; \). 



![](https://documents.lucid.app/documents/df5c23af-3428-463b-86df-287bf175faf0/pages/EN8Z4Yltz-~_?a=390&x=378&y=-547&w=484&h=154&store=1&accept=image%2F*&auth=LCA%208e02c15b48f01468f28fe1cfb1a5936fa7a323f2-ts%3D1608800448)

{% hint style="warning" %}
**There is an edge from A to B, doesn't not necessarily mean that there's also an edge from B to A.**
{% endhint %}
{% endtab %}

{% tab title="Undirected Edge" %}
An undirected edge has no direction. We say that two nodes are connected by or there's an edge **between** two nodes when they are connected by an undirected edge. We represent an undirected edge with a blank line.



![Undirected edge between A and B](https://documents.lucid.app/documents/df5c23af-3428-463b-86df-287bf175faf0/pages/EN8Z4Yltz-~_?a=398&x=441&y=-546&w=418&h=132&store=1&accept=image%2F*&auth=LCA%20b77da5a276a3520bf45c4f6a887a87654101211d-ts%3D1608800448)
{% endtab %}
{% endtabs %}

{% hint style="success" %}
* A graph is said to be an undirected graph if all the edges connecting it's nodes are undirected.
* A graph is said to be a directed graph if all the edges connecting it's nodes are directed.
* Node B is adjacent to A if there's an edge from A to B.
* Two nodes are adjacent to each other if there's an edge between them.
{% endhint %}



