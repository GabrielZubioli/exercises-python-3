nums = []
while True:
    num = int(input("Digite um numero (zero encerra): "))
    if num == 0:
        break
    else:
        nums.append(num)

for num in nums:
    print(num)