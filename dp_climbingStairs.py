def climbStairs(steps: int) -> int:
    stepArr = [i for i in range(steps+1)]
    stepArr[0] = 1
    stepArr[1] = 1

    for i in range(2,len(stepArr)):
        stepArr[i] = stepArr[i-1] + stepArr[i-2]

    return stepArr[len(stepArr)-1]

def climbStairsFollowUp(steps: int, increment: int) -> int:
    stepArr = [0 for i in range(steps + 1)]
    stepArr[0] = 1
    stepArr[1] = 1

    for i in range(2, len(stepArr)):
        for j in range(1, increment+1):
            if j > i:
                continue
            stepArr[i] += stepArr[i-j]

    return stepArr[steps]




a = climbStairsFollowUp(5,3)

print(a)