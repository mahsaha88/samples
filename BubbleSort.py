def bubble_sort(list1):
    for i in range(0, len(list1)-1):
        for j in range(0, len(list1)-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1


list1 = [5, 3, 8, 7, 2]
print(bubble_sort(list1))
