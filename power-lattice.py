'''
https://leetcode.com/discuss/interview-question/5063427/google-onsite-round-2

given a lattice kinda graph where each node is either a torch node that has power 16 or wire node where value is 0,
if power node is connected to wire node, it will transmit power to wire and value would become 15 from 0 (1 value would be lost during transmission), again if this wire node is connected to another wire node then value would become 14 of that node
for eg 16 -> 0 -> 0 would become 15 -> 14 -> 13, unless there is one more torch node ahead, then
16 -> 0 -> 0 -> 16
16 -> 15 -> 14 -> 16
16 -> 15 -> 15 <- 16


nothing was given, I had to tell how the representation would look like, in the end we need to return graph when the power had transmitted from all torch nodes to expected wire nodes. And graph in kinda lattice, like a cube (3 d).


I represented graph using unordered_map<node, vector>
where node is (block, data){
this.block = block
this.data = data
}

the representation would look something like


{
[{a,16}] = [{b,10}]
[{b, 0}] = [{f,0}]
[{f,0}] = [{e,16}, {g,0}]
...
}
then given source vertex, we can run bfs and process the nodes, maintaing parent node also
if parent node is 16 then change child value to 15
if parent node is other than 16 then change child value to parent.value - 1

'''

from collections import deque
from typing import List

class Node:
    def __init__(self, val, index, neighbours):
        self.val = val  # Power value (16 for torch nodes, 0 for wire nodes initially)
        self.index = index  # Unique identifier for each node
        self.neighbours = neighbours  # List of indices representing neighbors

    def set_value(self, value):
        self.val = value

def solve(graph: List[Node]) -> List[Node]:
    # Initialize the queue and visited list
    q = deque()
    visited = [False] * len(graph)

    # Add all nodes with val = 16 to the queue
    for node in graph:
        if node.val == 16:
            q.append(node)

    # Perform BFS to propagate power
    while q:
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            if visited[node.index]:
                continue
            visited[node.index] = True

            # Check each neighbor of the current node
            for neighbour_index in node.neighbours:
                neighbour_node = graph[neighbour_index]
                if not visited[neighbour_node.index]:
                    # Update the power of the neighboring node if it's less than the current node's power - 1
                    if neighbour_node.val < node.val - 1:
                        neighbour_node.set_value(node.val - 1)
                    q.append(neighbour_node)

    return graph
