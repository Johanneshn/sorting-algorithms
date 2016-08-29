
import timeit

#Sorting algorithms

def main():
    randomArr = [ 1,47, 71, 45, 75, 87, 58, 20, 54, 62]
    #insertion_sort(randomArr)
    #bubble_sort(randomArr)
    merge_sort(randomArr)



def merge_sort(arr):


    if (len(arr) > 1):
        mid_arr = len(arr)//2
        left_arr = arr[:mid_arr]
        right_arr = arr[mid_arr:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0
        j = 0
        k = 0


        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i = i+1
            else:
                arr[k] = right_arr[j]
                j = j+1
            k = k + 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i = i + 1
            k = k + 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j = j + 1
            k = k + 1


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
