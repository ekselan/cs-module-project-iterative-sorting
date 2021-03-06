# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        smallest_value = arr[cur_index]
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for unsorted_index in range(cur_index, len(arr)):
            if arr[unsorted_index] < smallest_value:
                smallest_value = arr[unsorted_index]
                smallest_index = unsorted_index

        # TO-DO: swap
        # Your code here

        # once found, swap with elem on the right edge of
        # sorted-unsorted boundary
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        
    return arr


# TO-DO:  implement the Bubble Sort function below

def bubble_sort(arr):
    """
    Loop through your array
    Compare each element to its neighbor
    If elements in wrong position (relative to each other, swap them)
    If no swaps performed, stop. Else, go back to the element at index 0 
    and repeat step 1.
    """
    # Your code here
    # # loop through elements
    # for i in range(len(arr) -1):
    #     cur_index = i
    #     counter = 0
    #     # for neighbor_index in range(cur_index, len(arr)):
    #     while counter < (len(arr) -1):  
    #         # if elems in wrong pos (rel to e/o), swap them
    #         if arr[counter] > arr[counter + 1]:
    #             arr[cur_index], arr[i+1] = arr[i+1], arr[cur_index]
    #         # breakpoint()
    #         counter += 1

    for n in range(0, len(arr)-1):
        x = 0
        while x < (len(arr)-1):     
            if arr[x+1] < arr[x]:
                temp = arr[x]
                arr[x] = arr[x+1]
                arr[x+1] = temp
            x+=1

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr


if __name__ == "__main__":
    arr = [5, 55, 6, 67, 16, 9, 25, 43, 12]
    # print(selection_sort(arr))

    print("---" * 10)
    print(bubble_sort(arr))

    arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    # breakpoint()