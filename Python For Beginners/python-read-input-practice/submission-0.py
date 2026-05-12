def add_two_numbers() -> int:
    num = input()
    myList = num.split(",")
    for i in range(len(myList)):
        myList[i] = int(myList[i])
    sum = 0
    for i in myList:
        sum+=i
    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
