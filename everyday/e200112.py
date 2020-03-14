# heapify subtree rooted at index i
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    # if left child of root exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
    # if right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
    # change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)


# nlogn
def heapsort(arr):
    n = len(arr)
    # build a maxheap
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    # one by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


arr = [3, 1, 5, 6]
heapsort(arr)
print(arr)
