# It is an optimization technique.
# Given an array of integers of size N, find maximum sum of K consecutive elements

def maxSum(arr, WindowSize):
    arraySize = len(arr)
    if( arraySize <= WindowSize):
        print("Invalid operation")
        return -1
    
    window_sum = sum( [arr[i] for i in range(WindowSize)])
    max_sum = window_sum

    # To compute the new sum, we remove (subtract) the first element in the previous window AND add the second element in the NEW WINDOW

    for i in range(arraySize-WindowSize):
        window_sum = window_sum - arr[i] + arr[i + WindowSize]
        max_sum = max(window_sum, max_sum)


    return max_sum


arr = [80, -50, 90, 100]
k = 2                       # window size
answer = maxSum(arr, k) # Final answer should be 190
print(answer)