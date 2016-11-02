'''
    GARRETT GUEVARA
    TECH ACADEMY DRILL:
    CREATE A SORTING ALGORITHM
'''

def bubble_sort(my_list):
    for i in range(len(my_list)-1,0,-1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

my_list = [67, 45, 2, 13, 1, 998]
my_list1 = [89, 23, 33, 45, 10, 12, 45, 45, 45]

print(bubble_sort(my_list))
print(bubble_sort(my_list1))
