import math
import numpy as np

PS_list = []

for number in range(1000, 10000):
    if math.sqrt(number).is_integer():
        PS_list.append(number)

zeroPS_set = set()

for number in PS_list:
    digit = str(number)
    for zero_check in digit:
        if int(zero_check) == 0:
            zeroPS_set.add(number)

zeroPS_list = list(zeroPS_set)

zeroPS_list.sort()

list_a = [x for x in PS_list if x not in zeroPS_list]

badendPS_set = set()

for number in list_a:
    digit = str(number)
    for digit_check in digit:
        if int(digit_check) == 2 or int(digit_check) == 3 or int(digit_check) == 7 or int(digit_check) == 8:
           badendPS_set.add(number)

badendPS_list = list(badendPS_set)

badendPS_list.sort()

list_b = [x for x in list_a if x not in badendPS_list]

def oblist(your_list, object_index):
    oblist = []
    object = str(your_list[object_index])
    for digit in object:
        oblist.append(digit)
    return oblist


def candidator(main_list, rowlist_oblist, x):
    new_list = []
    for number in main_list:
        digit = str(number)
        if int(digit[3]) == int(rowlist_oblist[int(x)]):
            new_list.append(number)
    return new_list


def full_oblist(your_list, list_length):
    new_list = []
    object_index = 0
    if object_index <= list_length:
        for object in your_list:
            object = oblist(your_list, object_index)
            new_list.append(object)
            object_index += 1
    return new_list


def PS_checker(number):
    is_PS = False
    if math.sqrt(number).is_integer():
        is_PS = True
    return is_PS


def number_from_list_digits(oblist):
    num = 0;
    tenth_spot = len(oblist)
    for digit in oblist:
        num = num + digit * (10 ** (tenth_spot - 1))
        tenth_spot = tenth_spot - 1
    return num


def solution_check(nested_list):
    solution = True
    i = 0
    for sublist in nested_list:
        number = number_from_list_digits(sublist)
        boolean = PS_checker(number)
        if boolean is False:
            i += 1
    if i != 0:
        solution = False
    return solution


matrix = np.array([[11, 12, 13, 14],
                   [21, 22, 23, 24],
                   [31, 32, 33, 34],
                   [41, 42, 43, 44]])

index = 0

symmetric_matrices = 0


