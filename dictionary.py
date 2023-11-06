n = int(input("Enter an integral number (n): "))

result_dict = {}

for i in range(1, n + 1):
    result_dict[i] = i * i

print(result_dict)
