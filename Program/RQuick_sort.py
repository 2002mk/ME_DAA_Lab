import random
# Function to find the partition position
def partition(array, low, high):
    # Choose a random pivot position
    randomNumber = random.randint(low, high)

    # Swap the pivot element with the last element of the array
    array[randomNumber], array[high] = array[high], array[randomNumber]

    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for the greater element
    i = low - 1
    swap = 0

    # Traverse through all elements
    # Compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # Swap it with the greater element pointed by i
            i += 1
            array[i], array[j] = array[j], array[i]
            swap += 1

    # Swap the pivot element with the greater element specified by i
    array[i + 1], array[high] = array[high], array[i + 1]

    # Return the position from where partition is done
    return i + 1

# Function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # elements smaller than pivot are on the left
        # elements greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

# Input
data = []
n = int(input("\nEnter number of elements: "))
for i in range(n):
    ele = int(input("Enter the element: "))
    data.append(ele)

print("\nOriginal array:", data)

# Sorting
quickSort(data, 0, n - 1)

print("\nSorted Array in Ascending Order:", data)