# nums = []
# for i in range(4):
#     nums.append(int(input()))
# sum = nums[0] + nums[1]
# print(sum)


# s = '12345'
# s = s[2:]
# print(s)

s = '{[]}()'
ls = []

for i in range(len(s)):
    if not ls:
        ls.append(s[i])
        print("4:", ls)
