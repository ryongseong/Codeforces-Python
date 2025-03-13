cards = int(input())
nums = list(map(int, input().split()))

s = 0
d = 0
l, r = 0, cards - 1
state = "s"

while l <= r:
    if state == "s":
        if nums[l] > nums[r]:
            s += nums[l]
            l += 1
        else:
            s += nums[r]
            r -= 1
        state = "d"
    else:
        if nums[l] > nums[r]:
            d += nums[l]
            l += 1
        else:
            d += nums[r]
            r -= 1
        state = "s"

print(f"{s} {d}")
