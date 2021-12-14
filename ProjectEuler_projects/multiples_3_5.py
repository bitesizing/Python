
max_value = 1000
sum_count = 0
num_array = []

for x in range(1, max_value):
    if x%3 == 0 or x%5 == 0:
        num_array.append(x)

for x in num_array:
    sum_count += x

print("The sum of all the multiples below " + str(max_value) + " is equal to " + str(sum_count) + "!")
