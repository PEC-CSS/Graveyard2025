# RoboCharge Optimization

_**Hey everyone this my approach to solving this problem , hope this helps you understand how the code for this problem is structured , i have provided some in line comments within the code aswell**_
---

## Problem Statement

A futuristic charging station has `N` docks labeled `D₁, D₂, ..., D_N`. Each dock `D_i` has an **optimal charge level** `C_i`. The station can adjust the actual charge levels `P_i` to minimize the **overload factor**, defined as:

Overload Factor = Absolute difference of `C_i` and `D_i`  **_|C_i - D_i|_**

### Constraints:
- The number of **changes** in charge levels between consecutive docks must not exceed `K`. A change occurs if `P_i ≠ P_{i-1}`.
- The goal is to find the **minimum possible overload factor**.

---

## Input/Output Format

### Input:
- The first line contains `T` (number of test cases).
- For each test case:
  - The first line contains two integers: `N` (number of docks) and `K` (max allowed changes).
  - The next line contains `N` integers: the optimal charge levels `C₁, C₂, ..., C_N`.

### Output:
- For each test case, print the minimal overload factor.

---

## Examples

### Example 1:
**Input:**

4

3 0

1 3 3

3 1

1 3 3

4 2

25 40 47 30

5 1

120 100 82 111 74


**Outputs:**  
1

0

4

19  

## Explantions
**Output**
`1`
**Explanation:**  
With `K=0`, all docks must have the same charge level. The minimal overload is achieved at `P=2`, resulting in differences `[1, 1, 1]`.
**Output:**  
`0`  
**Explanation:**  
Set `P₁=1`, `P₂=3`, `P₃=3`. Only 1 change occurs (between `D₁` and `D₂`), which is allowed.


---

## Approach

### Binary Search + Greedy Feasibility Check
1. **Binary Search on Overload Factor**:
   **What does it do?** - It tries to minimize the value of overload factor by checking the first mid for valid overload factor and if found `True` it iterates through other possible mid values and checks them.
   - The search space is `[0, max(C) - min(C)]`.
   - For each candidate overload value `mid`, check if it is feasible to adjust `P_i` such that the overload does not exceed `mid` with ≤ `K` changes.

3. **Feasibility Check**:
   **What does it do?** - It checks whether the `mid` in our Binary Search can be a possible overload factor or not.
   - Partition the docks into contiguous segments where the charge level can vary within `[current_min, current_max]` (adjusted by `mid`).
   - Track the number of segments. If the number of segments exceeds `K+1`, the candidate `mid` is invalid as we are allowed to make at MAX K number of changes on K+1 segments.
   - **Key Insight**: Each segment represents a group of docks with the same charge level. The number of changes allowed (`K`) equals the number of segment transitions (`segments - 1`).

### Special Case:
- If `K ≥ N-1`,  we can set `P_i = C_i` for all docks (overload factor is `0`). So we don't even check anything if the input satisfies this condition , we can confidently say the overload factor has to be zero.

