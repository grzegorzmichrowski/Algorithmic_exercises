def add_numbers_to_list():
    while True:
        numbers_list = input('Please write list of numbers separated by comma: ')
        if len(numbers_list) < 3 or (',' not in numbers_list): # change second condition
            continue
        numbers = numbers_list.split(',')
        numbers_integers = []
        try:
            for i in numbers:
                numbers_integers.append(int(i))
        except ValueError:
            continue
        return numbers_integers


list_of_numbers = add_numbers_to_list()

N = len(list_of_numbers)


def check_if_not_in_right_order():
    j = 0    
    while j <= N-2:
        if list_of_numbers[j] > list_of_numbers[j+1]:
            temp = list_of_numbers[j+1]
            list_of_numbers[j+1] = list_of_numbers[j]
            list_of_numbers[j] = temp
            j+=1
        else:
            j+=1


def check_if_all_numbers_checked():
    i = 1
    while i < N:
        check_if_not_in_right_order()
        i+=1


check_if_all_numbers_checked()

print(list_of_numbers)

# close in main function