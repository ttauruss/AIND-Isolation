
## Review of paper "Game Tree Searching by Min/Max approximation" by Ronald L. Rivest

The author proposes a technique for searching game trees. His idea is based on minimax algorithm with iterative heuristic.

Minimax algorithm with alpha-beta pruning expands all nodes at each depth level pruning those that won't be selected. When using iterative heuristic we expand one node at a time which can be at any depth level in the tree - thus forming a tree of non-uniform depth. The idea of iterative heuristic is to focus on expanding the node which has the most impact on the root value. The way we chose the node to expand is determined by the penalty function - "good" nodes has lower penalty than "bad" nodes. The author proposes a new way to define the penalty function based on min/max approximation.

Generalized mean values theory states that an approximation of the maximum of a set of values is a p-mean when p approches the infinity and an approximation of the minimum of a set of values is a p-mean when p approches the minus infinity. The difference between the usual min/max function and the one proposed in the paper is that the latter has continuous derivative that the author uses to define the penalty function.


