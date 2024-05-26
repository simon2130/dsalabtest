list = []
def add_nums(list):
    number = int(input("enter number to add in the list: "))
    while number != -1:
        number = int(input("enter another number or enter -1 to quit: "))
        list.append(number)
    return list


def sum(list, num):
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[i] + list[j] == num:
                if i == j:
                    continue
                return i, j

    return -1
add_nums(list)
num = int(input("enter number to find: "))
if sum(list,num) != -1:
    print("index --> ", sum(list,num))
else:
    print("the are no numbers that give ", num, "when added")


