input_for_array = input("Введите числа для массива через пробел:").split()
array = input_for_array[:]
array_replace_in_int = [int(item) for item in array]


def only_numbers_that_multiples_of_3():
    for i in array_replace_in_int:
        if i % 3 == 0:
            print(i)


print("Числа кратные 3:")
only_numbers_that_multiples_of_3()
