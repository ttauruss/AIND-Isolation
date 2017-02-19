
# Heuristic analysis

The following table summarizes the comparison of the improved heuristic versus student heuristics.

The first heuristic I tried is just an optimization on the improved heuristic. I noticed the redundant call to `get_legal_move` function which can be done only once in heuristic function to speed up the search and increase the depth. The results show no improvement.

Opponent | ID_Improved | Improved_Optimized
------- | ---------- | ---------
Total | 75.71%   | 75.36%
Random | 190/10 | 191/9
MM_Null | 163/37 | 171/29
MM_Open | 148/52 | 145/55
MM_Improved | 141/59 | 132/68
AB_Null | 157/43 | 161/39
AB_Open | 135/65 | 131/69
AB_Improved | 126/74 | 124/76
