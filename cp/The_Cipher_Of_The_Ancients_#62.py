def commonSubsequences(s1,s2):
    
    def getSubsequences(sample):
        subsequences= []
        for i in range(len(sample)):
            for j in range(i+1, len(sample)+1):
                for k in range(1,len(sample)):
                    subsequences.append(sample[i:j:k])
                    
        return subsequences

    s1 = getSubsequences(s1)
    s2 = getSubsequences(s2)
    common = []
    for i in s1:
        if i in s2:
            common.append(i)
    return common

def lengthOfLongestCommonSubsequence(common):
    length=0
    for i in common:
        if len(i) > length:
            length = len(i)
    return length

s1 = input().replace("\"", "")
s2 = input().replace("\"", "")
common = commonSubsequences(s1,s2)
print(lengthOfLongestCommonSubsequence(common))
            