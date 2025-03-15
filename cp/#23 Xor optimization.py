n = int(input())
data_packets = list(map(int, input().split()))

groups = []
xor_values = set()

def dfs(index):
    if index == n:
        xor_result = 0
        for i in groups:
            xor_result ^= g
        xor_values.add(xor_result)
        return

    for i in range(len(groups)):
        groups[i] += data_packets[index]
        dfs(index+1)
        groups[i] -= data_packets[index]

    groups.append(data_packets[index])
    dfs(index+1)
    groups.pop()

dfs(0)
print(len(xor_values))
