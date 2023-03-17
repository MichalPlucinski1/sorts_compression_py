import random
import time
from enum import Enum
import numpy as np
import matplotlib . pyplot as plot
import sys
import threading

threading.stack_size(67108864)
sys.setrecursionlimit(2 ** 20)



############################# sorts #############################

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

############################# usage functions #############################

#just separation from other entitis
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
def tabFill(arr, l=10, v=1, rand = True):
    if rand == True: # filling with randoms
        for i in range(0, l): #packing tab
            arr.append(random.randrange(1, v)) #from 1 to valuemax
    else:
        for i in range(0, l): #packing tab 
            arr.append(v)   


#function measuring time of actions in parameters
def mTime(arr, sort: aSort):
    avg = 0
    iterations = 3
    for i in range(iterations):
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

        avg += stop_time 

    stop_time = avg/iterations
    return stop_time


#dividing resuilts for smaller tabs
def divresults(res, viS, vsS, vhS, vmS):
    for i in res:
        viS.append(i[0])
        vsS.append(i[1])
        vhS.append(i[2])
        vmS.append(i[3])

#clearing
def aClear(r, res, viS, vsS, vhS, vmS, vTime):
    del res
    del viS 
    del vsS
    del vhS
    del vmS
    del vTime
    del r

#making graphs
def plotting(viS,vsS,vhS,vmS,vTime, num, title):
    plotnumber = 0 + num #for graphs arrangement
    #linear
    plot.figure()
    plot.plot(vTime, viS, vTime, vsS, vTime, vhS, vTime, vmS)
    plot.title(title)
    plot.xlabel('number of sorts')
    plot.ylabel('time[s]')
    plot.legend([ "iS","sS","hS","mS",])
    plot.grid(True)

    plot.show()
    #logarithm
    plot.figure()
    plot.plot(vTime, viS, vTime, vsS, vTime, vhS, vTime, vmS)
    plot.yscale('log')
    plot.title(str(title + ' log'))
    plot.xlabel('number of sorts')
    plot.ylabel('time[s]')
    plot.legend([ "iS","sS","hS","mS",])
    plot.grid(True) 
    plot.show()

    

#generating v-shaped
def vSFillTab(l, low_num_tabs):
    for i in range(1,low_num_tabs,2):
        l.append(i)
        l.insert(0, i+1)

#updating v-shaped
def vSAddToTab(l, step):
     step = int(step/2)
     for i in range(step):
        first_num = l[0]
        l.append(first_num+1)
        l.insert(0, first_num + 2)



############################# main #############################

