def even_parity(arr):
    element = 0
    for data in arr:
        element = element^data
    return element