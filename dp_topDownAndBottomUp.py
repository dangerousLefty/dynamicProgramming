
#this is not dp, but a simple recursion
def fib(n: int) -> int:
    if n == 0:
        return 1
    
    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)


#top-down approach to dp (recursion + memoization)
def fibTopDown(n: int) -> int:
    memoHm = {}
    return fibTopDownHelper(n, memoHm)


def fibTopDownHelper(n: int, hm) -> int:
    if n == 0 or n == 1:
        return 1
    
    if n not in hm:
        hm[n] = fibTopDownHelper(n-1, hm) + fibTopDownHelper(n-2, hm)
        return hm[n]
    
    else:
        return hm[n]

#bottom-up dp forward approach
#
# f(i-1)
#       \
#         >-------> f(i)
#       /
# f(i-2)

def fibBottomUpForward(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(dp)):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[len(dp)-1]

#bottom-up dp forward approach
#
#       -----> f(i+1)
#       |
#      f(i)
#       |
#       -----> f(i+2)

def fibBottomUpBackward(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    
    dp = [0 for i in range(n+2)]
    dp[0] = 1
    dp[1] = 1
    for i in range(1, len(dp)-2):
        dp[i+1] += dp[i]
        dp[i+2] += dp[i]

    return dp[n]




print(fibTopDown(4))
print(fibBottomUpForward(4))
print(fibBottomUpBackward(4))
