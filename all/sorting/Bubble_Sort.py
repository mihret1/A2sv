def countSwaps(arrays):
    myswaps = 0
    for i in range(len(arrays)):
        for j in range(len(arrays) - 1):
            if arrays[j] > arrays[j + 1]:
                temp = arrays[j]
                arrays[j] =arrays[j+1]
                arrays[j+1] = temp
                myswaps += 1
            else:
                continue
    first = arrays[0]
    last = arrays[-1]
    print("Array is sorted in", myswaps, "swaps.")
    print("First Element:", first)
    print("Last Element:", last)


s = int(input())
nums = tuple(input().split())
ary = [0] * s
for i in range(s):
    ary[i] = int(nums[i])
countSwaps(ary)
