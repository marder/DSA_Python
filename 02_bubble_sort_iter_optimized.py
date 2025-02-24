def bubble_sort(lst):

    size = len(lst)

    for i in range(size):

        for j in range(size - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst


unsorted_list = [69, 6, 15, 0, 55, 4]

print(f"Unsorted List: {unsorted_list}")

sorted_list = bubble_sort(unsorted_list)

print(f"Sorted List: {sorted_list}")
