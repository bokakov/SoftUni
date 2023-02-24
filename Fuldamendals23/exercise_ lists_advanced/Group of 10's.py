nums = [int(x) for x in input().split(", ")]

check_list = list()
for n in range(1, 10 + 1):
    check_list.clear()
    if len(nums) != 0:
        for i in nums:
            if i <= (n * 10):
                check_list.append(i)
        for el in check_list:
            nums.remove(el)

        print(f"Group of {n * 10}'s: {check_list}")
