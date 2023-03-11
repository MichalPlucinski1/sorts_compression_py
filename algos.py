import random
import time
from enum import Enum


def programStart():
    for i in range(4):
        print("---program start---")


#enum for sorts
class aSort(Enum):
    iS = 1
    sS = 2
    hS = 3
    mS = 4



#filling tab
def tabFill(arr, l=1000, v=100):
    for i in range(0, l): #packing tab
        arr.append(random.randrange(1, v)) #from 1 to valuemax



#function measuring time of actions in parameters
def mTime(arr, sort: aSort):
    print(sort)
    print(sort == aSort.iS)
    if sort == aSort.iS:
        start_time = time.time()
        iS(arr.copy())
        stop_time = time.time() - start_time

    elif sort == aSort.sS:
        start_time = time.time()
        sS(arr.copy())
        stop_time = time.time() - start_time

    elif sort == aSort.hS:
        start_time = time.time()
        hS(arr.copy())
        stop_time = time.time() - start_time

    elif sort == aSort.mS:
        start_time = time.time()
        hS(arr.copy())
        stop_time = time.time() - start_time    

    else:
        print("bad sort")
        return 0
    return stop_time


#Insertion Sort
def iS(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Selection Sort
def sS(arr):
# Traverse through all array elements
    for i in range(len(arr)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Heap Sort (auxiliary function)
def heapify(arr, N, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, N, largest)

# Heap Sort (main hS function)
def hS(arr):
    N = len(arr)

    # Build a maxheap.
    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    # One by one extract elements
    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# Merge Sort
def mS(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mS(L)
  
        # Sorting the second half
        mS(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def main():
    programStart()
    r = []
    l = 5000 #length of array
    v = 150 #max value in array
    n = 5 #how much reapets for each sort
    tabFill(r, l, v) #(arr, len, val)


    for sort in (aSort):
        
        print(sort.value, "-", sort)
        t = mTime(r, sort)
        print(sort.name,"  %s seconds " % (t))

    s2 = aSort.hS
    print(s2)
if __name__ == "__main__":
    main()


