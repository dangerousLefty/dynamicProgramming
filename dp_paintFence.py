def paintFence(nPosts: int, kPaints: int) -> int: 
    if nPosts == 0:
        return 0
    
    if nPosts == 1:
        return kPaints

    same = kPaints
    diff = kPaints * (kPaints - 1)

    if nPosts > 2:
        for i in range(3, nPosts+1):
            prevDiff = diff
            diff = (same + diff) * (kPaints - 1)
            same = prevDiff * 1

    return same + diff







a = paintFence(5,2)
print(a)