def exhausterL3():
    for sublist in len_order:
        global symmetric_matrices
        if sublist[len(sublist) - 1] == 0 and sublist == len_order[3]:
            sublist.remove(sublist[len(sublist) - 1])
            index = 0
            while index < len(sublist):
                matrix[:, 0] = sublist[index]
                nested_list_of_rows = []
                row_0 = matrix[0, :]
                row_1 = matrix[1, :]
                row_2 = matrix[2, :]
                row_3 = matrix[3, :]
                nested_list_of_rows.extend((row_0, row_1, row_2, row_3))
                if solution_check(nested_list_of_rows) is True:
                    print(matrix)
                if list(matrix[0, :]) == list(matrix[:, 0]) and list(matrix[1, :]) == list(matrix[:, 1]) and list(
                        matrix[2, :]) == list(matrix[:, 2]) and list(matrix[3, :]) == list(matrix[:, 3]):
                    symmetric_matrices += 1
                index += 1
            sublist.append(0)
        elif sublist[len(sublist) - 1] == 1 and sublist == len_order[3]:
            sublist.remove(sublist[len(sublist) - 1])
            index = 0
            while index < len(sublist):
                matrix[:, 1] = sublist[index]
                nested_list_of_rows = []
                row_0 = matrix[0, :]
                row_1 = matrix[1, :]
                row_2 = matrix[2, :]
                row_3 = matrix[3, :]
                nested_list_of_rows.extend((row_0, row_1, row_2, row_3))
                if solution_check(nested_list_of_rows) is True:
                    print(matrix)
                if list(matrix[0, :]) == list(matrix[:, 0]) and list(matrix[1, :]) == list(matrix[:, 1]) and list(
                        matrix[2, :]) == list(matrix[:, 2]) and list(matrix[3, :]) == list(matrix[:, 3]):
                    symmetric_matrices += 1
                index += 1
            sublist.append(1)
        elif sublist[len(sublist) - 1] == 2 and sublist == len_order[3]:
            sublist.remove(sublist[len(sublist) - 1])
            index = 0
            while index < len(sublist):
                matrix[:, 2] = sublist[index]
                nested_list_of_rows = []
                row_0 = matrix[0, :]
                row_1 = matrix[1, :]
                row_2 = matrix[2, :]
                row_3 = matrix[3, :]
                nested_list_of_rows.extend((row_0, row_1, row_2, row_3))
                if solution_check(nested_list_of_rows) is True:
                    print(matrix)
                if list(matrix[0, :]) == list(matrix[:, 0]) and list(matrix[1, :]) == list(matrix[:, 1]) and list(
                        matrix[2, :]) == list(matrix[:, 2]) and list(matrix[3, :]) == list(matrix[:, 3]):
                    symmetric_matrices += 1
                index += 1
            sublist.append(2)
        elif sublist[len(sublist) - 1] == 3 and sublist == len_order[3]:
            sublist.remove(sublist[len(sublist) - 1])
            index = 0
            while index < len(sublist):
                matrix[:, 3] = sublist[index]
                nested_list_of_rows = []
                row_0 = matrix[0, :]
                row_1 = matrix[1, :]
                row_2 = matrix[2, :]
                row_3 = matrix[3, :]
                nested_list_of_rows.extend((row_0, row_1, row_2, row_3))
                if solution_check(nested_list_of_rows) is True:
                    print(matrix)
                if list(matrix[0, :]) == list(matrix[:, 0]) and list(matrix[1, :]) == list(matrix[:, 1]) and list(
                        matrix[2, :]) == list(matrix[:, 2]) and list(matrix[3, :]) == list(matrix[:, 3]):
                    symmetric_matrices += 1
                index += 1
            sublist.append(3)


def exhausterL2():
    for sublist in len_order:
        if sublist[len(sublist) - 1] == 0 and sublist == len_order[2]:
            sublist.remove(sublist[len(sublist) - 1])
            index = 0
            while index < len(sublist):
                matrix[:, 0] = sublist[index]
                exhausterL3()  # EXHAUSTER 3 LEVEL 1
                index += 1
            sublist.append(0)
        elif sublist[len(sublist) - 1] == 1 and sublist == len_order[2]:
            sublist.remove(sublist[len(sublist) - 1])
            index = 0
            while index < len(sublist):
                matrix[:, 1] = sublist[index]
                exhausterL3()  # EXHAUSTER 3 LEVEL 2
                index += 1
            sublist.append(1)
        elif sublist[len(sublist) - 1] == 2 and sublist == len_order[2]:
            sublist.remove(sublist[len(sublist) - 1])
            index = 0
            while index < len(sublist):
                matrix[:, 2] = sublist[index]
                exhausterL3()  # EXHAUSTER 3 LEVEL 3
                index += 1
            sublist.append(2)
        elif sublist[len(sublist) - 1] == 3 and sublist == len_order[2]:
            sublist.remove(sublist[len(sublist) - 1])
            index = 0
            while index < len(sublist):
                matrix[:, 3] = sublist[index]
                exhausterL3()  # EXHAUSTER 3 LEVEL 4
                index += 1
            sublist.append(3)

