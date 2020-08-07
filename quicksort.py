from animate import Plot
def partition(data, start, end):
    b = (start - 1) 
    pivot = data[end] 

    for i in range(start, end):

        if data[i] <= pivot:
            b += 1
            data[b], data[i] = data[i], data[b]


            Plot(pivot, data)

    data[b + 1], data[end] = data[end], data[b + 1]
    return b + 1


def quickSort(data, start, end):
    if start < end:
        
        p = partition(data, start, end)

        
        quickSort(data, start, p - 1)
        quickSort(data, p + 1, end)