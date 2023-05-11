def selectionSort(array): 
    
    for ind in range(len(arr)): 
        min_index = ind # set the minimum value of array to first position 
 
        for j in range(ind + 1, len(arr)): 
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
selectionSort(arr)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)  