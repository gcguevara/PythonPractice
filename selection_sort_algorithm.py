'''
    GARRETT GUEVARA
    TECH ACADEMY DRILL:
    CREATE A SORTING ALGORITHM
'''

def selection_sort(my_list):
    for i in range(0,len(my_list)-1, 1):
        min_value = i
        for j in range(i+1,len(my_list), 1):
            if my_list[j] < my_list[min_value]:
                min_value = j
        if min_value != i:
            temp = my_list[i]
            my_list[i] = my_list[min_value]
            my_list[min_value] = temp
    return my_list


my_list = [67, 45, 2, 13, 1, 998]
my_list1 = [89, 23, 33, 45, 10, 12, 45, 45, 45]

print(selection_sort(my_list))
print(selection_sort(my_list1))


                
    
