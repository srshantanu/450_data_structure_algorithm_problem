class Pair():
    def __int__(self):
        self.min = 0
        self.max = 0


# basic linear search
def max_min_array(arr):
    arr_len = len(arr)
    minmax = Pair()

    if arr_len == 1:
        minmax.min = arr[0]
        minmax.max = arr[0]
        return minmax

    if arr[0] < arr[1]:
        minmax.min = arr[0]
        minmax.max = arr[1]
    else:
        minmax.min = arr[1]
        minmax.max = arr[0]

    for val in range(2,arr_len):
        if arr[val] < minmax.min:
            minmax.min = arr[val]
        elif minmax.max < arr[val]:
            minmax.max = arr[val]

    return minmax

# tournament method:
def min_max_tournament(arr,start, end):

    arr_min = arr[start]
    arr_max = arr[start]

    if start == end:
        arr_min,arr_max = arr[start], arr[start]

        return (arr_min , arr_max)

    elif start == end+1:
        arr_max = max(arr[start],arr[end])
        arr_min = min(arr[start],arr[end])

        return (arr_min,arr_max)

    else:
        mid = (start+end)//2
        arr_min1, arr_max1 = min_max_tournament(arr,start,mid)
        arr_min2,arr_max2 = min_max_tournament(arr,mid+1,end)

        return (min(arr_min1,arr_min1), max(arr_max1,arr_max2))




if __name__ == "__main__":
    t = int(input(""))
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        max_min = max_min_array(arr)

        # normal method
        print(max_min.min,max_min.max)

        # Tournament Method:
        print(min_max_tournament(arr,0,len(arr)-1))
