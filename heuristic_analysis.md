
# Heuristic analysis

The following table summarizes the comparison of the improved heuristic versus student heuristics.

The first heuristic I tried is just an optimization on the improved heuristic. I noticed the redundant call to `get_legal_move` function which can be done only once in heuristic function to speed up the search and increase the depth. The results show no improvement.

The second try was to do the opposite of what the improved heuristic does - prefer boards with minimum moves for the agent. It wasn't much different from the improved heuristic.

Opponent | ID_Improved | Improved_Optimized | Opposite
------- | ---------- | --------- | -----------
Total | 75.71%   | 75.36% | 71.21%
Random | 190/10 | 191/9 | 182/18
MM_Null | 163/37 | 171/29 | 176/24
MM_Open | 148/52 | 145/55 | 129/71
MM_Improved | 141/59 | 132/68 | 121/79
AB_Null | 157/43 | 161/39 | 153/47
AB_Open | 135/65 | 131/69 | 130/70
AB_Improved | 126/74 | 124/76 | 106/94
