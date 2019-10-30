ans = 0
a = [3, 1, 2, 5, 4]
tmp = [0] * len(a)

def merge_sort(nums, l, r):
    if l == r:
        return
    mid = (l + r) // 2
    merge_sort(nums, l, mid)
    merge_sort(nums, mid + 1, r)
    i, j = l, mid + 1
    x = l - 1
    global ans
    while i <= mid and j <= r:
        if nums[i] < nums[j]:
            x += 1
            tmp[x] = nums[i]
            i += 1
        else:
            x += 1
            tmp[x] = nums[j]
            ans += mid - i + 1
            j += 1
    while i <= mid:
        x += 1
        tmp[x] = nums[i]
        i += 1
    while j <= r:
        x += 1
        tmp[x] = nums[j]
        j += 1
    for i in range(l, r + 1):
        nums[i] = tmp[i]

merge_sort(a, 0, len(a) - 1)
print(ans)
