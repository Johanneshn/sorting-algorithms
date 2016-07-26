import numpy as np
import timeit

#Sorting algorithms

def main():
    randomArr = np.random.randint(10,size=10)
    insertion_sort(randomArr)
    print timeit.timeit("insertion_sort", setup="from __main__ import insertion_sort", number=1)

def bubble_sort(arr):
    print("# Bubbel sort \n# Unsorted array: ")
    print(arr)

    n = len(arr)-1
    for j in range(n,0,-1):
        for i in range(j):
            if arr[i]>arr[i+1]:
             arr[i], arr[i+1] = arr[i+1], arr[i]

    print("# Sorted array: ")
    print(arr)


def insertion_sort(arr):

    n = len(arr)-1
    for j in range(1,n,1):
        x = j
        while x>0 and arr[x]<arr[x-1]:
            arr[x],arr[x-1] = arr[x-1],arr[x]
            x = x-1

    print("# Sorted array: ")
    print(arr)


if __name__ == "__main__":
    main()