def exhausterL1():
    for sublist in len_order:
        if sublist[len(sublist) - 1] == 0 and sublist == len_order[1]:
            sublist.remove(sublist[len(sublist) - 1])
            index = 0
            while index < len(sublist):
                matrix[:, 0] = sublist[index]
                exhausterL2()  # EXHAUSTER 2 LEVEL 1
                index += 1
            sublist.append(0)
        elif sublist[len(sublist) - 1] == 1 and sublist == len_order[1]:
            sublist.remove(sublist[len(sublist) - 1])
            index = 0
            while index < len(sublist):
                matrix[:, 1] = sublist[index]
                exhausterL2()  # EXHAUSTER 2 LEVEL 2
                index += 1
            sublist.append(1)
        elif sublist[len(sublist) - 1] == 2 and sublist == len_order[1]:
            sublist.remove(sublist[len(sublist) - 1])
            index = 0
            while index < len(sublist):
                matrix[:, 2] = sublist[index]
                exhausterL2()  # EXHAUSTER 2 LEVEL 3
                index += 1
            sublist.append(2)
        elif sublist[len(sublist) - 1] == 3 and sublist == len_order[1]:
            sublist.remove(sublist[len(sublist) - 1])
            index = 0
            while index < len(sublist):
                matrix[:, 3] = sublist[index]
                exhausterL2()  # EXHAUSTER 2 LEVEL 4
                index += 1
            sublist.append(3)

def exhauster4x4():
    for sublist in len_order:
        if sublist[len(sublist) - 1] == 0 and sublist == len_order[0]:
            sublist.remove(sublist[len(sublist) - 1])
            index = 0
            while index < len(sublist):
                matrix[:, 0] = sublist[index]
                exhausterL1()  # EXHAUSTER 1 LEVEL 1
                index += 1
            sublist.append(0)
        elif sublist[len(sublist) - 1] == 1 and sublist == len_order[0]:
            sublist.remove(sublist[len(sublist) - 1])
            index = 0
            while index < len(sublist):
                matrix[:, 1] = sublist[index]
                exhausterL1()  # EXHAUSTER 1 LEVEL 2
                index += 1
            sublist.append(1)
        elif sublist[len(sublist) - 1] == 2 and sublist == len_order[0]:
            sublist.remove(sublist[len(sublist) - 1])
            index = 0
            while index < len(sublist):
                matrix[:, 2] = sublist[index]
                exhausterL1()  # EXHAUSTER 1 LEVEL 3
                index += 1
            sublist.append(2)
        elif sublist[len(sublist) - 1] == 3 and sublist == len_order[0]:
            sublist.remove(sublist[len(sublist) - 1])
            index = 0
            while index < len(sublist):
                matrix[:, 3] = sublist[index]
                exhausterL1()  # EXHAUSTER 1 LEVEL 4
                index += 1
            sublist.append(3)

while index < len(list_b):
    
    rowlist_0 = oblist(list_b, index)

    matrix[3, :] = rowlist_0

    candidates_0 = candidator(list_a, rowlist_0, 0)
    candidates_1 = candidator(list_a, rowlist_0, 1)
    candidates_2 = candidator(list_a, rowlist_0, 2)
    candidates_3 = candidator(list_b, rowlist_0, 3)

    canoblist_0 = full_oblist(candidates_0, int(len(candidates_0)))
    canoblist_1 = full_oblist(candidates_1, int(len(candidates_1)))
    canoblist_2 = full_oblist(candidates_2, int(len(candidates_2)))
    canoblist_3 = full_oblist(candidates_3, int(len(candidates_3)))

    canoblist_0.append(0)
    canoblist_1.append(1)
    canoblist_2.append(2)
    canoblist_3.append(3)

    len_order = []

    len_order.append(canoblist_0)
    len_order.append(canoblist_1)
    len_order.append(canoblist_2)
    len_order.append(canoblist_3)

    len_order.sort(key=len)

    matrix[:, 0] = canoblist_0[0]
    matrix[:, 1] = canoblist_1[0]
    matrix[:, 2] = canoblist_2[0]
    matrix[:, 3] = canoblist_3[0]

    exhauster4x4()

    index += 1

print(symmetric_matrices)