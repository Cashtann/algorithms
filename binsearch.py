list = [1, 2, 4, 5, 6, 8, 12, 23 ,34, 45, 67, 76, 78, 93, 102, 204, 425, 543, 742, 995]

iteration = 0

def binsearch(arr, item):
    global iteration
    if len(arr) == 0:
        return -1
    L = 0
    R = len(list)-1
    M = 0
    while L <= R:
        M = (L+R)//2
        iteration += 1
        if arr[M] > item:
            R = M-1
        elif arr[M] < item:
            L = M+1
        else:
            return M
    return -1
searchFor = ""
while True:
    searchFor = input("Provide search item: ")
    if searchFor.isnumeric():
        break
    else:
        print("Wrong input bozo")
result = binsearch(list, int(searchFor))
if result != -1:
    print("\nNumber {} was found on index {} of the list in {} iteration(s) ".format(searchFor, result, iteration))
else:
    print("\nNumber not found! ")
