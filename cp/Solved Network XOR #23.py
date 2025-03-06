from itertools import combinations
from functools import lru_cache

def get_unique_xor_values(n, data_packets):
    xor_values = set()

    @lru_cache(None)
    def dfs(state):
        state = tuple(sorted(state))
        
        if state in visited:
            return
        visited.add(state)

        xor_result = 0
        for value in state:
            xor_result ^= value
        xor_values.add(xor_result)

        for x, y in combinations(range(len(state)), 2):
            new_state = list(state)
            new_state[y] += new_state[x]
            new_state[x] = 0
            new_state = tuple(sorted(num for num in new_state if num != 0))
            dfs(new_state)

    visited = set()
    dfs(tuple(data_packets))
    
    return len(xor_values)

n = int(input())
data_packets = list(map(int, input().split()))
unique_xor_count = get_unique_xor_values(n, data_packets)
print(unique_xor_count)