def main():
    programStart()
    

    #array settings
    r = []
    #l = 5000 #length of array  # overwritten by 
    v = 150 #max value in array

    
    #loop of 1 sort settings
    startValue = 1000 #750 
    endValue = 2000 #3000
    step = 75 #2  #50
    plot.figure()


    #bufored times
    results = []
    viS = []
    vsS = []
    vhS = []
    vmS = []
    vTime = []

    tabFill(r, startValue, v)
    print("startValue: ", startValue, " endValue: ", endValue, " with step: ", step)

    ################### for random ###################
    for i in range(startValue, endValue, step):
        vTime.append(i) #making y dimmension for plot
        iResults = [] #iteration results in form [iS, sS, hS, mS]
        tabFill(r, step, v) #increasing list size by quant. of step random elements
        print("Filling, len of arr: ", len(r), " of ", endValue)

        for sort in (aSort):
            #print(sort.value, "-", sort)
            t = mTime(r, sort)
            #print(sort.name,"  %s seconds " % (t))
            iResults.append(t)
        results.append(iResults.copy())
        
        iResults.clear()

        print("end of this iteration \n")
    #print(results)

    divresults(results, viS, vsS, vhS, vmS) #dividing results into results per sort
    
    plotting(viS,vsS,vhS,vmS,vTime, 1, "randoms")


    aClear(r, results, viS, vsS, vhS, vmS, vTime)




    ################### for sorted asc ###################
    r = []
    results = []
    viS = []
    vsS = []
    vhS = []
    vmS = []
    vTime = []
    tabFill(r, startValue, v)
    print("startValue: ", startValue, " endValue: ", endValue, " with step: ", step)

    for i in range(startValue, endValue, step):
        vTime.append(i)
        iResults = []
        tabFill(r, step, v)
        print("Filling, len of arr: ", len(r), " of ", endValue)
        mS(r) #here's the difference
        for sort in (aSort):
            #print(sort.value, "-", sort)
            t = mTime(r, sort)
            #print(sort.name,"  %s seconds " % (t))
            iResults.append(t)
        results.append(iResults.copy())
        
        iResults.clear()

        print("end of this iteration \n")

    divresults(results, viS, vsS, vhS, vmS)

    plotting(viS,vsS,vhS,vmS,vTime, 5, "sorted asc")

    aClear(r, results, viS, vsS, vhS, vmS, vTime)

    ################### for sorted desc ###################

    r = []
    results = []
    viS = []
    vsS = []
    vhS = []
    vmS = []
    vTime = []
    tabFill(r, startValue, v)
    print("startValue: ", startValue, " endValue: ", endValue, " with step: ", step)

    for i in range(startValue, endValue, step):
        vTime.append(i)
        iResults = []
        tabFill(r, step, v)
        print("Filling, len of arr: ", len(r), " of ", endValue)
        r.sort(reverse=True) #and here's the difference
        for sort in (aSort):
            #print(sort.value, "-", sort)
            t = mTime(r, sort)
            #print(sort.name,"  %s seconds " % (t))
            iResults.append(t)
        results.append(iResults.copy())
        
        iResults.clear()

        print("end of this iteration \n")

    divresults(results, viS, vsS, vhS, vmS)

    plotting(viS,vsS,vhS,vmS,vTime, 9, "sorted desc")

    aClear(r, results, viS, vsS, vhS, vmS, vTime)

    ################### for const ###################
    r = []
    results = []
    viS = []
    vsS = []
    vhS = []
    vmS = []
    vTime = []
    tabFill(r, startValue, v)
    print("startValue: ", startValue, " endValue: ", endValue, " with step: ", step)

    for i in range(startValue, endValue, step):
        vTime.append(i)
        iResults = []
        tabFill(r, step, v, False)
        print("Filling, len of arr: ", len(r), " of ", endValue)
        r.sort(reverse=True) #and here's the difference
        for sort in (aSort):
            #print(sort.value, "-", sort)
            t = mTime(r, sort)
            #print(sort.name,"  %s seconds " % (t))
            iResults.append(t)
        results.append(iResults.copy())
        
        iResults.clear()

        print("end of this iteration \n")

    divresults(results, viS, vsS, vhS, vmS)

    plotting(viS,vsS,vhS,vmS,vTime, 13, "const")

    aClear(r, results, viS, vsS, vhS, vmS, vTime)

    ################### for v-shaped ###################

    r = []
    results = []
    viS = []
    vsS = []
    vhS = []
    vmS = []
    vTime = []
    vSFillTab(r, startValue)
    print("startValue: ", startValue, " endValue: ", endValue, " with step: ", step)
    for i in range(startValue, endValue, step):
        vTime.append(i)
        iResults = []
        for sort in (aSort):
            #print(sort.value, "-", sort)
            t = mTime(r, sort)
            #print(sort.name,"  %s seconds " % (t))
            iResults.append(t)
        results.append(iResults.copy())
        
        iResults.clear()
        print("Filling, len of arr: ", len(r), " of ", endValue)
        vSAddToTab(r, step)

    divresults(results, viS, vsS, vhS, vmS)

    plotting(viS,vsS,vhS,vmS,vTime, 17, "v-shaped")

    aClear(r, results, viS, vsS, vhS, vmS, vTime)

    ################### all sorts passed ###################



    #plot.show()

if __name__ == "__main__":
    
    thread = threading.Thread(target=main) 
    thread.start()
    #main()



"""
how to implement avg 
we wanna improve quality of results by making several (ultimately 15) tries and take avg of the measurments
for this code probably it would be best to make all tests for 1 type of tab, then retake it.
 So maybe list of results for every sort should be multidimensial vsS[[values in 1-st attempt], [values of 2'nd], ..., [value of 15'th attempt]]
 then we must make another list, which n-th element will be the avg of n-th elements of every attempt


 question is: making avg of sorting one tab, or sorting different data's but with same amount?
"""