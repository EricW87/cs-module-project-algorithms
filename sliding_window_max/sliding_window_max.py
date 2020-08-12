'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    max_arr = [] #array of maximums
    cur_window = []#holds current window value

    #first window - it doesn't behave like the others
    max_num = nums[0]
    max_index = 0
    index = 1

    while index < k: 
        if nums[index] > max_num:
            max_num = nums[index]
            max_index = index

        index += 1

    max_arr.append(max_num)
    #end first window

    first_in_window = 1
    #2nd window and greater
    while index < len(nums):
        #print("cur_window " + str(cur_window))
        if max_index < first_in_window:
            max_num = nums[first_in_window]
            max_index = first_in_window
            
            for i in range(first_in_window + 1, first_in_window + k):
                if(nums[i] >= max_num):
                    max_num = nums[i]
                    max_index = i
        elif nums[index] >= max_num:
            max_num = nums[index]
            max_index = index


        index += 1
        first_in_window += 1
        max_arr.append(max_num)       
    #end windows2+

    return max_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
