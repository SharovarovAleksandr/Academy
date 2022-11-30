import random
import time
from random_words import RandomWords
w = RandomWords()



# Bubble Sort Algorithm
def bubble_sort(l):
    n = len(l)
    for j in range(n - 1):
        for i in range(n - j - 1):
            if l[i]>l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
    return l



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


def quick_sort(nums):
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)

word_list=w.random_words(letter=None,count=250, min_letter_count=3)
ua_list=["гуцул","цегла","цеберко","рішення","пательня","лазня","крамниця","краватка","ожина","лохина","праска"]
print(word_list)

for i in ua_list:
    k=random.randint(0,len(word_list))
    word_list[k]=i
print(word_list)

l1=word_list.copy()
l2=word_list.copy()

st=time.time()
bubble_sort(l1)
print(l1)
rez1=time.time()-st
print("Час виконання bubble_sort - ",rez1)

st=time.time()
quick_sort(l2)
print(l2)
rez2=time.time()-st
print("Час виконання quick_sort - ",rez2)

print("Алгоритм quick_sort ефективніший за bub_sort у ",rez1/rez2," разів")