from array import array
from timeit import default_timer as timer
import numpy as np
from matplotlib import pyplot as plt

# START OF MERGE SORT MODULE
    # The logic behind the merge sort is to split the array in half recursively
    # When arrays with all the subarrays have size 1, start merging them while sorting
    # It does all the steps even if not needed

def merge(arr, begin, end, middle):
    # Make copies of both arrays we're trying to merge
    left_copy = arr[begin:middle + 1]
    right_copy = arr[middle+1:end+1]

    # Initial values for variables that we use to keep track of where we are in each array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = begin

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the merged
        # list and then move forward in left_copy (by increasing the pointer)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            arr[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Opposite from above
        else:
            arr[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Regardless of where we got our element from
        # move forward in the  part
        sorted_index = sorted_index + 1

    # After running out in one of the sides, just put the rest of the elements at the end (it is guaranteed that these will be sorted)
    while left_copy_index < len(left_copy):
        arr[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        arr[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1
        
def mergeSort(arr, begin, end):
    if begin >= end:
        return
    mid = (begin + end)//2
    mergeSort(arr, begin, mid)
    mergeSort(arr, mid + 1, end)
    merge(arr, begin, end, mid)

def mergeSortCall(arr):
    # Creating a function to simplify the calling of merge sort for the user
    mergeSort(arr, 0, len(arr)-1)

# END OF MERGE SORT MODULE

# START OF BUBBLE SORT MODULE
    # Bubble sort consist in swapping adjacent keys, if the pair is not sorted
    # Bubble sort passes through the array at least once

def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return

def bubbleSortCall(arr):
    # Just standartizing function calls 
    bubbleSort(arr)

# END OF BUBBLE SORT MODULE

# START OF QUICK SORT MODULE
    # Quick sort consists of chosing a pivot and placing it in the correct posiciont in the array
    # Then, we divide the array in left and right subarrays (centered in the pivot) and apply the algorithm again for each side
    # The every element of the left subarray is lower than the pivot and for the right is the oposite 

# Function to find the partition position (and placing the pivot at the right position) 
def partition(array, begin, end):

  # choose the rightmost element as pivot
  pivot = array[end]

  # pointer for greater element
  i = begin - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(begin, end):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[end]) = (array[end], array[i + 1])

  # return the position from where partition is done
  return i + 1

def quickSort(arr,begin,end):
    if begin < end:
        # Find where the pivot is and sort the subarrays
        pivotIndex = partition(arr,begin,end)

        # Call quick sort recursivelly
        quickSort(arr,begin,pivotIndex-1)
        quickSort(arr,pivotIndex+1,end)

def quickSortCall(arr):
    # Simplified call
    quickSort(arr,0,len(arr)-1)

# END OF QUICK SORT MODULE

# MAIN
def main():
    # Creating the vector of results for each runtime
    quickTime = []
    bubbleTime = []
    mergeTime = []
    sizeOfArray = []
    #starting power
    power = 1
    while power <= 7:
        #quick sort and merge sort will be limited to n = 10**7
        #Further analysis at the end of the code
        n = int(10**power) 
        #n>10**5 starts taking too long to sort with bubble sort (n = 10**5, t = )
        #n>10**7 starts taking too long to sort with quick and merge sort (n = 10**7, t = )
        print(n)
        sizeOfArray.append(n)
        arr = np.random.rand(n)*200000 - 100000
        # For each array created, add the runtime of each algorithm to its array
        # Sort only the copies of the array to retain the original one
        # Quick sort
        start = timer()
        quickSortCall(arr.copy())
        end = timer()
        quickTime.append(end-start)
        aux = 0
        # Bubble sort will be limited to 10**4 for a shorter computing time
        # Further analysis at the end of the code
        if power<=4:
            start = timer()
            bubbleSortCall(arr.copy())
            end = timer()
            bubbleTime.append(end-start)
            aux = end-start
        # Merge sort
        else:
            #any results after 10**4 must be ignored, setting it constant after for simplicity
            bubbleTime.append(bubbleTime[3])
        start = timer()
        mergeSortCall(arr.copy())
        end = timer()
        mergeTime.append(end-start)
        power = power + 1 #step of the power of 10
    # Plot each algorithm
    plt.plot(sizeOfArray, quickTime, "r--", label = "Quick sort")
    plt.plot(sizeOfArray, mergeTime, "b-", label = "Merge sort")
    plt.plot(sizeOfArray, bubbleTime, "g:", label = "Bubble sort")
    plt.title(
    "Runtime comparison",
    fontsize='large',
    loc='center',
    fontweight='bold',
    style='italic',
    family='monospace')
    plt.legend()
    plt.show()
    print("merge sort: " + mergeTime)
    print("bubble sort: " + bubbleTime)
    print("quick sort: " + quickTime)
        

main()
