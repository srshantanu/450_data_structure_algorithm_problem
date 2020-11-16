def reverse_array(arr):
    i = 0
    j = len(arr)-1
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i+=1
        j-=1

    return "".join(arr)


def recursive_reverse_array(arr,start,end):
    if start >= end:
        return
    else:
        arr[start],arr[end] = arr[end],arr[start]
        recursive_reverse_array(arr,start+1,end-1)


if __name__ == "__main__":
    t = int(input(""))
    for _ in range(t):
        arr = list(map(str, input()))

        # Normal Approach
        print(reverse_array(arr))

        # Recursive Approch
        print(recursive_reverse_array(arr,0,len(arr)-1))