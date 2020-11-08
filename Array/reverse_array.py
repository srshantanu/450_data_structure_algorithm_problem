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


if __name__ == "__main__":
    t = int(input(""))
    for _ in range(t):
        arr = list(map(str, input()))

        print(reverse_array(arr))