import numpy as np
import timeit

#Sorting algorithms

def main():
    randomArr = np.random.randint(10000,size=100)
    insertion_sort(randomArr)
    bubble_sort(randomArr)


def bubble_sort(arr):

    start_time = timeit.default_timer()
    n = len(arr)-1
    for j in range(n,0,-1):
        for i in range(j):
            if arr[i]>arr[i+1]:
             arr[i], arr[i+1] = arr[i+1], arr[i]

    elapsed = timeit.default_timer() - start_time
    print(elapsed)




def insertion_sort(arr):

    start_time = timeit.default_timer()
    n = len(arr)-1
    for j in range(1,n,1):
        x = j
        while x>0 and arr[x]<arr[x-1]:
            arr[x],arr[x-1] = arr[x-1],arr[x]
            x = x-1

    elapsed = timeit.default_timer() - start_time

    print(elapsed)



if __name__ == "__main__":
    main()
