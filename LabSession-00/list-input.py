number = int(input("Enter how many numbers to insert: "))
nums = []

for i in range(number):
    number_input = int(input("Enter number " + str(i + 1) + ": "))
    nums.append(number_input);

print(nums)

