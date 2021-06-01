def target(array, target_sum):
    print("array: ", array)
    print("target sum: ", target_sum)
    num1 = 0; num2 = 0
    sum_arr = []
    for i in range(len(array)):
        num1 = array[i]
        for j in range(len(array)):
            num2 = array[j]
            if((num1 + num2) == target_sum):
                sum_arr.append(num1); sum_arr.append(num2)
                return sum_arr
    return "Didn't find any two numbers that sum to the target"




size = input("How big is your int array: ")
array = []
for i in range(int(size)):
    x = input("Give a number: ")
    array.append(int(x))
ts = input("What's your target sum: ")
print(target(array, int(ts)))

