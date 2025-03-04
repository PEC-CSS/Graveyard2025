from itertools import combinations

def get_unique_xor_values(n, data_packets):
    xor_values = set()
    states_done = set()
    
    def dfs(state):
        if tuple(state) in states_done:
            return
        states_done.add(tuple(state))
        
        xor_result = 0
        for value in state:
            xor_result ^= value
        xor_values.add(xor_result)    
        for x, y in combinations(range(len(state)), 2):
            if state[x] == 0:
                continue
            
            new_state = state[:]
            new_state[y] += new_state[x]
            new_state[x] = 0
            new_state = [val for val in new_state if val != 0]   
            dfs(new_state)  
    dfs(data_packets)
    return len(xor_values)
n = int(input())
data_packets = list(map(int, input().split()))
unique_xor_count = get_unique_xor_values(n, data_packets)
print(unique_xor_count)
