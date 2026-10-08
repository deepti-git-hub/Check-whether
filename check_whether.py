numbers = [1, 2, 3, 2, 1]

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

if numbers == reversed_list:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")
