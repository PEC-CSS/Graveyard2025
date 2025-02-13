from functools import lru_cache

def count_dragon_blessed(X):
    """
    Count numbers in [0, X] that are Dragon-Blessed.
    (0 is counted as Dragon-Blessed as a single-digit number.)
    """
    s = str(X)
    n = len(s)
    
    @lru_cache(maxsize=None)
    def dp(pos, tight, started, first_digit):
        """
        pos: current index (0-indexed) in s
        tight: True if current prefix is exactly equal to s's prefix; else False
        started: True if we've placed a nonzero digit (i.e., the number has started)
        first_digit: the first nonzero digit (if started), or -1 if not started
        """
        # Base case: if we've processed all positions:
        if pos == n:
            # If we never started, that means the number is 0 (which is valid).
            return 1
        
        res = 0
        max_digit = int(s[pos]) if tight else 9
        
        for d in range(0, max_digit + 1):
            new_tight = tight and (d == max_digit)
            if not started:
                # Still in the leading zeros
                if d == 0:
                    # Continue without starting
                    res += dp(pos + 1, new_tight, False, -1)
                else:
                    # Start the number with d
                    res += dp(pos + 1, new_tight, True, d)
            else:
                # Already started: enforce that the chosen digit is < first_digit
                if d < first_digit:
                    res += dp(pos + 1, new_tight, True, first_digit)
                # If d >= first_digit, skip this branch (invalid Dragon-Blessed)
        return res

    return dp(0, True, False, -1)

# Example usage:
L, R = map(int, input().split())
# Count valid numbers in [0, R] and subtract those in [0, L-1]
result = count_dragon_blessed(R) - count_dragon_blessed(L - 1)
print(result)
