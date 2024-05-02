nums = range(1, 10)
products = {}
possible_combs = 0

for a in nums:
    if nums[-2] == a:
        break
    for b in nums[nums.index(a) + 1 :]:
        if nums[-1] == b:
            break
        for c in nums[nums.index(b) + 1 :]:
            prod = a * b * c
            products[prod] = products.get(prod, [0]) + [f"{a}*{b}*{c}"]
            products.get(prod)[0] = products.get(prod)[0] + 1
            possible_combs += 1


multi_combs_prods = {}
num = 0
num_1 = 0
for x, y in products.items():
    num_1 += 1
    if y[0] > 1:
        multi_combs_prods[x] = y
        num += 1

del products

print(f"There are {possible_combs} possible combinations for the range provided")
print(
    f"There are {num} such products that has multiple different combinations out of {num_1}"
)
print(multi_combs_prods)
