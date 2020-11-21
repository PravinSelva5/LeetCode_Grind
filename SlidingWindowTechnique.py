# It is an optimization technique.
# Given an array of integers of size N, find maximum sum of K consecutive elements


'''
USEFUL FOR:
    - Things we iterate over sequentially
        - Look for words such as contiguous, fixed sized
        - Strings, arrays, linked-lists
    - Minimum, maximum, longest, shortest, contained with a specific set
        - maybe we need to calculate something
        



'''

def maxSum(arr, WindowSize):
    arraySize = len(arr)
    if( arraySize <= WindowSize):
        print("Invalid operation")
        return -1
    
    window_sum = sum( [arr[i] for i in range(WindowSize)])
    max_sum = window_sum

    # To compute the new sum, we remove (subtract) the first element in the previous window AND add the second element in the NEW WINDOW

    for i in range(arraySize-WindowSize):
        window_sum = window_sum - arr[i] + arr[i + WindowSize]   # This is where you subtract the first element from the previous window and ADD the second element of the NEW WINDOW
        max_sum = max(window_sum, max_sum)


    return max_sum


arr = [80, -50, 90, 100]
k = 2                       # window size
answer = maxSum(arr, k) # Final answer should be 190
print(answer)