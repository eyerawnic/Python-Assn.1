input_str = input("Enter a sequence of comma-separated numbers: ")

numbers_list = [int(num) for num in input_str.split(',')]

numbers_tuple = tuple(numbers_list)

print("List:", numbers_list)
print("Tuple:", numbers_tuple)
