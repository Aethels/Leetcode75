def binary_search(nums, target):
  # nums is a sorted array of integers
  # target is an integer to be searched
  # returns the index of target in nums, or -1 if not found
  
  # initialize the left and right pointers
  left = 0
  right = len(nums) - 1
  
  # loop until left and right pointers meet
  while left <= right:
    # find the middle index
    mid = (left + right) // 2
    
    # check if the middle element is the target
    if nums[mid] == target:
      return mid # return the index
    
    # if the target is smaller than the middle element
    elif target < nums[mid]:
      # discard the right half of the array
      right = mid - 1
    
    # if the target is larger than the middle element
    else:
      # discard the left half of the array
      left = mid + 1
  
  # if the loop ends without finding the target
  return -1 # return -1 to indicate not found

# read the input from standard input and evaluate it as a Python expression
arr = input("Lütfen bir tam sayı dizisi girin: ")
arr = eval(arr)

# read the target from standard input and convert it to an integer
target = int(input("Lütfen hedef sayıyı girin: "))

# call the function and print the result
result = binary_search(arr, target)
print(result) # prints the index of target in arr, or -1 if not found
