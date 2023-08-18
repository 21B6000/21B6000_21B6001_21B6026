input_tuples = (1, 2, 3, 4, 5)

def tuple_sum1(tuples):
    count = 0
    for i in tuples:
        count = count + i
    return(count)

print("sum of tuples", input_tuples, " = ", tuple_sum1(input_tuples))