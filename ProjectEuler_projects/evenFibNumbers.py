# gen fib sequence up to max limit
# add even-valued to array
# return sum of array

def gen_fib(max_value):
    prev_value = 1
    current_value = 1
    fib_output = [1, 1]

    while current_value < max_value:
        temp_value = current_value

        current_value += prev_value
        prev_value = temp_value

        fib_output.append(current_value)

    return fib_output

def return_even(input_array):
    output_array = []

    for x in input_array:
        if x%2 == 0:
            output_array.append(x)

    return output_array

def sum_array(input_array):
    output = 0

    for x in input_array:
        output += x

    return output

def run():
    max_value = 4000000

    fib = gen_fib(max_value)
    fib = return_even(fib)
    result = sum_array(fib)

    print("The sum of the even-numbered terms in the Fibonnaci sequence below 4 million is " + str(result) + "!")

run()
