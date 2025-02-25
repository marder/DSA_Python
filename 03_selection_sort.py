def selection_sort(lst):

    for i in range(len(lst)):

        min_index = i

        for j in range(i + 1, len(lst)):

            if lst[j] < lst[min_index]:
                min_index = j

        lst[min_index], lst[i] = lst[i], lst[min_index]

    return lst


lst = [69, 11, 2, 13, 1]
print(f'Unsorted List: {lst}')

sorted_list = selection_sort(lst)
print(f'Sorted List: {sorted_list}')
