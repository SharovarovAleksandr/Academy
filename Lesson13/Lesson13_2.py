import time
import random
from random_words import RandomWords


def partition(nums, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]

# Quick Sort Algorithm
def quick_sort(nums):
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)

# Insertion Sort Algorithm
def insertion_sort(data):
    for scanIndex in range(1, len(data)):
        tmp = data[scanIndex]
        minIndex = scanIndex
        while minIndex > 0 and tmp < data[minIndex - 1]:
            data[minIndex] = data[minIndex - 1]
            minIndex -= 1
        data[minIndex] = tmp
    return data

# Selection Sort Algorithm
def selection_sort(data):
    for scanIndex in range(0, len(data)):
        minIndex = scanIndex
        for compIndex in range(scanIndex + 1, len(data)):
            if data[compIndex] < data[minIndex]:
                minIndex = compIndex
        if minIndex != scanIndex:
            data[scanIndex], data[minIndex] = data[minIndex], data[scanIndex]
    return data

# Bubble Sort Algorithm
def bubble_sort(data):
    length = len(data)
    for iIndex in range(length):
        swapped = False
        for jIndex in range(0, length - iIndex - 1):
            if data[jIndex] > data[jIndex + 1]:
               data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
               swapped = True
        if not swapped:
            break
    return data

# Merge Sort Algorithm
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # We use the list lengths often, so it is handy to make variables
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # We check which value from the start of each list is smaller
            # If the item at the beginning of the left list is smaller, add it
            # to the sorted list
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # If the item at the beginning of the right list is smaller, add it
            # to the sorted list
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # If we've reached the end of the left list, add the elements
        # from the right list
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # If we've reached the end of the right list, add the elements
        # from the left list
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):
    # If the list is a single element, return it
    if len(nums) <= 1:
        return nums

    # Use floor division to get midpoint, indices must be integers
    mid = len(nums) // 2

    # Sort and merge each half
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Merge the sorted lists into a new one
    return merge(left_list, right_list)

# Insertion Sort Algorithm
def insertion_sort(nums):
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Insert the item
        nums[j + 1] = item_to_insert


def heapify(nums, heap_size, root_index):
    # Assume the index of the largest element is the root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index, and the element is greater
    # than the current largest element, then update the largest element
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # Do the same for the right child of the root
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # If the largest element is no longer the root element, swap them
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)

# Heapify Sort Algorithm
def heap_sort(nums):
    n = len(nums)

    # Create a Max Heap from the list
    # The 2nd argument of range means we stop at the element before -1 i.e.
    # the first element of the list.
    # The 3rd argument of range means we iterate backwards, reducing the count
    # of i by 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Move the root of the max heap to the end of
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


def ev_rez(tp,n,el,met):
    s=0.0
    l=list()
    for i in range(n):
        if tp == "int":
            for m in range(el):
                l.append(random.randint(0, 1000))
        elif tp == "float":
            for m in range(el):
                l.append(random.uniform(0.1,100))
        elif tp == "str":
            l = w.random_words(letter=None, count=el, min_letter_count=3)

        st=time.time()
        if met=="bubble_sort":
            bubble_sort(l)
        elif  met=="quick_sort":
            quick_sort(l)
        elif met == "merge_sort":
            merge_sort(l)
        elif met == "insertion_sort":
            insertion_sort(l)
        elif met == "selection_sort":
            selection_sort(l)
        elif met == "heap_sort":
            heap_sort(l)
        else:
            print("Виникла помилка в програмі!!!")

        s+=time.time()-st
        l.clear()
    return s/n

w=RandomWords()
while True:
    try:
        n=int(input("Введіть кількість ітерацій : "))
        break
    except ValueError:
        print(" Кількість обчислень повинна бути цілим числом! ")
        continue
while True:
    try:
        el=int(input("Введіть кількість елементів списку : "))
        break
    except ValueError:
        print(" Кількість елементів списку повинна бути цілим числом! ")
        continue
while True:
    tp = input("Введіть тип списку (int/float/str) : ")
    if tp=="int":
        break
    elif tp=="float":
        break
    elif tp=="str":
        break
    else:
        print("Тип списку може бути тільки int або float або str! ")


list_metod=["bubble_sort","quick_sort","insertion_sort","merge_sort","selection_sort","heap_sort"]
for i in list_metod:
    print(" Середній час виконання ",n," ітерацій методом ",i," дорівнює ",ev_rez(tp,n,el,i))
